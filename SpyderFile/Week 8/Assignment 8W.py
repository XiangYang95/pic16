# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:22:50 2018

@author: Xiang Yang Ng
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import trapz
 

N = 50
P = np.pi/2

x_data = np.linspace(0, 1, N)
y_data = np.sqrt(1 - x_data**2)

z0 = np.append(x_data[N-1], y_data[:N-1])

plt.plot(x_data, y_data)

def z2xy(z):
    xs = np.linspace(0, z[0], N)
    ys = np.append(z[1:], 0)
    return xs, ys

x1,y1 = z2xy(z0)

plt.plot(x1,y1)

def obj(k):
    xs, ys = z2xy(k)
    return -trapz(ys, xs)

print obj(z0)

def constraint(z):
    xs, ys = z2xy(z)
    dx = xs[1] - xs[0]
    l = np.sum(np.sqrt(dx**2 + (ys[:-1] - ys[1:])**2))
    return l-P

print constraint(z0)

bounds = [(0,P) for i in range(50)]

con = {"type": "eq", "fun": constraint}

result = minimize(obj, z0, bounds = bounds, constraints = con)

new_z0 = np.array([np.random.uniform(0,P) for i in range(50)])

result1 = minimize(obj, new_z0, bounds = bounds, constraints = con)

print result1

x2, y2 = z2xy(new_z0)
plt.plot(x2,y2)