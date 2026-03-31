import numpy as np 
import scipy.linalg as la

# vector 
v = np.array([1,2,3])
print(v)

# matrix
A = np.array([[1,2],[3,4]])
print(A)

# scalar multiplication
s_scaled = 5 * v
print(s_scaled)

# matrix multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = A @ B
print(C)

# add
a = np.array([[2,3],[4,5]])
b = np.array([[6,7],[8,9]])
add_v = a + b
print(add_v)

# transpose
Y = np.array([[2,3],[4,5]])
transpoe = Y.T
print(transpoe)

# linear equation solve
G = np.array([[2,3],[5,4]])
H = np.array([8,13])
soln = np.linalg.solve(G,H)
print(soln)

# another example of linear algebra
A = np.array([[8,3,-2],[-4,7,5],[3,4,-12]])
b = np.array([9,15,35])
solve = np.linalg.solve(A,b)
print(solve)

#LU decomposition
A = np.array([[2,4,5],
              [1,3,2],
              [4,2,1]])

P,L,U = la.lu(A)
print(P)
print(L)
print(U)

# QR decompostion
A = np.array([[1,2,3],
              [4,5,6]])
Q,R = np.linalg.qr(A)
print(Q)
print(R)