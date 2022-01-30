import math
import matplotlib.pyplot as plt


def f(t):
    # JUST CHANGE THE FUNCTION HERE
    return math.sin(t)


def integrate(f):
    # UGLY BUT QUICK INTEGRATION CODING
    x = 0
    n = 0
    sum = 0
    while x <= 100:
        y = f(x)
        sum += y
        x += 0.01
        n += 1
    average = sum/n
    return average*100


def laplaceTransform(f,s):
    # GETS THE LAPLACE TRANSFORM AT S
    def g(t):
        return math.exp(-s*t)
    return integrate(g)


# PLOT IT
xpoints = []
ypoints = []
x = 0
while x < 3:
    y = laplaceTransform(f,x)
    ypoints.append(y)
    xpoints.append(x)
    x += 0.1
plt.plot(xpoints,ypoints)
plt.grid()
plt.axhline(c="r")
plt.axvline(c="r")
plt.title("The Laplace Transform of the function f(t) = sin(t)")
plt.show()

# QUIT
quit()