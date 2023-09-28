import numpy as np


alpha = 0.5
beta = 0.2
delta = 0.1
gamma = 0.3

X_m = np.array([[1], [-4]]) # initial conditions
dx = alpha*X_m[0] - beta*X_m[0]*X_m[1]
dy = delta * X_m[0] * X_m[1] - gamma * X_m[1]
d = np.array([dx, dy])
X_p =  X_m + 0.01 * d # need to do forward euler to get extra X value

for i in range(10): # now using X_p and X_m for adams bashforth
    dxp = alpha*X_p[0] - beta*X_p[0]*X_p[1]
    dyp = delta * X_p[0] * X_p[1] - gamma * X_p[1]
    dp = np.array([dxp, dyp])
    dxm = alpha*X_m[0] - beta*X_m[0]*X_m[1]
    dym = delta * X_m[0] * X_m[1] - gamma * X_m[1]
    dm = np.array([dxm, dym])
    X_i = X_p
    X_p = X_p + 0.01/2 *(3 * dp - dm)
    X_m = X_i

print(X_p)

