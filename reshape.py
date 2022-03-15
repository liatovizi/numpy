import numpy as np

a=np.arange(9)
anew=a.reshape(3,3)
print("anew", anew)
print("a", a)

d=np.arange(4)             # 1d array
dr=d.reshape(1,4)          # row vector
dc=d.reshape(4,1)          # column vector
print("d", d)
print("dr", dr)
print("dc", dc)