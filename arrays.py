import numpy as np

a=np.arange(2)
b=np.arange(2,5)
print(f"a has shape {a.shape}: {a}")
print(f"b has shape {b.shape}: {b}")
print(np.concatenate((a,b)))

c=np.arange(1,5).reshape(2,2)
print(f"c has shape {c.shape}:", c, sep="\n")
print(np.concatenate((c,c)))

print("New row:")
print(np.concatenate((c,a.reshape(1,2))))
print("New column:")
print(np.concatenate((c,a.reshape(2,1)), axis=1))