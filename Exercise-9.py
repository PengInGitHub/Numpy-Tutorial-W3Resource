import numpy as np

#Write a Python program to add a border (filled with 0's) around an existing array.

x=np.ones((3,3))
#np.ones((3,3)) instead of np.array((3,3))
x=np.pad(x,pad_width=1,mode='constant',constant_values=0)
print(x)
