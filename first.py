import numpy as np

print(np.zeros((2,3)))
print(np.ones((3,4)))
print(np.full((3,2), fill_value=7))
print(np.empty((2,4)))
print(np.eye(5, dtype=int))
print(np.arange(0,10,2))
print(np.linspace(0, np.pi, 5))


print(np.random.random((3,4)))        # Elements are uniformly distributed from half-open interval [0.0,1.0)

print(np.random.normal(0, 1, (3,4)))    # Elements are normally distributed with mean 0 and standard deviation 1

print(np.random.randint(-2, 10, (3,4)))  # Elements are uniformly distributed integers from the half-open interval [-2,10)

np.random.seed(7)
print(np.random.randint(0, 100, 10))
print(np.random.normal(0, 1, 10))

new_generator = np.random.RandomState(seed=122)  # RandomState is a class, so we give the seed to its constructor
print(new_generator.randint(0, 100, 10))

a = np.array([1,2,3,4,5])
b = np.array([1,3,2,4,5])

print(np.where(a == b))

o = np.linspace(0, 100, 5)
print(o)

a = np.array([[1,2,3],
              [4,5,6]])
o = np.tile(a, 10)
print(o)

#matrix multiplication
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
o = a@b
print(o)

#matrix transpose
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

a_transpose = a.T

print(a_transpose)

