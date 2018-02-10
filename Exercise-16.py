import numpy as np

#Find the number of elements of an array, length of one array element in bytes
x=np.array([1,2,3],dtype=np.float64)
print(x.size)
print(x.itemsize)#each float64 has 8 bytes
print(x.nbytes)
