import numpy as np
import scipy.linalg as la

# matrix rank in R^3
v1 = np.array([1,0,0])
v2 = np.array([0,1,0])
v3 = np.array([0,0,1])

A = np.column_stack((v1 , v2 ,v3))

Rank = np.linalg.matrix_rank(A)

print(Rank)

# matrix rank in R^2
v1 = np.array([1,2])
v2 = np.array([2,4])

A = np.column_stack((v1 ,v2))

Rank1 = np.linalg.matrix_rank(A)
print(Rank1)

# matrix in R^3
v1 = np.array([1,2,3])
v2 = np.array([2,4,6])
v3 = np.array([9,8,10])

A = np.column_stack((v1 , v2 ,v3))

Rank2 = np.linalg.matrix_rank(A)

print(Rank2)