# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:42:11 2018

@author: Lenovo
"""
import math 
from sympy import *
from IPython.display import display

init_printing(use_latex = "mathjax")

a, b, c, x, y, n = symbols("a b c x y n ")
k = solve(a*x**2 + b*x + c, x)
display(k)

print solve(x**2 - x - 1, x)

print diff(x**x, x)

print integrate(x* exp(x))

print integrate(sin(x)/ x, (x, -oo, 0))

print sinh(x).rewrite(exp(x))

print Integer(1)/2

a = 2*sin((x+y)/2)*cos((x-y)/2)

b = sin(x) + sin(y)

print a.equals(b)

expr = exp(n*math.pi*I)
print expr.subs(n, (Integer(3)/2))

f =  lambdify(n, expr, "sympy")

display(f(2))