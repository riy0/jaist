def qsort(L):
    if L == []:
        return []
    else:
        x = L[0]
        M = L[1:]
        L1 = [ y for y in M if y <= x ]
        L2 = [ y for y in M if y >  x ]
        return qsort(L1) + [x] + qsort(L2)

print(qsort([1,3,5,4,2]))
