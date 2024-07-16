import numpy as np
import matplotlib.pyplot as plt


def ode(x, r):
    # 3.4.11
    #return r * x - np.sin(x)

    # 3.4.15 
    #return 1/2 * r * x**2 + 1/4 * x**4 - 1/6 *x**6

    # 3.3.1 laser
    return x * r / (x + 1) - x

    ## 3.1.5 
    #return r ** 2 + x ** 2
    #return r ** 2 - x ** 2

    ## Pitchfork 3.4.1 - 3.4.4
    return r * x + 4 * x ** 3
    #return r * x - np.sinh(x)
    #return r * x - 4 * x ** 3
    #return x + r * x / ( 1 + x ** 2 )

    ## Transcritical 3.2.1-3.2.4
    #return r * x + x ** 2
    #return r * x - np.log(1+x)
    #return x - r * x * (1-x)
    #return x * (r - np.exp(x))

    ##saddle node 3.1.1-3.1.4
    #return 1 + r*x + x**2 
    #return r - np.cosh(x)
    #return r + x - np.log(1+x)
    #return r + 0.5 * x - x / (1+x)

def plotr(r):
    plt.plot(xrange, ode(xrange,r), label= 'r={}'.format(r))

#bug
xrange = np.linspace(-10,10, 10)

xrange = np.linspace(-10,10, 100)
xrange = np.linspace(-4,4, 100)
xrange = np.linspace(-0.1,4, 100)
#xrange = np.linspace(-0.01,0.01, 100)

R = 10
#R = 1
for r in np.round(np.linspace(-R,R,5),2):
    plotr(r)
#plt.plot(xrange, ode(xrange,2), label= 'r=2')
#plt.plot(xrange, ode(xrange,1), label= 'r=1')
#plt.plot(xrange, ode(xrange,0.5), label= 'r=0.5')
#
plt.legend()
plt.axhline(0, linestyle ="--", color = 'gray')
#plt.title("$ \dot x = rx + 4 x ^ 3 $")
   
#plt.title(" $\dot x = r  x - \ln(1+x)$")
#plt.title("  $\dot x = r - \cosh x$ ")
   


#plt.savefig('#fig/Pitchfork.png')
plt.show()
