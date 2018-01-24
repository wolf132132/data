import numpy as np

#make a list
my_list1 = [1, 2, 3 ,4]
#make this list as an array
my_array1 = np.array(my_list1)

#make a 2*2 array
my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)

#inidicate the type of the array
print (my_array2.dtype)

#make an array fileld up with zeros (floating type. 5 elements)
zero_array = np.zeros(5)
aero_array2 = np.empty(5)

#make an array fileld up with 1
ones_array = np.ones(5)

#make an identity array
np.eye(5)

#5 means start element. 50 means end element. 2 means increment size
list3 = np.arange(5)
list4 = np.arange(5, 50, 2)

