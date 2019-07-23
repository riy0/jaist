def mymap(f, L):
    M = []
    for x in L:
        M.append(f(x))
    return M

def concat(L):
    M = []
    for Li in L:
        M = M + Li
    return M

def product(L1, L2):
    M = []
    for x in L1:
        for y in L2:
            M.append((x,y))
    return M

def reverse(L):
    n = len(L)
    for i in range(0, n // 2):
        (L[i], L[n - i - 1]) = (L[n - i - 1], L[i])

def bsort(L):
    for i in range(0, len(L)-1):
        for j in range(0, len(L)-i-1):
            if L[j] > L[j+1]:
                (L[j], L[j+1]) = (L[j+1], L[j])


print( mymap(lambda x: x*2, [1,2,3]) )
print( concat([[1,2,3],[4],[5,6]]) )
print( product([1,2,3],["a","b"]) )
