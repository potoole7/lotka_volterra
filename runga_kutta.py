import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# max time
T = 100
# n
N = 100000
# timestep
dt=T/N
# time
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
s = 10


#Set of differential equations (L-V)
def lv(t,x, y, alpha, beta, delta, gamma):
    return np.array([
                     alpha*x - beta*x*y,
                     delta*x*y - gamma*y
                    ])

#scipy implementation of the solver (runga-kutta scipy solver)
LV_sol = solve_ivp(lambda t, : lv(t, sol[0,0], sol[0,1], a, b, d, g), t, sol)

plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.show()

