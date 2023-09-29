import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sklearn.metrics import mean_squared_error

def true_sol(t):
    return np.exp(-1*t)

def rhs(t, z):
    return np.array([-1*z])

T = 10
z0 = np.array([1])

steps = [0.2, 0.4, 0.6, 0.8, 1]

for step in steps:
    sol = solve_ivp(lambda t,z: rhs(t, z), t_span=[0, T], y0=z0, max_step=step)
    t = np.linspace(0, T)
    mse = mean_squared_error(true_sol(t), sol.y.T)
    plt.plot(step, mse)
    plt.legend(step)
    plt.xlabel('step')
    plt.ylabel('MSE')


#plt.legend('Ground truth')
plt.savefig('sol_z.png', dpi=300)
plt.show()







"""
for step in steps:
    sol = solve_ivp(lambda t,z: rhs(t, z), t_span=[0, T], y0=z0, max_step=step)
    t = np.linspace(0, T)
    plt.plot(sol.t, sol.y.T)
    label = 'RK-45'
    plt.legend('RK-45',)


sol_true = true_sol(t)

plt.plot(t, sol_true)
plt.xlabel('t')
plt.legend('Ground truth')
plt.savefig('sol_z.png', dpi=300)
"""