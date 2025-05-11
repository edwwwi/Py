import numpy as np

r = int(input("enter row no"))
c = int(input("enter row no"))
matrix1 = []
for i in range(r):
    row = list(map(int,input("enter mat1 ").split()))
    matrix1.append(row)
matrix2 = []  
for i in range (r):
    row = list(map(int,input("enter mat1 ").split()))
    matrix2.append(row)

mat1 = np.array(matrix1)
mat2 = np.array(matrix2)

print(np.matmul(mat1,mat2))
print(mat1.T)
print(mat2.T)