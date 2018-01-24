import numpy as np

#make an array starting at 0 and ending at 11
arr = np.arange(0,11)

#call the element at the index
a = arr[8]
b = arr[1:5]

#set particular elements to a vaule
arr[0:5] = 100

arr = np.arange(0,11)

#slice_arr is not a copy. It is a view of the original array
#all the elements in the array equals 99
slice_arr = arr[:] = 99

#make a copy of the array
arr_copy = arr.copy()

#make a 2-d array
arr_2d = np.array(([5, 10 ,15], [20, 25, 30], [35, 40, 45]))

# check one row
c = arr_2d[1]

# check one value. first is row.
d = arr_2d[1][1]

#row 1 and 2. column 2 and 3
e = arr_2d[:2, 1:]

arr2d_0 = np.zeros((10, 10))

#get the length of the array
arr_length = arr2d_0.shape[1]

#re set the value of the row
for i in range (arr_length):
    arr2d_0[i]=1

#get the value of row 2,4,6 and 8
arr2d_0[[2,4,6,8]]

