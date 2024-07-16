import numpy as np
import matplotlib.pyplot as plt

def ode(x):

    # saddle node
    return - x ** 2
    # 3.1.1
    #return np.cosh(x)
    #return (x ** 2 + 1 )/ x

    # 3.4.15
    #return x **2 - x **4

    # 3.1.2 
    #return x

    ## 3.3.2
    #return 1/ (x ** 2 -1)
    #
    ## 3.4.11
    return np.sin(x) / x
  
    ## 3.4.13 
    #return - np.log(x-1) / x
    #return x + np.exp(x)

    return x / np.tanh(x)

def derivatives(x):
    return 2 * x

x = np.linspace(-10,10, 100)
beta = ode(x)
det = derivatives(x)
plt.xlabel('r')
plt.ylabel('x')
plt.axhline(0, linestyle ="--", color = 'gray')
plt.plot(beta,x)
plt.plot(det,x, '.')
#plt.savefig('fig/###betatanhx_bifurcation.png')
plt.show()

    



