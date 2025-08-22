import numpy as np
from sklearn.decomposition import PCA

# A = np.array([1,2,3,4,5,5,6,])
# norm = np.linalg.norm(A)
# print(norm)

# v1 = np.array([1,2,3])
# v2 = np.array([4,5,6])

# is_orhto = (np.dot(v1, v2) == 0)
# print(is_orhto)

# proj = (np.dot(v1, v2) / np.dot(v2, v2)) * v2
# print(proj)

# M = np.array([[1,2], [3,4], [5,6]])
# c1 , c2 = 1.5 , 2.5

# l_c = c1 * M[0] + c2 * M[1]
# print(l_c)

# v1 = np.array([1,2,3])
# v2 = np.array([2,4,6])

# M = np.stack([v1, v2], axis=1)

# r = np.linalg.matrix_rank(M)

# is_independent = (r == M.shape[1])

# if is_independent:
#     print('The vectors are linearly independent.')
# else:
#     print('The vevtors are linearly dependent.')


x = np.random.rand(4,3)

p = PCA(n_components = 2)
reduce = p.fit_transform(x)

print(x)
print()
print(reduce)


