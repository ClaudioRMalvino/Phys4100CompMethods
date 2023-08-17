import numpy as np
import matplotlib.pyplot as plt

""" Deltoid Curve"""

# creates an array of 2000 evenly spaced elements from 0 to 10pi
theta = np.linspace(0, 2*np.pi, 2000)
x = 2*np.cos(theta) + np.cos(2*theta)  # calculates the x values
y = 2*np.sin(theta) - np.sin(2*theta)  # calculates the y values

plt.figure(1)
plt.plot(x, y)  # creates a plot of the x and y values
plt.title("Deltoid Curve")


"""" Galilean Spiral """

# creates an array of 2000 evenly spaced elements from 0 to 10pi
theta2 = np.linspace(0, 10*np.pi, 2000)
r = theta2**2  # calculates for r
x = r*np.cos(theta2)  # calculates the x values
y = r*np.sin(theta2)  # calculates the y values

plt.figure(2)
plt.plot(x, y)  # creates  a plot of the x and y values
plt.title("Galilean Spiral")

"""Fey's Function"""

# creates an array of 2000 evenly spaced elements from 0 to 24pi
theta3 = np.linspace(0, 24*np.pi, 2000)
r = np.exp(np.cos(theta3)) - 2*np.cos(4*theta3) + \
    np.sin(theta3/12)**5  # calculates for r
x = r*np.cos(theta3)  # calculates the x values
y = r*np.sin(theta3)  # calculates the y values

plt.figure(3)
plt.plot(x, y)  # creates a plot of the x and y values
plt.title("Fey's Function")

plt.show()  # prints all three figures
