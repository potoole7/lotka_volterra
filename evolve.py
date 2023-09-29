import numpy as np

def evolve(phi, f, Df, t, z0, T, N):
    z = np.zeros(N+1)
    h = T / N
    z[0] = z0
    for idx in range(1, N+1):
        z[idx] = phi(f, Df, t + idx*h, z[idx - 1], h)
    return z