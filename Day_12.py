import numpy as np

# # creating 3D array 
arr_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(arr_3)

# # 3 x 3 matrix with all elements zero
arr_z = np.zeros((3,3))
print(arr_z)

# # 3 x 3 matrix with all elements one
arr_o = np.ones((3,3))
print(arr_o)

# # create a identity matrix of 5 x 5
iden_mat = np.eye(6)
print(iden_mat)

# # create a array containing 50 numbers from 1
arr = np.arange(1,51)
print(arr)

# # creating a array containiing even numbers from 0 to 100
arr_even = np.arange(0 ,101,2)
print(arr_even)

# # creating a array having 5 value from 1 to 10 with evenly spaced intervals
arr_s = np.linspace(1,10,5)
print(arr_s)

# # creating a array of random numbers between 0 to 1
arr_random = np.random.rand(4,4)
print(arr_random)

# # random values in a array
random_arr = np.random.randint(1,11, size = (4,4))
print(random_arr) 

# having look at the shape , size , dimension ,datatype , itemsize and bytes of the array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print('shape of array:', arr.shape)
print('size of array:', arr.size)
print('Dimension of array:', arr.ndim)
print('Datatype of array:', arr.dtype)
print('Itemsize of array:', arr.itemsize)
print('Total bytes of array:', arr.nbytes)

# # slicing  the array
arr1 = np.array([10, 20 , 30 ,40 ,50])
print(arr1[0]) # indexing first element
print(arr1[-1]) # indexing last element
print(arr1[1:4]) # slicing from index 1 to 3
print(arr1[::2]) # slicing with step 2
print(arr1[::-1]) # reversing the array

# slicing 2D array
arr2 = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(arr2)

print(arr2[2,1])
print(arr2[::2,1])
print(arr2[0,::2])
print(arr2[:,2])
print(arr2[:,0:2])

print(arr2.diagonal())
anti_diag = np.fliplr(arr2).diagonal()
print(anti_diag)