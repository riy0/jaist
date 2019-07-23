def reverse(L):
    M = []
    for x in L:
        M = [x] + M
    return M

def palindrome(L):
    return L == reverse(L)

def ascending(L):
    for i in range(1,len(L)):
        if not L[i-1] <= L[i]:
            return False
    return True

def maximum(L):
    m = L[0]
    for x in L:
        if x > m:
            m = x
    return m

def join(L, s):
    if L == []:
        return ""
    else:
        t = L[0]
        for i in range(1, len(L)):
            t = t + s+ L[i]
        return t

