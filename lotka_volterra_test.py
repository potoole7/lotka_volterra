import numpy as np

def lv(t,x, y, alpha, beta, delta, gamma):
    return np.array([
                     alpha*x - beta*x*y,
                     delta*x*y - gamma*y
                    ])

alpha, beta, delta, gamma = 0.1, 0.2, 0.3, 0.4
x0 = 1
y0 = 1
t_span = [0, 5]