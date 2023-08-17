import numpy as np 
import matplotlib.pyplot as plt 
from scipy import constants
from numpy.fft import rfft,irfft

hbar = constants.hbar
L = 10.0e-8
N = 1000

#dimension of the box
grid  = np.linspace(0,L,N)

def Psi(x):
    
    """This function defines Psi(x,0)."""
    
    x_0 = L/2
    sigma = 1.0e-10
    k = 5.0e+10
    
    return np.exp((-(x-x_0)**2)/2*(sigma**(2)))*np.exp(1j*k*x)
  
#creates an array of the complex type to hold the values of Psi(x)
# then sets x = 0 and x = N equal to zero      
psi = np.zeros(N,complex)
psi[:] = Psi(grid)
psi[0] = 0
psi[N-1] = 0

#holds the real and imaginary part of Psi(x)
real = np.real(psi)
imaginary = np.imag(psi)

def dst(y):
    
    """This function performs a Type - 1 discrete sine transform on real data y."""
    
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -np.imag(rfft(y2))[:N]
    a[0] = 0.0

    return a

#holds the coefficients alpha and eta
alpha = dst(real)
eta = dst(imaginary)

def RPsi(k,n,t):
    """ This function defines the real part of the time dependent wave function."""
    m = 9.109e-31
    
    return (alpha[k]*np.cos(((np.pi**(2)*hbar*k**(2)) / (2*m*L**(2)))*t) 
            - eta[k]*np.sin(((np.pi**(2)*hbar*k**(2))/(2*m*L**(2)))*t))*np.sin((np.pi*k*n)/N)
    
RPsi_vals = []

t = 1.0e-16
k = np.arange(1,N)

#Real part of the wave function is a sum from k =1 to N, normalized by 1/N at x_n
# the loop below takes the sum of k = 1 to N for at every n = i from 0 to N
for i in range(N):
    RPsi_vals.append(1/N*np.sum(RPsi(k,i,t)))

Real_Psi = np.array(RPsi_vals)

def idst(a):
    
    """ This function peforms a Type 1 inverse DST of a"""
    
    N = len(a)
    c = np.empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0

    return y

idst_Real_Psi = idst(Real_Psi)
plt.plot(grid, idst_Real_Psi)