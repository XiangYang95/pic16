# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:36:32 2018

@author: Xiang Yang Ng
"""

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt
def f(y, t, m, g, l):
    dy = np.zeros(len(y))
    dy[0] = y[1]
    dy[1] = -g/l*np.sin(y[0])
    return dy

p1 = 1
p2 = 1
p3 = 1

f1 = lambda v,t: f(v,t,p1,p2,p3)

init_cond = [1.0,0.0]

t = np.linspace(0, 10, 101)

sol = spint.odeint(f1, init_cond, t)

plt.plot(t, sol[:,0])
    