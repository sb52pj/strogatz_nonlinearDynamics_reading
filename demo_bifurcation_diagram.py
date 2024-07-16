#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
# @Author : Xu Inter
# @Created Time : 2023-05-11 10:14:12
# @Description : 
"""


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def ode(x, r):
    return r + x - np.log(1+x)
    return 1 + r*x + x**2 
    return r - np.sin(x)

r_values = np.linspace(-10, 10, 100)
x0 = np.pi / 2  # initial condition

x_values = []
for r in r_values:
    sol = solve_ivp(lambda t, x: ode(x, r), [0, 100], [x0])
    x_values.append(sol.y[0][-1])


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def system(x, r):
    return r - np.sin(x)

r_values = np.linspace(0, 10, 1000)

def guess(x_guesses, handle):
  stable_branch = []
  unstable_branch = []
  
  for i in range(len(r_values)):
      r = r_values[i]
      x_guess = x_guesses[i]
      sol, info, ier, msg = fsolve(ode, x_guess, args=(r,), full_output=True)
      if ier == 1 and sol > 0:
          stable_branch.append((r, sol))
      elif ier == 1 and sol < 0:
          unstable_branch.append((r, sol))
      else:
          pass


  stable_branch = np.array(stable_branch)
  unstable_branch = np.array(unstable_branch)

  print(stable_branch, len(stable_branch))
  if len(stable_branch) != 0:
      handle.plot(stable_branch[:,0], stable_branch[:,1], '-', markersize=1)
  else:
      pass
  if len(unstable_branch) != 0:
      handle.plot(unstable_branch[:,0], unstable_branch[:,1], '.', markersize=1)
  else:
      pass 


fig,(axb,axf) = plt.subplots(1,2)

x_guesses = np.ones(len(r_values)) * 10
guess(x_guesses, axb)
x_guesses = np.ones(len(r_values)) * 2
guess(x_guesses,axb)
x_guesses = np.ones(len(r_values)) 
guess(x_guesses,axb)



#plt.xlabel('r')
#plt.ylabel('x')
#plt.title('Bifurcation diagram')
#plt.show()


#axb.plot(r_values, x_values)
axb.set_xlabel('r')
axb.set_ylabel('x')
axb.set_title('Bifurcation diagram')

xrange = np.arange(-10,10)
axf.plot(xrange, ode(xrange,2), label= 'r=2')
axf.plot(xrange, ode(xrange,1), label= 'r=1')
axf.plot(xrange, ode(xrange,0.5), label= 'r=0.5')

axf.axhline(0, linestyle ="--", color = 'gray')
plt.legend()

axf.set_title('vector field')
axf.set_ylabel('$\dot x$')
axf.set_xlabel('x')
plt.show()
