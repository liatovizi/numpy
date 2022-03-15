import numpy as np

b=np.array([[1,2,3], [4,5,6]])
print(b)
print(b[1,2])    # row index 1, column index 2
print(b[0,-1])   # row index 0, column index -1

b[0,0] = 10
print(b)
print(b[0])    # First row
print(b[1])    # Second row

#slicing
a=np.array([1,4,2,7,9,5])
print(a)
print(a[1:3])
print(a[::-1])

print(b)
print(b[:,0])
print(b[0,:])
print(b[:,1:])

b[:,1:] = 7
print(b)
