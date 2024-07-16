
import numpy as np
import matplotlib.pyplot as plt

# Define the systems of differential equations
def system1(x, r):
    return 1 + r * x + x**2

def system2(x, r):
    return r - np.cosh(x)

def system3(x, r):
    return r + x - np.log(1 + x)

def system4(x, r):
    return r + 0.5 * x - x / (1 + x)

# Define the range of x and r values
x_range = np.linspace(-10, 10, 40)
r_range = np.linspace(-4, 4, 10)

# Define the function for drawing slope fields
def slope_field(system, r, ax):
    #print(type(ax),dir(ax))
    #ax.set_title('Slope Field: r={}'.format(r))
    #ax.set_xlabel('x')
    #ax.set_ylabel('dx/dt')
    #for x in x_range:
    #    dx = system(x, r)
    #    dy = 1
    #    ax.quiver(x, 0, dx, dy, angles='xy', scale_units='xy', scale=10)
    ax.plot(x_range, system(x_range,r))
    ax.axhline( 0, linestyle ="--", color = 'gray') # x数值应与dt挂钩


# Draw slope fields for different r values
fig, ax = plt.subplots(4,10)
for index,r in enumerate(r_range):
    slope_field(system1, r, ax[0][index] )
    slope_field(system2, r, ax[1][index] )
    slope_field(system3, r, ax[2][index] )
    slope_field(system4, r, ax[3][index] )

for index,r in enumerate(r_range):
    ax[3][index].set_xlabel('r={}'.format(np.round(r,1)))

# Define the function for finding the fixed points of a system
from scipy.optimize import fsolve
def fixed_points(system, r):
    def f(x):
        return system(x, r)
    x_range = np.linspace(-10, 10, 10)
    roots =fsolve(f, x_range)
    fixed_points = []
    for root in roots:
        if np.isreal(root) and root.imag == 0:
            fixed_points.append(root)
    return fixed_points

# Define the function for drawing bifurcation diagrams
fig, ax = plt.subplots(2,2)

r_range = np.linspace(-4, 4, 60)
def bifurcation_diagram(system, ax):
    ax.set_title('Bifurcation Diagram')
    ax.set_xlabel('r')
    ax.set_ylabel('Fixed Points')
    for r in r_range:
        fixed_point = fixed_points(system, r)
        for fp in fixed_point:
            ax.plot(r, fp, 'k.', markersize=2)

# Draw bifurcation diagrams for each system
bifurcation_diagram(system1, ax[0,0])
bifurcation_diagram(system2, ax[0,1])
bifurcation_diagram(system3, ax[1,0])
bifurcation_diagram(system4, ax[1,1])


plt.show()
