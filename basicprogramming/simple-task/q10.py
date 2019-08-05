import math

def integral(f,a,b):
    n = 10000
    d = (b-a) / n
    y = 0
    for k in range(1, n):
        y = y + f(a+k*d)
    return d * ((f(a) + f(b)) / 2 + y)

print(integral(lambda x: x*x, 3,6))
print(integral(lambda x: x*math.sin(x),0, 2 * math.pi))

def derivative(f, x):
    d = 0.00000001
    return (f(x+d) - f(x)) / d

def newton(f,x):
    d = 0.00000001
    if abs(f(x)) < d:
        return x
    else: return newton(f, x - f(x) / derivative(f,x))

print(newton(labbda x: x*x - 2, 1 ))


