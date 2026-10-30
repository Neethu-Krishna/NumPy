# 1.Create a 1D NumPy array with numbers from 1 to 10.
import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10])
#arr1 = np.arange(1,11)
print(arr)
# 2.Create a NumPy array of zeros of size 5.
zero_size = np.zeros((5) ,dtype=int)
print(zero_size)

# 3.Create a NumPy array of ones of size 4 × 4.
ones_size = np.ones(((4,4)),dtype=int)
print(ones_size)

# 4.Create an array of even numbers from 2 to 20.
even_array = np.arange(2,21,2)
print(even_array)

# 5.Create an array with values from 10 to 50, step 5.
value = np.arange(10,51,5)
print(value)

# 6.Create an array [1, 2, 3] and multiply it by 3.
multiply_array = np.array([1,2,3])
result = multiply_array * 3
print(result)

# 7.Create two arrays and add them element-wise.
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
result = array1 + array2
print(result)

# 8.Create an array [10, 20, 30, 40] and find its mean.
mean_array = np.array([10,20,30,40])
print(np.mean(mean_array))

# 9.Create an array [4, 9, 16, 25] and find the square root.
sqrt_array = np.array(([4,9,16,25]),dtype=int)
print(np.sqrt(sqrt_array))

# 10.Create a random array of size 5 and find its sum.
rand_array = np.random.rand(5)
print(rand_array)
print(np.sum(rand_array))

# 11.Slice the first 5 elements from an array of numbers from 1 to 10.
elements = np.arange(1,11)
print(elements)
print(elements[:5])

# 12.Get the last two elements of [10, 20, 30, 40, 50].
elements = np.array([10,20,30,40,50])
print(elements[-2:])

# 13.Change the 3rd element of [1, 2, 3, 4, 5] to 99.
element = np.array([1,2,3,4,5])
element[2] = 99
print(element)

# 14.Create a 3×3 matrix and access the element in the 2nd row, 3rd column.
matrix = np.array([
         [1,2,3],
         [4,5,6],
         [7,8,9]
    ])
print(matrix[1,2])
# 15.Create a 1D array and reverse it using slicing.
array_1d = np.array([1,2,3,4,5])
print(array_1d[::-1])

# 16.Generate a random integer between 1 and 100.
random_int = np.random.randint(1,101)
print(random_int)

# 17.Generate a random array of size 3 × 3.
random_array = np.random.rand(3,3)
print(rand_array)

# 18.Generate 5 random numbers from a normal distribution.
random_number = np.random.randn(5)
print(random_number)

# 19.Generate 10 random numbers between 0 and 1.
random_number = np.random.rand(10)
print(random_number)

# 20.Shuffle an array [1, 2, 3, 4, 5] randomly.
array_shuffle = np.array([1,2,3,4,5])
np.random.shuffle(array_shuffle)
print(array_shuffle)

# 21.Transpose a 2×3 matrix.

# 22.Reshape a 1D array (1 to 12) into 3×4.
# 23.Resize a 1D array of size 5 into 3×3 (showing how elements repeat or using zero padding).
# 24.Convert a 2D array into 1D.