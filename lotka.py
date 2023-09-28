import numpy as np
import matplotlib.pyplot as plt
import timestep_functions as ts

# max time
T = 100
# number of time steps
N = 100000
# timestep
# dt=T/N
# time (for plot)
t=np.linspace(0,T,N+1)
# ODE parameters
a=1.2
b=0.5
d=0.2
g=0.3

# arrays to store solutions
sol = np.zeros((N+1, 2))

# initial conditions
sol[0,0] = 10
sol[0,1] = 10

# Forward Euler solution
sol_fe = ts.f_euler(sol, N, T, a, b, g, d)

plt.plot(t, sol_fe[:,0])
plt.plot(t, sol_fe[:,1])
plt.show()

