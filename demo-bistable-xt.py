import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the ODE dx/dt = x - x^3
def ode(x, t):
    return x - x**3

# Define the time points to solve the ODE at
t = np.linspace(0, 5, 1000)

# Define the initial conditions
x0_list = [-1.5, -0.5, 0.5, 1.5]

# Solve the ODE for each initial condition
for x0 in x0_list:
    x = odeint(ode, x0, t)
    plt.plot(t, x, label=f'x0 = {x0:.1f}')

# Set the axis labels and legend
plt.xlabel('Time t')
plt.ylabel('x')
plt.legend()

# Show the plot
plt.show()
