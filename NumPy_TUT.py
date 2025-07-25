import numpy as np

#------------------------ Creat Arrays ------------------------
arr_1_d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_2_d = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])
arr_3_d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

#------------------------ Higher dimensiion Arrays ------------------------
arr_Higher = np.array([1, 2, 3, 4], ndmin=5)  

#------------------------ Check Dimension ------------------------
print(f"the number of Dimensions for 1-D: {arr_1_d.ndim}") 
print(f"the number of Dimensions for 2-D: {arr_2_d.ndim}") 
print(f"the number of Dimensions for 3-D: {arr_3_d.ndim}") 

#------------------------ Array Indexing ------------------------
print(arr_1_d[0])
print(arr_2_d[1, 1])
print(arr_3_d[1, 1, 0])

#------------------------ Scaling ------------------------
print(arr_1_d[1:4])
print(arr_1_d[1:9:2])
print(arr_1_d[::2])

print(arr_2_d[1, 0:4:2])

print(arr_3_d[0, 1, 0:3:2])

#------------------------ Data Types -----------------------
arr_str = np.array(["Chess", "Game", "Python"])
print(arr_str.dtype)

#------------------------ Specifying data type -----------------------
arr_s = np.array([1, 2, 3, 4], dtype= "S")
print(arr_s.dtype)

#------------------------ Converting data type -----------------------
arr_I = arr_s.astype("i")
print(arr_I)
print(arr_I.dtype)

#------------------------ Copy vs view  -----------------------
a = arr_1_d.copy() 
b = arr_1_d.view()

#------------------------ Check ownership -----------------------
print(a.base)
print(b.base)

#------------------------ Shape -----------------------
print(arr_1_d.shape)
print(arr_2_d.shape)
print(arr_3_d.shape)
print(arr_Higher.shape)

#------------------------ Reshape -----------------------
reshaped1 = arr_1_d.reshape(4,3)
print(reshaped1)
reshaped2 = arr_1_d.reshape(2, 3, 2)
print(reshaped2)
 
#------------------------ Filtering -----------------------
Filter = arr_3_d.reshape(-1)
print(Filter)

#------------------------ Array Iterating -----------------------

#1-D
for x in arr_1_d:
  print(x)

#2-d
for x in arr_2_d:
  for y in x:
    print(y)

#3-D
for x in arr_3_d:
  for y in x:
    for z in y:
      print(z)

#------------------------ Iterating Arrays Using nditer() -----------------------
for x in np.nditer(arr_3_d):
  print(x)

#------------------------ Using ndenumerate() -----------------------

#1-D
for idx, x in np.ndenumerate(arr_1_d):
  print(idx, x)

#2-D
for idx, x in np.ndenumerate(arr_2_d):
  print(idx, x)

#------------------------ Joining Arrays -----------------------
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

joined = np.concatenate((arr1,arr2))
print(joined)

#Stacking
arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])

stacked1 = np.stack((arr3, arr4), axis=1)
print(stacked1)

#hstack / vstack / dstack

print(np.hstack((arr3,arr4)))
print(np.vstack((arr3,arr4)))
print(np.dstack((arr3,arr4)))

#------------------------ Siplitting Arrays -----------------------
split_array1d = np.array_split(arr_1_d, 4)
print(split_array1d)

#2-D
split_array2d = np.array_split(arr_2_d, 4)
print(split_array2d)

#------------------------ Searching Arrays -----------------------
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
y = np.searchsorted(arr, 3, side='right')

#------------------------ sorting Array -----------------------
print(np.sort(arr))

#------------------------ Filtering arrays -----------------------
x = arr > 2
newarr = arr[x]

print(newarr)
print(x)










