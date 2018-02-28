import math
from sympy import *
init_printing(use_latex = 'mathjax')
from IPython.display import display

#steps corresponds to the assignment's procedure
#step 1
t, T, Ie, T0, P, tf = symbols('t T Ie T0 P t_f')
w = Function('w')

e11 = w(t).diff(t) -  T/Ie

#step 2
e12 = T0*(1 - w(t)*T0/(4*P))

#step 3
e13 = e11.subs(T, e12)

#test case
etest = w(t).diff(t) + w(t)*T0**2/(4*P*Ie) - T0/Ie

#prove equality
print "Prove that my result is equivalent to Eq13: MyEq13 - Eq13 =", simplify(e13 - etest)

#step 4
e14 = dsolve(e13, w(t)).rhs

#step 5
k = e14.subs(t, 0)

var("C1")

constant = solve(k, C1)[0]

#step 6
e14 = e14.subs(C1, constant) 

#test case
etest = (-4*P/T0)* exp(-1*(T0**2)*t/(4*P*Ie)) + 4*P/T0

#prove equality
print "Prove that my result is equivalent to Eq14: MyEq14 - Eq14 =", simplify(e14 - etest)

#step 7
e12modified = e12.subs(w(t), e14)

e15 = integrate(e12modified, (t, 0, tf), conds = 'none')

#test case
etest = 4*P*Ie/T0*(1-exp(-T0**2*tf/(4*P*Ie)))

#prove equality
print "Prove that my result is equivalent to Eq15: MyEq15 - Eq15 =", simplify(e15 - etest)

#step 8
e17 = simplify(diff(e15, T0))

#test case
etest = simplify((2*tf + 4*Ie*P/T0**2)*exp(-T0**2*tf/(4*Ie*P))-4*Ie*P/T0**2)

#prove equality
print "Prove that my result is equivalent to Eq17: MyEq17 - Eq17 =", simplify(e17 - etest)


e18 = simplify(solve(e17, T0)[1])

#test case
etest = simplify(sqrt(Ie)*sqrt(P)/sqrt(tf)*sqrt(-2*(1 + 2*LambertW(-1/(2*sqrt(exp(1))), -1))))

print "My equation 18:",
display(e18)

#prove equality
print "Prove that my result is equivalent to Eq18: MyEq18 - Eq18 =", simplify(e18-etest)

