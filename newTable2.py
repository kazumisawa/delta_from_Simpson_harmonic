from fractions import Fraction
from decimal import Decimal, getcontext

# --------------------------------------
# precision
# --------------------------------------

getcontext().prec = 100

# --------------------------------------
# true delta
# --------------------------------------

gamma = Decimal(
    "0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495"
)

log2 = Decimal(2).ln()

delta = gamma - log2/Decimal(3) - Decimal(1)/Decimal(3)

# --------------------------------------
# Simpson-type functions
# --------------------------------------

def g(n):
    return Fraction(1, 3) * (
        Fraction(1, 2*n-1)
        + Fraction(4, 2*n)
        + Fraction(1, 2*n+1)
    )

def h(N):

    # odd N >= 3

    if N % 2 == 1:

        if N < 3:
            raise ValueError("odd N must be >= 3")

        s = Fraction(0, 1)

        for k in range(1, (N - 1)//2 + 1):
            s += g(k)

        return s

    # N = 4

    if N == 4:

        return Fraction(3, 8) * (
            Fraction(1, 1)
            + Fraction(3, 2)
            + Fraction(3, 3)
            + Fraction(1, 4)
        )

    # even N >= 6

    if N >= 6:

        return (
            h(N - 3)
            + Fraction(3, 8) * (
                Fraction(1, N - 3)
                + Fraction(3, N - 2)
                + Fraction(3, N - 1)
                + Fraction(1, N)
            )
        )

    raise ValueError("N must be >= 3")

def a(N):
    return 2*h(N) - h(N*N)

# --------------------------------------
# LaTeX scientific notation
# --------------------------------------

def latex_sci(x):

    s = f"{x:.2E}"

    mantissa, exponent = s.split("E")

    exponent = int(exponent)

    return rf"{mantissa}\times 10^{{{exponent}}}"

# --------------------------------------
# Table 2
# --------------------------------------

print(r"$N$ & $a(N)$ & $|\delta-a(N)|$ & $r(N)$ \\")
print(r"\hline")

for N in range(3, 21):

    x = a(N)

    a_dec = Decimal(x.numerator) / Decimal(x.denominator)

    err = abs(delta - a_dec)

    a_str = f"{a_dec:.12f}"

    if N >= 6:

        r = Decimal(1) / (Decimal(N) - Decimal(4))**4

        r_str = latex_sci(r)

    else:

        r_str = r"--"

    err_str = latex_sci(err)

    print(
        f"${N}$"
        f" & ${a_str}$"
        f" & ${err_str}$"
        f" & ${r_str}$"
        r" \\"
    )
