import numpy as np

x = np.array([1, 2, 3])

print(x)

print(type(x)) # numpy.ndarray --> which means n dimensional array

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = x + y

print(z)

z = x * y

print(z)

z = 3 * x # each element of x is multiplied my 3

print(z)

z = x ** 2

print(z) # each element of x is squared

x = np.array([1, 10, 100, 1000, 100000])

z = np.log10(x)

print(z) # this will print log base 10 of each element of x

x = np.array([1, 10, 100, 1000, 100000])

z = np.log(x)

print(z) # this will print log base e of each element of x

# dot producy

x = np.array([1, 2, 3, 4])
y = np.array([-4, -5, -6, -7])

z = np.dot(x, y)

print(z)

# Shape of a vector

# all numpy arrays have an attribute called shape. The shape is a tuple.
# for vectors (single dimensional) the shape is of the form (n,)
# where n is the no of components in the vector

x = np.array([1, 2, 3, 4])

print(x.shape)

# for a vector the following relation is always true

print(x.shape[0] == len(x))

# On many occassions, we might want to create a NumPy array all of whose elements are zeros or ones or some other constant. If we want a vector of zeros, one way would be as follow

x = np.array([0 for i in range(4)])

print(x)

# but there is a seperate method for this in numpy

x = np.zeros(4)

print(x)

# for vector of ones

x = np.ones(4)
