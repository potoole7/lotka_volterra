# Forward Euler Method
# Args: 
# sol: np.array of solutions, where:
#   sol[:, 0] is the prey population (x), and 
#   sol[:, 1] is the predator population (y)
# N: number of time steps
# T: max time
# a, b: prey parameters, max prey per capita growth rate, effect of presence 
# of predators on the prey growth rate.
# g, d: predator parameters, predator's per capita death rate, and the effect of 
# the presence of prey on the predator's growth rate.
def f_euler(sol, N, T, a, b, g, d):

   dt = T / N # time step

   for i in range(N):
     sol[i+1, 0] = sol[i, 0] + a * sol[i, 0]* dt - b * sol[i, 0] * sol[i, 1] * dt
     sol[i+1, 1] = sol[i, 1] - g * sol[i, 1]* dt + d * sol[i, 0] * sol[i, 1] * dt

   return sol
