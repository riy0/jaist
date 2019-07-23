import random
import time

def merge(L1, L2):
    M = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            M.append(L1[i])
            i = i + 1
        else:
            M.append(L2[j])
            j = j + 1
    M.extend(L1[i:])
    M.extend(L2[j:])
    return M

def msort(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        return merge(msort(L[0:n//2]), msort(L[n//2:n]))

def bsort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                (L[j], L[j+1]) = (L[j+1], L[j])

def qsort(L):
    if L ==[]:
        return []
    else:
        x = L[0]
        L1 = [y for y in L[1:] if y <= x]
        L2 = [y for y in L[1:] if y > x]
        return qsort(L1) + [x] + qsort(L2)

def duration(f,x):
    start = time.time()
    y = f(x)
    return(y, time.time() -start)


L = [ random.randint(0, 10000) for i in range(0, 10000) ]
M = L[:]

print("-- bsort --")
(_, bsort_duration) = duration(bsort, M)
print(M, len(M))

print("-- qsort --")
(M, qsort_duration) = duration(qsort, L)
print(M, len(M))

print("-- msort --")
(M, msort_duration) = duration(msort, L)
print(M, len(M))

print("bsort:", bsort_duration)
print("qsort:", qsort_duration)
print("msort:", msort_duration)

