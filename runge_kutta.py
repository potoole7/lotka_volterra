import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t=np.linspace(0,100, 10)
# ODE parameters
a=1.2
b=0.5
d=0.2
g=0.3

# initial conditions
y0 = np.array([10, 10])

#Set of differential equations (L-V)
def lv(t, y, a, b, d, g):
    np.array([
            a*y[0] - b*y[0]*y[1],
            d*y[0]*y[1] - g*y[1]
            ])


#scipy implementation of the solver (runga-kutta scipy solver)
sol = solve_ivp(lambda t, y: lv(t, y, a, b, d, g), t, y0)

z = sol.sol(t)
plt.show(t, z.T)
plt.xlabel('t')
plt.legend(['x', 'y'], shadow=True)
plt.title('Lotka-Volterra System')
plt.show()