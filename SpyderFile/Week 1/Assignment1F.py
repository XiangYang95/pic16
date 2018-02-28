import math

def f(x):
    y = x**2 - 1.0
    return y

def fder(x):
    z = 2 * x
    return z

def g(x):
    y = math.sin(x)
    return y

def gder(x):
    z = math.cos(x)
    return z

def h(x):
    y = math.log(x) - 1.0
    return y

def hder(x):
    z = 1.0/x
    return z

f_tuple = (f, fder)

g_tuple = (g, gder)

h_tuple = (h, hder)

def solve(func_tuple, x):
    while abs(func_tuple[0](x)) > 0.0001:
        x = x - func_tuple[0](x)/func_tuple[1](x)
            
    print x
    
solve(f_tuple, 3)
solve(f_tuple, -0.5)
solve(g_tuple, 2)
solve(h_tuple, 1.5)

