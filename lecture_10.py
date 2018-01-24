import numpy as np

#create the array and reshape it to have 10 rows and 5 columns
arr = np.arange(50).reshape((10,5))

#transpose the array
arr_t = arr.T

#calculate dot product
arr_dot = np.dot(arr_t, arr)

arr2 = np.array([[1,2,3]])
arr2.swapaxes(0,1)
