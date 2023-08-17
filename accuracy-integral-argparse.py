import numpy as np
import time
import argparse

parser = argparse.ArgumentParser(prog='Accuracy and Speed  - Calculating Integrals',
                                 description="Calculates the integral of (1-x**2)**0.5 utilizing the Reimann's definition of an integral and also provides execution time.")
parser.add_argument('N', metavar='N = slices', type=int,
                    help="Enter N number of slices, the larger the value of N the greater the accuracy. N must be an integer > 0. ")
args = parser.parse_args()

N = args.N  # defines N as the input in the terminal


def main(N):
    """"This function utilizes Reimann's definition of an integral to get an approximation of the integral for the function (1-x**2)^0.5. """

    if N <= 0:
        print("Error: N must be > 0")
    else:
        start_time = time.time()
        h = 2/N
        I = 0

        for k in range(N):

            x = -1 + h*k
            y = np.sqrt(1-np.power(x, 2))
            I += h*y

        print(
            f"Execution time:  {time.time() - start_time:0.5f} \nIntegral Approximation:  {I:0.5f}")


main(N)
