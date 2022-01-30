import math
import matplotlib.pyplot as plt


def f(t):
    return math.sin(t)


def integrate(f):
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
    def g(t):
        return math.exp(-s*t)
    return integrate(g)


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


quit()