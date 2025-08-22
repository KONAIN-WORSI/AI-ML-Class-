import numpy as np

A = np.array([[2,-1],
              [3,4]])

X = np.array([1,2])

Tx = A @ X
print(f'T(x) = {Tx}')

# scaling 
kx , ky = 1.5,0.5
A = np.array([[kx,0],
              [0,ky]])

v = np.array([2,3])
Tx = A @ v
print(Tx)

# matrix rotation
theta = np.pi/2 # 90 degree

A = np.array([[np.cos(-theta), -np.sin(-theta)],
              [np.sin(-theta), np.cos(-theta)]])

v = np.array([3,2])

Rotated_vector = A @ v
print(Rotated_vector)

# reflection matrix of x-axis
A = np.array([[1,0],
              [0,-1]]) # -> for reflection along x-axis

v = np.array([3,4])
reflected_v = A @ v
print(reflected_v)

# reflection matrix of y-axis
A = np.array([[-1,0], # -> for reflection along y-axis
              [0,1]])

v = np.array([3,4])
reflected_v = A @ v
print(reflected_v)

# compostion of linear transformation

A = np.array([[1,3],
              [4,9]])
B = np.array([[4,7],
              [4,10]])

X = np.array([1,2])

Result  = B @ (A @ X)
print(Result)

Result_1 = (B @ A) @ X
print(Result_1)