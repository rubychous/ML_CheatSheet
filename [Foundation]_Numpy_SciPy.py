# Numpy, SciPy Foundation

import numpy as np
import scipy

# 1-d array is just like a list
array1d=np.array([1,3,5,7,9])
print(array1d)
type(array1d)

# 2-d array is like a 2-d grid
array2d=np.array([[1,2,3],[4,5,6]])
print(array2d)
type(array2d)

# show how many rows and columns
array2d.shape

# extract the value in 2-d array
array2d[1,2]
array2d[1,:-1]

new2dArray=np.array([[1,2,4,5,9],[3,4,6,6,10],[15,3,2,14,7]])
# extract elements with indices [1,2], [0,4], [2,3]
newSubArray=new2dArray[[1,0,2],[2,4,3]]

# extract values to meet the condition
new2dArray[new2dArray>10]

# return boolean value
new2dArray>10

# create some standard arrays by using built-in function
# create an array of all zeros
arrayOfZero=np.zeros((2,2),dtype="int64")

# create an array of ones
# the default value is float
arrayOfOnes=np.ones((3,3))

# create an array with same values
arraywithConstantValue=np.full(new2dArray.shape,7)

# create an identity matrix with 2 rows and columns
identityMatrix=np.eye(2)

# create array with random numbers
arrayOfRandomNumbers=np.random.random((2,2)) 

# transpose an array
transposeArray=np.transpose(new2dArray)

# reshape the array but remain the same value
reshapeArray=np,reshape(new2dArray,[1,15])

# use maths operation
array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[7,8,9],[3,2,1]])

array1+array2

# +,-,/,* are equivalent to add, subtract, divide,multiply
np.subtract(array1,array2)

# broadcasting
# add array3 to each row of array1
array3=[[1,4,7]]  # it can also be np.array([1,4,7])
array1+array3

# perform inner product in array
np.dot(array1,array2.T) # T is shorthand using np.transpose()

# applying sum function
# axis=0 indicates rows
# axis=1 indicates columns
np.sum(array1,axis=0)
np.sum(array1,axis=1)

# apply stack function
np.vstack((array1,array2))
np.hstack((array1,array2))

# the following section is about scipy package
# the spatial module can find the distance between the given 2 points
# the distance metric can be any one of a number of options
# such as euclidean, cosine, correlation, hamming and so on
# pdist will compute pairwise distances between the rows in a numpy array
from scipy.spatial.distance import correlation, cosine, pdist, squareform

array1=np.array([0,1,0])
array2=np.array([1,0,0])

correlation(array1,array2)

allPoints=np.vstack([array1,array2])
d=squareform(pdist(allPoints, 'euclidean'))
