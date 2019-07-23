def next(A, L):
    M = L[:]
    for x in L:
        for y in A[x]:
            if y not in M:
                M.append(y)
    return M

def succ(A, x):
    L = [x]
    while True:
       M = next(A, L)
       if L == M:
          return L
       L = M

A = { 0: [2], 1: [2], 2: [1,3], 3: [4,5], 4: [4], 5: [] }
print(succ(A, 2))
