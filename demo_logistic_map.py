import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

# Set the parameters
x0 = 0.5  # initial condition
n = 1000  # number of iterations
r_vals = [r/100 for r in range(200, 400)]  # bifurcation parameter range

# Generate the logistic map for each value of r
x = [x0]
for r in r_vals:
    for i in range(n-1):
        x.append(logistic_map(r, x[-1]))
    plt.plot([r]*len(x), x, 'r.', markersize=0.5)
    x = [x0]

# Plot the bifurcation diagram
plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcation diagram for logistic map')
plt.show()
