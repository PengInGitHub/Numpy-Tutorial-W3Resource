import numpy as np
import time

# Convert a list and tuple into arrays
my_list=[1,2,3,4,5]
x=np.asarray(my_list)
print(x)

#defination of tuple
#A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
#Creating a tuple is as simple as putting different comma-separated values.
print(time.localtime())
print(range(10))

my_tuple=([1,1,1],[2,3,3])
print(my_tuple)

#compare list and tuple
#list and tuple are squential data struecture
#list uses [] while tuple uses ()
#tuple could not be modified
#tuple is more structured
