import numpy as np
import matplotlib.pyplot as plt


def derivative(x=float, delta=float):
    """This function takes the derivative of x*(x-1) as the limit delta goes to 0 utilizing the definition of a derivative."""

    def f(x): return x*(x - 1)  # defines the function f(x) =  x*(x-1)

    return((f(x+delta) - f(x))/delta)  # returns the derivate of f(x)


VectDeriv = np.vectorize(derivative)  # vectorizes the derivative function

# an array holding values of delta
deltaDomain = np.array([1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14])

y_axis = np.round(VectDeriv(1, deltaDomain), 15)

print(y_axis)

# creates a scatter plot of the values of the derivative vs delta
plt.scatter(x=deltaDomain, y=y_axis)
plt.title("Derivate of f(x) at x = 1 vs $\delta$")
plt.ylabel("d/dx(f(1))")
plt.xlabel("$\delta$")
plt.show()
