import numpy as np

def diamond(n):
    a = np.eye(n, dtype=int)
    b = a[::-1]
    bb = b.T[:n-1].T
    c = np.concatenate((bb,a), axis=1)

    d = c[::-1]
    dd = d[1:]
    e = np.concatenate((c,dd))
    return np.array(e)


import numpy as np

def diamond(n):
    a = np.eye(n, dtype=int)
    b = a[::-1]
    bb = b.T[:n-1].T
    c = np.concatenate((bb,a), axis=1)

    d = c[::-1]
    dd = d[1:]
    e = np.concatenate((c,dd))
    return np.array(e)


print(diamond(3))
