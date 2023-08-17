import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import random

N = 1250  # number of iterations per frame, total iterations = N*frames

step = 1  # size of step in the x,y direction

# constructs the figure where the particle will reside and the patch for the particle itself
fig = plt.figure(figsize=(5, 5))
ax = plt.axes(xlim=(0, 101), ylim=(0, 101))
title = ax.set_title("Brownian Motion")
particle = plt.Circle((50, 50), 0.75, fc='r')

# hold the value for the x and y points of the particle
p_x, p_y = [], []


def init():
    """This function describes the initial condition of the particle in the animation."""

    particle.center = (50, 50)
    ax.add_patch(particle)
    return particle,


def brownian_motion(i):
    """ This function holds the algorithm for brownian motion that will be iterated N times 
        at every frame of the animation. """

    dx, dy = 0, 0  # defines the step in the x and y direction
    x_i, y_i = 50, 50  # initial position of the particle (50,50)

    for i in range(N):

        # random number generator for values [1,5).
        p = np.random.randint(1, 5)

        # randomly determines the movement in the x direction and sets boundaries
        if p == 1:
            if x_i <= 0:
                dx = 5*step
            else:
                dx = -step
        elif p == 2:
            if x_i >= 101:
                dx = -5*step
            else:
                dx = step

        # randomly determines the movement in the y direction and sets boundaries
        elif p == 3:
            if y_i <= 0:
                dy = 5*step
            else:
                dy = -step
        elif p == 4:
            if y_i >= 101:
                dy = -5*step
            else:
                dy = step

        # holds adds the new value of dx,dy, into x_i,y_i
        x_i += dx
        y_i += dy
        p_x.append(x_i)
        p_y.append(y_i)

        # gives the new position of the particle
        particle.center = (x_i, y_i)
    return particle,


# function that runs the animation and saves the animation as an mp4.
anim = animation.FuncAnimation(
    fig, func=brownian_motion, init_func=init, frames=800, interval=250, blit=True)
anim.save('brownian_motion_malvino.mp4')
