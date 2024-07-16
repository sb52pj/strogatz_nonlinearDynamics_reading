#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
# @Author : Xu Inter
# @Created Time : 2023-05-04 15:19:05
# @Description : 
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the differential equations
def eq1(x, t):
    return -x**3

def eq2(x, t):
    return -x

# Set initial conditions and time range
x0 = 1
t = np.linspace(0, 30, 1000)

# Solve the differential equations using Euler's method
def euler(f, x0, t):
    x = np.zeros_like(t)
    x[0] = x0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        x[i] = x[i-1] + f(x[i-1], t[i-1]) * dt
    return x

# Solve the differential equations using Runge-Kutta method
def rk4(f, x0, t):
    x = np.zeros_like(t)
    x[0] = x0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        k1 = f(x[i-1], t[i-1])
        k2 = f(x[i-1] + 0.5*dt*k1, t[i-1] + 0.5*dt)
        k3 = f(x[i-1] + 0.5*dt*k2, t[i-1] + 0.5*dt)
        k4 = f(x[i-1] + dt*k3, t[i-1] + dt)
        x[i] = x[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4) * dt
    return x

# Solve and plot the solutions using Euler's method
#plt.subplot(211)
plt.plot(t, euler(eq1, x0, t), label='x\' = -x^3')
plt.plot(t, euler(eq2, x0, t), label='x\' = -x')
plt.title('Euler\'s method')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()

## Solve and plot the solutions using Runge-Kutta method
#plt.subplot(212)
#plt.plot(t, rk4(eq1, x0, t), label='x\' = -x^3')
#plt.plot(t, rk4(eq2, x0, t), label='x\' = -x')
#plt.title('Runge-Kutta method')
#plt.xlabel('t')
#plt.ylabel('x')
#plt.legend()

plt.tight_layout()
plt.show()
