def member(x,L):
    for y in L:
        if x == y:
            return True
        return False

def gcd(x,y):
    """
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    """
    while y > 0:
        (x,y) = (y, x % y)
    return x


def f(x):
    return x * x -2

def bisection(a, b):
    e = 0.000000001
    c = (a + b) / 2
    if abs(a - b) < e:
        return c
    elif f(a) * f(c) <= 0:
        return bisection(a,c)
    else 
        return bisection(c,b)


def g(x,z):
    return x * x -z

def root(z):
    e = 0.000000001
    a = 0
    b = z + 1
    while abs(a -b) > e:
        c = (a + b) / 2
        if g(a,z) * g(c,z) <= 0:
            b = c
        else:
            a = c
    return (a + b) /2


print(gcd(24,32)) 
print(bisection(0,3))
print(root(4))
