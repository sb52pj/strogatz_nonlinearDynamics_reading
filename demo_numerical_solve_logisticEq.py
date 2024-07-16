import numpy as np
import matplotlib.pyplot as plt

# Define parameters
r = 0.5  # growth rate
K = 100  # carrying capacity
N0 = 10  # initial population size
t = np.linspace(0, 50, 1000)  # time points for plotting

# Define function for logistic equation
def logistic_eq(N, t, r, K):
    dN_dt = r * N * (1 - N / K)
    return dN_dt

# Solve logistic equation numerically using scipy.integrate.odeint
from scipy.integrate import odeint
sol = odeint(logistic_eq, N0, t, args=(r, K))

# Plot solution
plt.plot(t, sol, label='Population')
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Logistic Equation')
plt.legend()
plt.show()
