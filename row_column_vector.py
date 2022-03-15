
import numpy as np

def get_row_vectors(a):
    to_add = []
    shape = a.shape
    new_dim = shape[1]
    for row in a:
        to_add.append(np.array(row.reshape(1, new_dim)))
    return to_add

def get_column_vectors(a):
    to_add = []
    b = a.T
    shape = b.shape
    new_dim = shape[1]
    for row in b:
        to_add.append(np.array(row.reshape(new_dim, 1)))

    return to_add

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

a = np.array([[5, 0, 3],
  [3 ,7 ,9]])
print(get_row_vectors(a))
print(get_column_vectors(a))

