import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4, 1000)
t2 = np.linspace(0, 3000, 1000)
N = 1000


def square_wave(t):
    """This function defines a square wave."""

    x = 2*np.floor(t)-np.floor(2*t)+1

    return(x)


def sawtooth_wave(t):
    """This function defines a sawtooth wave."""

    x = 2*(t-np.floor((t+(1/2))))

    return(x)


def mod_sine_wave(t, N):
    """This function defines a modulated sine wave. """

    x = np.sin((np.pi*t)/N)*np.sin((20*np.pi*t)/N)

    return(x)


# plots the graph of square_wave(t)
plt.figure(1)
plt.plot(t, square_wave(t), color="Red")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Square Wave")

# plots the graph of sawtooth_wave(t)
plt.figure(2)
plt.plot(t, sawtooth_wave(t), color="Green")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Sawtooth Wave")

# plots the grapf of mod_sine_wave(t,N)
plt.figure(3)
plt.plot(t2, mod_sine_wave(t2, N), color="Orange")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Modulated Sine Wave")

# performs the real fast fourier transform on square_wave(t) and calculates the square of the coefficients.
square_rfft_coeff = ((np.fft.rfft(square_wave(t))))
square_rfft_real = square_rfft_coeff*np.conjugate(square_rfft_coeff)

# plots the graph of the real fast fourier transform of the square_wave(t) function
plt.figure(4)
plt.plot(square_rfft_real, color="Red")
plt.xlabel("k")
plt.ylabel("FFT Coefficients, ${C_{k}}^{2}$")
plt.title("FFT of Square Wave")

# performs the real fast fourier transform on sawtooth_wave(t) and calculates the square of the coefficients.
saw_rfft_coeff = ((np.fft.rfft(sawtooth_wave(t))))
saw_rfft_real = saw_rfft_coeff*np.conjugate(saw_rfft_coeff)

# plots the graph of the real fast fourier transform of the sawtooth_wave(t) function
plt.figure(5)
plt.plot(saw_rfft_real, color="Green")
plt.xlabel("k")
plt.ylabel("FFT Coefficients, ${C_{k}}^{2}$")
plt.title("FFT of Sawtooth Wave")

# plots the graph of the real fast fourier transform of the square_wave(t) function
mod_sine_rfft_coeff = ((np.fft.rfft(mod_sine_wave(t2, N))))
mod_sine_rfft_real = mod_sine_rfft_coeff*np.conjugate(mod_sine_rfft_coeff)

# plots the graph of the real fast fourier transform of the mod_sine_wave(t,N) function
plt.figure(6)
plt.plot(mod_sine_rfft_real, color="Orange")
plt.xlabel("k")
plt.ylabel("FFT Coefficients, ${C_{k}}^{2}$")
plt.title("FFT of Modulated Sine Wave")

plt.show()
