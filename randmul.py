import numpy as np 


a = np.random.randint(20,size=(3,3))
b = np.random.randint(20,size=(3,3))

print(a)
print(b)

a1 = np.array(a)
b1 = np.array(b)

print(a1.dot(b1))