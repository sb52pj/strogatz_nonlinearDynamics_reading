
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz system equations
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# Set the initial conditions
x0, y0, z0 = (0.1, 0.0, 0.0)

# Set the parameters
s = 10
r = 28
b = 2.667

# Set the time step and duration of the simulation
dt = 0.01
t_max = 50
n = int(t_max/dt)

# Initialize the solution arrays
x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

# Set the initial values
x[0], y[0], z[0] = (x0, y0, z0)

# Simulate the Lorenz system
for i in range(n-1):
    x_dot, y_dot, z_dot = lorenz(x[i], y[i], z[i], s, r, b)
    x[i+1] = x[i] + x_dot * dt
    y[i+1] = y[i] + y_dot * dt
    z[i+1] = z[i] + z_dot * dt

# Plot the Lorenz attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz attractor')
plt.show()
