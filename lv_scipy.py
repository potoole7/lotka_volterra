import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ODE parameters
a=1.2
b=0.5
d=0.2
g=0.3

t_span = [0, 100]
y0 = np.array([10, 10])

def lv_rhs(t, sol, a, b, d, g):
    return np.array([
        a*sol[0] - b*sol[0]*sol[1],
        d*sol[0]*sol[1] - g*sol[1]
    ])

sol = solve_ivp(lambda t,y: lv_rhs(t, y, a, b, d, g), t_span, y0)

plt.plot(sol.t, sol.y.T)
plt.xlabel('t')
plt.legend(['x', 'y'])
plt.savefig('sol.png', dpi=300)
