# Exercise 1

def maximum(t):
    [l, x, r] = t
    if r == []:
        return x
    else:
        return maximum(r)

def delete(x, t):
    if t == []:
        return t
    else:
        [l, y, r] = t
        if x < y:
            return [delete(x, l), y, r]
        elif x > y:
            return [l, y, delete(x, r)]
        # hereafter, x == y holds
        elif l == []:
            return r
        elif r == []:
            return l
        else:
            z = maximum(l)
            return [delete(z, l), z, r]

t0 = [[], 0, []]
t2 = [[], 2, []]
t4 = [[], 4, []]
t3 = [t2, 3, t4]
t5 = [t3, 5, []]
t1 = [t0, 1, t5]
t7 = [[], 7, []]
t9 = [[], 9, []]
t8 = [t7, 8, t9]
t6 = [t1, 6, t8]

print(delete(5, t6))
print(delete(6, t6))

def succ(A, x):
    M = []
    Q = [x]
    while Q != []:
       u = Q.pop()
       M.append(u)
       for v in A[u]:
           if not v in M:
               Q.append(v)
    return M

A = { 0: [2], 1: [2], 2: [1,3], 3: [4,5], 4: [4], 5: [] }
print(succ(A, 2))

