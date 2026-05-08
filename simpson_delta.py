import math

# --- constants  ---
gamma = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495
delta = gamma - math.log(2)/3 - 1/3

# --- g(k) ---
def g(k):
    tmp = 2 * k
    return (1.0/(tmp-1) + 4.0/tmp + 1.0/(tmp+1)) / 3.0

# --- h(N) ---
def h(N):
    if N % 2 == 1: # N odd
        M = (N - 1) // 2
        s = 0.0
        for k in range(1, M+1):
            s += g(k)
        return s
    else: # N even 
        return h(N-1) + (1.0/6.0) * (
            1.0/(N-1) +
            4.0/(N-0.5) +
            1.0/N
        )

# --- r(N) ---
def r(N):
    if N % 2 == 1:
        if N < 3:
            return None
        return 1.0 / (15.0 * (N-1)**4)
    else:
        if N < 4:
            return None
        return (
            1.0 / (15.0 * (N-2)**4) +
            1.0 / (120.0 * (N-1)**5)
        )

# --- a(N) ---
def a(N):
    return 2.0 * h(N) - h(N*N)

# --- output ---
print("N\ta(N)\tdelta-a(N)\tr(N)")

for N in range(3, 41):
    val = a(N)
    diff = delta - val
    bound = r(N)

    print(N, val, diff, bound, sep="\t", end=" \\\\\n")
