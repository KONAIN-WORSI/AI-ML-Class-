import numpy as np
#  S -> V
arr = np.array([1, 2, 3, 4, 5]) # v
s = 5 # s

new_arr = arr * s

# print(arr)
# print(new_arr)

#s -> M
s = 4
mat = np.array([[1, 2, 4],
                 [2, 3, 5],
                 [5, 7, 3]])

new_mat = s - mat # mat - s
# print(mat)
# print(new_mat)
mat = np.array([[2, 4, 7],
               [3, 4, 6],
                 [4, 6, 9]])
v = np.array([1, 2, 3])

# new_mat = mat + v
# print(mat)
# print(new_mat)

# 1D 
M = np.array([1,2,3,46,7,4,3,99])

new_m = np.sort(M)[::-1] # sort in descending order
print(M)
print(new_m)

# matrix sorting
mat = np.array([[3,5,6],
                [6,4,2],
                [9,8,7]])

new_mat = np.sort(mat, axis = 1) # sort each row
new_c = np.sort(mat, axis = 0) # sort each column
print(new_mat)

# row appending
mat = np.array([[1, 2, 3],
                [2, 3, 6]])
new_row1 = np.array([[2, 5 ,7]])

new_row2 = np.array([[2, 100 ,700]])

new_mat1 = np.append(mat, new_row1, axis = 0) # already appended

new_mat2 = np.append(new_mat1, new_row2, axis = 0) # added another row

print(mat)
print()
print(new_mat1)
print()
print(new_mat2)