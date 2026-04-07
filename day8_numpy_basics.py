# Day 8 - NumPy Practice
# Raj Gajare | Prime 2.0

import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr2=np.array([10,20,30,40,50,60])

print("array operation:")
print(arr1)
print(arr2)
print("zeros:",np.zeros(5))
print("Ones:",np.ones(5))
print("Range:",np.arange(0,10,2))
print("linespace:",np.linspace(0,1,5))

# print 2-array operation
print("operations:")
print("add:",arr1+arr2)
print("multiply:",arr1*arr2)
print("Square:", arr1 ** 2)
print("Sqrt:", np.sqrt(arr2))

# part-3 indexing & slicing
print("indexing")
print("first element:",arr1[0])
print("last element:",arr1[-1])
print("slice [1:4]:", arr1[1:4])
print("Reverse:", arr1[::-1])

mat=np.array([[1,2,3],
              [4,5,6],
              [6,7,8]])

print("matrix:")
print("shape:",mat.shape)
print("Reshape to 1x9:", mat.reshape(1, 9))
print("Transpose:\n", mat.T)

#  Part 5 - Built-in Functions
print("\n=== Statistics ===")
data = np.array([85, 92, 78, 95, 88, 76, 90])
print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Std Dev:", np.std(data))
print("Median:", np.median(data))