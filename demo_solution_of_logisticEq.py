
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
r = 0.1
K = 100

# Define the time points to evaluate the solution
t = np.linspace(0, 100, 1000)

# Define the initial populations to plot
N0_values = [10, 50, 100, 150]

# Plot the solutions
plt.figure(figsize=(8, 6))
for N0 in N0_values:
    N = K / (1 - (1 - K / N0) * np.exp(-r * t))
    plt.plot(t, N, label=f'N0={N0}')


def logistic_eq(N, t, r, K):
    dN_dt = r * N * (1 - N / K)
    return dN_dt

# Solve logistic equation numerically using scipy.integrate.odeint
from scipy.integrate import odeint
sol = odeint(logistic_eq, N0, t, args=(r, K))

plt.plot(t, sol, label='python odeint', linestyle = '--')

dt = 0.1
# Solve using forward Euler method
N_Euler = np.zeros(len(t))
N_Euler[0] = N0
for i in range(1, len(t)):
    N_Euler[i] = N_Euler[i-1] + dt*logistic_eq(N_Euler[i-1], t[i-1], r, K)

# Solve using fourth-order Runge-Kutta method
N_RK4 = np.zeros(len(t))
N_RK4[0] = N0
for i in range(1, len(t)):
    k1 = dt*logistic_eq(N_RK4[i-1], t[i-1], r, K)
    k2 = dt*logistic_eq(N_RK4[i-1]+k1/2, t[i-1]+dt/2, r, K)
    k3 = dt*logistic_eq(N_RK4[i-1]+k2/2, t[i-1]+dt/2, r, K)
    k4 = dt*logistic_eq(N_RK4[i-1]+k3, t[i-1]+dt, r, K)
    N_RK4[i] = N_RK4[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6

# Plot the results
plt.plot(t, N_Euler, label='Forward Euler', linestyle = '--')
plt.plot(t, N_RK4, label='4th Order Runge-Kutta', linestyle = '--')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()

plt.show()
