import numpy as np

# asks user to input a height
h = float(input("Enter the height of the tower in meters: "))
g = 9.81    # gravitational constant

t = np.sqrt((2*h)/g)    # gives time in seconds until the ball hits the ground

print(
    f'The ball takes {t:.2} seconds to hit the ground from a height of {h} meters.')
