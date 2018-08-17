import numpy as np

#Numpy Version

#in command line: pip3 install numpy
#print(np.__version__)

#Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.

#py list
l = [2,32,22.2,-7.66]
#np array
#a=np.array(l)
#some statistics
# print("mean ",np.mean(1))
# print("median: ",np.median(l))
# print("min: ",np.min(l))
# print("std: ",np.std(a))

#print(l)

#print(a)
#print(np.mean(l))

#Write a Python program to create a 3x3 matrix with values ranging from 2 to 10.

# a=np.arange(2,11)
# x=a.reshape(3,3)

#print(x)
#arithmetic operation
if True:
    a = np.array([1,3,-2,7],float)
    b = np.array([[2,6,4,2], [1,8,7,2]])
    c = np.array([3,-2,5,7],float)
    d = np.array([[1,2,5,6], [7,2,3,1]])

    print (np.dot(a,c))

