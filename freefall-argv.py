import sys
import numpy as np


def freefall(h):
    """ Calculates the amount of time in seconds for an object to hit the ground at a given height, h, in meters. """
    if len(sys.argv) > 2:
        print("Error: Function only takes one argument")
    else:
        g = 9.81    # gravitational constant
        # gives time in seconds until the ball hits the ground
        t = np.sqrt((2*h)/g)
        print(
            f'The ball takes {t:.3} seconds to hit the ground from a height of {h} meters.')


h = int(sys.argv[1])
freefall(h)
