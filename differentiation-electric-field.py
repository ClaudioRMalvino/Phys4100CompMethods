import numpy as np
import matplotlib.pyplot as plt


def electric_potential(x2, y2):
    """This function calculates the electric potential at a point (x,y) giving a distance r away from the two charges."""

    k = 9.0E+09
    r_1 = np.sqrt((x2 - 45)**2 + (y2 - 50)**2)
    r_2 = np.sqrt((x2-55)**2+(y2-50)**2)
    q_1 = 1
    q_2 = -1
    return (k* ((q_1 / r_1) + (q_2 / r_2)))
    
def electric_field(x, y, h):
    """Calculates the electric field by taking the gradient of the electric potential by method of the central difference approximations."""

    Ex = (electric_potential(x+(h/2), y) - electric_potential(x-(h/2), y))/h
    Ey = (electric_potential(x, y+(h/2)) - electric_potential(x, y-(h/2)))/h
    return -Ex, -Ey

def plot_elec_potential(grid):
    """Function plots the electric potential (edge on), density of electric potential, and the electric field lines
    """

    fig, ax = plt.subplots()
    # Plot 1: Electric Potential (edge on)
    plt.figure(1)
    ax.plot(grid)
    ax.set(xticks=np.arange(0, 110, 10),
        title="Electric Potential of the Plane (edge on)",
        xlabel="Distance along x direction, cm", 
        ylabel="Electric Potential, V")

    # Plot 2: Density of Electric Potential
    plt.figure(2)
    plt.pcolormesh(grid.T, alpha=0.7)
    plt.colorbar()
    plt.title("Density of Electric Potential Across the Plane")
    x, y = np.meshgrid(np.arange(1, 101, 1), np.arange(1, 101, 1))
    h = 0.1

    # Plot 3: Electric Field
    plt.figure(3)
    plt.streamplot(x, y,  electric_field(x,y,h)[0],
                electric_field(x, y, h)[1], density=2)
    plt.title("Electric Field between $+q_1$ and $-q_2$")
    plt.show()


# vectorizes the potential in order to utilize it in the loop
vect_potential = np.vectorize(electric_potential)

grid = np.zeros((100, 100))  # creates 2D plane that is 100 x 100

x2 = np.arange(1, 101, 1)
y2 = np.arange(1, 101, 1)

for i in range(0, len(x2)-1):
    for j in range(0, len(y2)-1):
        grid[i, j] = vect_potential(i, j)
        
plot_elec_potential(grid)
