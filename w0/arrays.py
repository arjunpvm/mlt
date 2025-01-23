# Arrays

import numpy as np
# NumPy arrays have an attribute called ndim that gives the number of dimensions of the array

x = np.array([1, 2, 3])
M = np.array([[1, 2, 3], [4, 5, 6]])

print("shape of x", x.shape)
print("shape of M", M.shape)

print("dimension of x", x.ndim)
print("dimension of M", M.ndim)

# we can go higher than than two dimensions

M = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]], 
               [[13, 14, 15, 16],
               [17, 18, 19, 20],
               [21, 22, 23, 24]]
              ])

print(M.shape)
print(M.ndim)
print(M)

# reshaping

# Arrays can be reshaped

A = np.array([[1,2,3],[4,5,6]])
print(A.reshape(6))

A = np.array([1, 2, 3, 4, 5, 6])

print(A.reshape(2,3))

A = np.array([[1,2,3],[4,5,6]])
print(A.reshape(3, -1)) # -1 is for unknown dimension whch lets numpy decide it

# matrix addition

M = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([1, 1, 1, 1])
print('Shape of M:', M.shape)
print('Shape of b:', b.shape)

print(M + b)
