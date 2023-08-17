import argparse
import numpy as np

parser = argparse.ArgumentParser(prog='Free Fall',
                                 description="Calculates the amount of time in seconds for an object to hit the ground at a given height, H, in meters.")
parser.add_argument('h', metavar='height', type=float,
                    help="Enter the height in meters")
args = parser.parse_args()

h = args.h


def freefall(h):
    """ Calculates the amount of time in seconds for an object to hit the ground at a given height, h, in meters. """
    if h <= 0:
        print("Error: input a height > 0")
    else:
        g = 9.81    # gravitational constant
        # gives time in seconds until the ball hits the ground
        t = np.sqrt((2*h)/g)
        print(
            f'The ball takes {t:.3} seconds to hit the ground from a height of {h} meters.')


freefall(h)
