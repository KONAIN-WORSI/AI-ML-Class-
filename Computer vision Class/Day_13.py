import numpy as np 

# # array reshaping 
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# re_arr = arr.reshape(5,-1)
# print(arr)
# print(re_arr)

# # array iteration in 1D array

# arr_1d = np.array([10, 20, 30, 40, 50])

# for num in arr_1d:
#     print(num , end=' ')

# array iteration in 2D array
# arr_2d = np.array([[1,2,3,],[4,5,6]])

# for num in arr_2d:  # -> this will iterate over rows
#     print(num)

# for num in np.nditer(arr_2d): # -> this will iterate over all elements
#     print(num)


# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])

# add = a + b
# sub = a - b
# pro = a * b
# div = a / b
# exp = b ** 5
# re = b % a

# # element-wise operations
# print('addition:',add)
# print('subtraction:',sub)
# print('multiplication:',pro)
# print('division:',div)
# print('exponentiation:',exp)
# print('remainder:',re)

# using universal functions
# arr = np.arange(1,11)

# sqrt = np.sqrt(arr)
# n_log = np.log(arr)
# ten_log = np.log10(arr)
# exp = np.exp(arr)
# s = np.sin(arr)
# c = np.cos(arr)
# t = np.tan(arr)

# print('square root:',sqrt)
# print('Natural logarithm:',n_log)
# print('Base 10 logarithm:',ten_log)
# print('exponential:',exp)
# print('sine:',s)
# print('cosine:',c)
# print('tangent:',t)
# 
#
# data = np.array([10,20,30,40,50])


# me = np.mean(data)
# md = np.median(data)
# var = np.var(data)
# std = np.std(data)
# min =  np.min(data)
# max = np.max(data)

# print('Mean:',me)
# print('Median:',md)
# print('Varinence:',var)
# print('Standard Deviation:',std)
# print('Minimum:',min)
# print('Maximum:',max)
# print(np.argmin(data))
# print(np.argmax(data))

# A = np.array([[100,2],[99,2]])
# B = np.array([[200,6],[7,50]])

# dit1 = np.linalg.det(A)
# dit2 = np.linalg.det(B)

# inv1 = np.linalg.inv(A)
# inv2 = np.linalg.inv(B)

# print(dit1)
# print(dit2)
# print(inv1)
# print(inv2)

A = np.array([10,30,40,50,60,70,80])
sum = np.sum(A)
sum_cum = np.cumsum(A)

print(sum)
print(sum_cum)
