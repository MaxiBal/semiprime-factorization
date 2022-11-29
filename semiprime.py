import math

def solveP(N):
    # https://mae.ufl.edu/~uhk/QUICK-SEMI-PRIME-FACTORING.pdf

    found = False
    prev_Nf_N = 18446744073709551629 + 18446744073709551653 - 10

    p = 0
    q = 0

    while not found:
        Nf_N = prev_Nf_N + 1
        determinant = math.sqrt(math.pow(Nf_N / 2, 2) - N)
        half_Nf_N = Nf_N * 0.5

        p = half_Nf_N - determinant
        q = half_Nf_N + determinant

        #print(p, q)

        if p * q == N:
            found = True

    return p, q

p, q = solveP(340282366920938464385711811117245792737)

print("P:", p, "Q:", q)