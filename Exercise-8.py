import numpy as np

#Write a Python program to create a 2d array with 1 on the border and 0 inside.

x=np.ones((5,5))
x[1:-1,1:-1]=0
print(x)
