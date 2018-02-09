import numpy as np

#Create a 8x8 matrix and fill it with a checkerboard pattern
x=np.zeros((8,8),dtype=int)
x[1::2,::2]=1
x[::2,1::2]=1
print(x)
