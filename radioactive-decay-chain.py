import numpy as np
import matplotlib.pyplot as plt

# number of atoms at t = 0
N_Bi213 = 10000
N_Pb209 = 0
N_Ti209 = 0
N_Bi209 = 0

# range of time in seconds with step size dt in seconds
dt = 1.0
tmax = 20000
total_time = np.arange(0.0, tmax, dt)

# half life of each element
tau_Bi213 = 46 * 60
tau_Pb209 = 3.3*60
tau_Ti209 = 2.2*60

# probability of decay for each element
p_Bi213 = 1 - 2**(-dt/tau_Bi213)
p_Pb209 = 1 - 2**(-dt/tau_Pb209)
p_Ti209 = 1 - 2**(-dt/tau_Ti209)

# arrays that indexes the amount of atoms for each element at each second 
Bi213_atoms = []
Pb209_atoms = []
Ti209_atoms = []
Bi209_atoms = []

# the algorithm below simulates the decay of Bi 213 to Bi 209

for t in total_time:
    
    #add the new value of the number of atoms for each element after each iteration
    
    Bi213_atoms.append(N_Bi213)
    Pb209_atoms.append(N_Pb209)
    Ti209_atoms.append(N_Ti209)
    Bi209_atoms.append(N_Bi209)
    
    # simulates random decay for Pb 209 into Bi 209
    for i in range(N_Pb209):
        if  np.random.rand() < p_Pb209:
            N_Pb209 -= 1
            N_Bi209 += 1
    
    # simulates random decay for Ti 209 into Pb 209
    for i in range(N_Ti209):
        if  np.random.rand() < p_Ti209:
            N_Ti209 -= 1
            N_Pb209 += 1
    
    # simulates random decay for Bi 213 and then simulates the probability of decaying into Pb 209 or Ti 209
    for i in range(N_Bi213):
        if  np.random.rand() < p_Bi213:
            N_Bi213 -= 1
            if np.random.rand() < 0.9791:
                N_Pb209 += 1
            else: 
                N_Ti209  += 1


# plots the graph of the number of atoms per element vs time
 
plt.plot(total_time, Pb209_atoms, label = "Pb 209")
plt.plot(total_time,Ti209_atoms, label = "Ti 209")
plt.plot(total_time,Bi209_atoms, label = "Bi 209")
plt.plot(total_time, Bi213_atoms, label = "Bi 213")
plt.title("Decay Chain of Bi 213")
plt.xlabel("Time, [s]")
plt.ylabel("Number of Atoms")
plt.legend( )
plt.show()