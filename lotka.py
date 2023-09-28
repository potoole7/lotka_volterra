import numpy as np
import matplotlib.pyplot as plt

# max time
T = 100
# n
N = 100000
# timestep
dt=T/N
# time
t=np.linspace(0,T,N+1)
# ODE parameters
a=1.7
b=0.9
d=0.2
g=0.3

# arrays to store solutions
sol = np.zeros((N+1, 2))

# initial conditions
sol[0,0] = 10
sol[0,1] = 10

# loop using forward euler
for i in range(N):
    sol[i+1,0]=sol[i,0]+a*sol[i,0]*dt - b*sol[i,0]*sol[i,1]*dt
    sol[i+1,1]=sol[i,1]-g*sol[i,1]*dt + d*sol[i,0]*sol[i,1]*dt

fig, ax = plt.subplots(1,2)
ax[0].plot(t, sol[:,0])
ax[0].plot(t, sol[:,1])
ax[1].plot(sol[:,0], sol[:,1])
plt.show()

