from fractions import Fraction
from decimal import Decimal, getcontext

# --------------------------------------------------
# precision
# --------------------------------------------------
getcontext().prec = 100

# --------------------------------------------------
# constants
# --------------------------------------------------
gamma = Decimal(
    "0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495"
)

log2 = Decimal(2).ln()

delta = gamma - log2/Decimal(3) - Decimal(1)/Decimal(3)

# --------------------------------------------------
# harmonic number
# --------------------------------------------------
def H(n):
    s = Decimal(0)
    for k in range(1, n + 1):
        s += Decimal(1) / Decimal(k)
    return s

# --------------------------------------------------
# existing methods (newTable3.py)
# --------------------------------------------------
def detemple(n):
    return H(n) - (Decimal(n) + Decimal("0.5")).ln()

def detemple4(n):
    x = Decimal(n) + Decimal("0.5")
    return (
        H(n)
        - x.ln()
        - Decimal(1)/(Decimal(24)*x*x)
        + Decimal(7)/(Decimal(960)*x**4)
    )

def negoi97(n):
    x = Decimal(n) + Decimal("0.5")
    return (
        H(n)
        - x.ln()
        - Decimal(1)/(Decimal(24)*x*x)
    )

def chen2011_wrong(n):
    x = Decimal(n) + Decimal("0.5") + Decimal(1)/(Decimal(24)*Decimal(n))
    return H(n) - x.ln()

def chen2011(n):

    x = (
        Decimal(n)
        + Decimal("0.5")
        + Decimal(1)/(Decimal(24)*Decimal(n))
        - Decimal(1)/(Decimal(48) * Decimal(n)**2)
    )

    return H(n) - x.ln()

def chen_mortici_2012(n):
    x = (
        Decimal(n)
        + Decimal("0.5")
        + Decimal(1)/(Decimal(24)*Decimal(n))
        - Decimal(1)/(Decimal(48)*Decimal(n)**2)
        + Decimal(23)/(Decimal(5760)*Decimal(n)**3)
    )
    return H(n) - x.ln()

def mortici_p(n):
    x = Decimal(n) + Decimal("0.5")
    return (
        H(n)
        - x.ln()
        - Decimal(1)/(Decimal(24)*x*x)
        + Decimal(7)/(Decimal(960)*x**4)
    )

def mortici_u(n):
    x = Decimal(n) + Decimal("0.5")
    return (
        H(n)
        - x.ln()
        - Decimal(1)/(Decimal(24)*x**2)
        + Decimal(7)/(Decimal(960)*x**4)
        - Decimal(31)/(Decimal(8064)*x**6)
        + Decimal(127)/(Decimal(30720)*x**8)
    )

def mortici_v(n):
    x = Decimal(n) + Decimal("0.5")
    return (
        H(n)
        - x.ln()
        - Decimal(1)/(Decimal(24)*x**2)
        + Decimal(7)/(Decimal(960)*x**4)
        - Decimal(31)/(Decimal(8064)*x**6)
        + Decimal(127)/(Decimal(30720)*x**8)
        - Decimal(511)/(Decimal(67584)*x**10)
    )

# --------------------------------------------------
# Misawa method (newTable2.py)
# --------------------------------------------------
def g(n):
    return Fraction(1, 3) * (
        Fraction(1, 2*n-1)
        + Fraction(4, 2*n)
        + Fraction(1, 2*n+1)
    )

def h(N):

    if N % 2 == 1:
        s = Fraction(0, 1)
        for k in range(1, (N - 1)//2 + 1):
            s += g(k)
        return s

    if N == 4:
        return Fraction(3, 8) * (
            Fraction(1,1)
            + Fraction(3,2)
            + Fraction(3,3)
            + Fraction(1,4)
        )

    if N >= 6:
        return (
            h(N-3)
            + Fraction(3, 8) * (
                Fraction(1, N-3)
                + Fraction(3, N-2)
                + Fraction(3, N-1)
                + Fraction(1, N)
            )
        )

    raise ValueError("N must be >= 3")

def misawa_a(N):
    return 2*h(N) - h(N*N)

# --------------------------------------------------
# scientific notation
# --------------------------------------------------
def sci(x):
    return f"{x:.3E}"


# --------------------------------------------------
# LaTeX scientific notation
# --------------------------------------------------
def latex_sci(x):

    if x == 0:
        return r"$0$"

    s = f"{x:.2E}"

    mantissa, exponent = s.split("E")

    exponent = int(exponent)

    return rf"${mantissa}\times 10^{{{exponent}}}$"

# --------------------------------------------------
# Table header
# --------------------------------------------------
print(r"\begin{tabular}{ccccc}")
print(r"\hline")

print(
    r"$N$"
    r" & $|\delta-a(N)|$"
    r" & $|\gamma_D-\gamma|$"
    r" & $|\gamma_{CM12}-\gamma|$"
    r" & $|\gamma_{MV}-\gamma|$ \\"
)

print(r"\hline")

# --------------------------------------------------
# Table body
# --------------------------------------------------
for N in [10, 50, 100, 500]:

    x = misawa_a(N)

    misawa_dec = (
        Decimal(x.numerator)
        / Decimal(x.denominator)
    )

    row = [

        f"${N}$",

        latex_sci(abs(delta - misawa_dec)),

        latex_sci(abs(detemple(N) - gamma)),

        latex_sci(abs(chen_mortici_2012(N) - gamma)),

        latex_sci(abs(mortici_v(N) - gamma))

    ]

    print(" & ".join(row) + r" \\")

print(r"\hline")
print(r"\end{tabular}")

