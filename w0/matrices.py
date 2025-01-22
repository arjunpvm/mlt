import numpy as np

M = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(M)

print(type(M))

# Matrix addition
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A + B)

# Scalar multiplication

print(3 * A)

# Element wise multiplication

print(A * B)

# functions on matrices

# Given a matrix, we sometimes would want to apply a function to every element of the matrix. For example, we may want to take the absolute value of all the elements. Let us say  f  is this function

A = np.array([[-1,2],[-3,-4]])

print(np.abs(A))

# to square each element of a matrix

print(A ** 2)

# Transpose of a matrix

print(np.transpose(M))

# different way

print(M.T)

# Matrix multiplication

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A @ B)

# matrix and vector multiplication

x = np.array([6, 7, 8])

print(M @ x)

# shape of a matrix

# The dimensions of a matrix are determined by the shape attribute

print(M.shape) # which prints (3, 3) three rows and three columns

# Matrix of zeroes

# to initialize a matrix of zeroes

M = np.zeros((2,4))

print(M)

# for matrix of ones

M = np.ones((4,2))

print(M)

# for identity matrix

I = np.eye(3)

print(I)
