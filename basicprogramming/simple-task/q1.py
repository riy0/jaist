def factorial(n):
    x = 1
    for i in range(n+1):
        x = x*i
    return x

def fib(n):
    x = 0
    y = 1
    for i in range(n):
        (x, y) = (y, x+y)
    return x

"""
x0 = x
 x = y
 y = x0 + y
"""

def leibniz(n):
    x = 0
    s = 1
    for i in range(n):
        x = x+ s*4 / (2*i +1)
        s = -s
    return x

print(factorial(10))
print(fib(5)) 
print(leibniz(10000))
