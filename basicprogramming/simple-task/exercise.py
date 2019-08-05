L = [0, 1, 2]
M = L
L[1] = L[2]
M[0] = M[1]
#print(L)

def f(x, y):
    while x < y:
        x = x - y
    return x

print(f(2018,10))


def map(f, L):
    M = []
    for x in L:
        M.append(f(x))
    return M

print(map(lambda x: x * x, [1, 2, 3]))

for i in range(0, n*n):
    for j in range(0, 2*n):
        x = x + i + j
