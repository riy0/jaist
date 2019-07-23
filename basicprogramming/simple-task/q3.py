def mul(A, B):
    l = len(A)
    m = len(A[0])
    n = len(B[0])
    C = []
    for i in range(0, l):
        Ci = []
        for j in range(0, n):
            Cij = 0
            for k in range(0, m):
                Cij = Cij + A[i][k] * B[k][j]
            Ci = Ci + [Cij]
        C = C + [Ci]
    return C

