import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

eV = constants.eV  # conversion factor of 1.602176634×10^19 J
V = 20*eV
E = eV*np.linspace(0, 20, 1000)
accuracy = 0.001*eV
m = 9.1094E-31  # mass of electron in kg


def y_1(x):
    """This function defines the function y1"""

    w = constants.nano  # equivalent to 1.0 x 10^-9 m
    h = constants.hbar  # reduced planks constant in J*s

    return(eV*np.tan(np.sqrt(((w**2)*m*x) / (2*(h**2)))))


def y_2(x):
    """This function defines the function y2"""

    return(eV*np.sqrt((V - x) / x))


def y_3(x):
    """This function defines the function y2"""

    return(eV*(-np.sqrt(x / (V - x))))


def BinarySearchY1Y2(x1, x2, accuracy):
    """This function contains the algorithm for binary search between two points [x1, x2] in the domain of
    y1 and y2. It will continue to utilize the binary search method until it has calculated a target in y1 and y2 such that the the absolute
    value of the difference of these two targets is less than the value of the selected accuracy. """

    mid = (x1+x2)/2
    # sets the initial absolute value
    initialabsval = np.abs(y_1(mid)-y_2(mid))
    absval = initialabsval

    if initialabsval < accuracy:  # immediately returns the
        return(mid)

    else:

        while absval > accuracy:
            X1 = x1
            X2 = x2
            MID = mid

            x1 = mid

            mid = (x1 + x2)/2
            absval = np.abs(y_1(mid)-y_2(mid))

            if absval < initialabsval:

                X1 = x1
                MID = mid
                initialabsval = absval

            else:

                x2 = mid
                x1 = X1

                mid = (x1 + x2)/2
                X2 = x2
                MID = mid
                absval = np.abs(y_1(mid)-y_2(mid))
                initialabsval = absval

    return(mid/eV)


def BinarySearchY1Y3(x1, x2, accuracy):
    """This function contains the algorithm for binary search between two points [x1, x2] in the domain of
    y1 and y3. It will continue to utilize the binary search method until it has calculated a target in y1 and y3 such that the the absolute
    value of the difference of these two targets is less than the value of the selected accuracy. """

    mid = (x1+x2)/2
    initialabsval = np.abs(y_1(mid)-y_3(mid))
    absval = initialabsval

    if initialabsval < accuracy:
        return(mid)

    else:

        while absval > accuracy:

            X1 = x1
            X2 = x2
            MID = mid

            x1 = mid

            mid = (x1 + x2)/2
            absval = np.abs(y_1(mid)-y_3(mid))

            if absval < initialabsval:

                X1 = x1
                MID = mid
                initialabsval = absval

            else:

                x2 = mid
                x1 = X1

                mid = (x1 + x2)/2
                X2 = x2
                MID = mid
                absval = np.abs(y_1(mid)-y_3(mid))
                initialabsval = absval
    return(mid/eV)

# code that plots the graph of y1, y2, and y3 with the doman in E. It is plotted in units of J.


plt.plot(E,  y_1(E), label="$y_1$")
plt.plot(E, y_2(E), label="$y_2$")
plt.plot(E, y_3(E), label="$y_3$")
plt.xlabel("Energy, J")
plt.ylabel("Allowed Energies, J")
plt.ylim(-0.74E-17, 0.75E-17)
plt.legend()
plt.show()

print(f'The first six energy levels of the electron are:\n\
\nE_0 = {BinarySearchY1Y3(0E-18,0.0E-18, accuracy)} eV\n\
E_1 = {BinarySearchY1Y3(0.1E-18,0.4E-18, accuracy)} eV\n\
E_2 = {BinarySearchY1Y2(0.25E-18,0.5E-18, accuracy)} eV \n\
E_3 = {BinarySearchY1Y3(0.6E-18,1.0E-18, accuracy)} eV \n\
E_4 = {BinarySearchY1Y2(1.1E-18,1.3E-18, accuracy)} eV\n\
E_5 = {BinarySearchY1Y3(1.6E-18,2.0E-18, accuracy)} eV')
