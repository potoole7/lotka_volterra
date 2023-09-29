def fwd_euler(f, Df, t, z, h):
    return z + h*f(t, z)