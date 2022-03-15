import numpy as np

def info(name, a):
    print(f"{name} has dim {a.ndim}, shape {a.shape}, size {a.size}, and dtype {a.dtype}:")
    print(a)

b=np.array([[1,2,3], [4,5,6]])
info("b", b)

c=np.array([b, b])
info("c", c)

d=np.array([[1,2,3,4]])
info("d", d)

