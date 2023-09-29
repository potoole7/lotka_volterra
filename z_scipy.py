import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def true_sol(t):
    return np.exp(-1*t)

def rhs(t, z):
    return np.array([-1*z])

T = 10
z0 = np.array([1])

sol = solve_ivp(lambda t,z: rhs(t, z), t_span=[0, T], y0=z0, max_step=0.1)

t = np.linspace(0, T)
sol_true = true_sol(t)

plt.plot(sol.t, sol.y.T)
plt.plot(t, sol_true)
plt.xlabel('t')
plt.legend(['RK45', 'Ground truth'])
plt.savefig('sol_z.png', dpi=300)