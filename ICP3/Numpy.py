# import libraries

import numpy as np
# add 15 random numbers to the array using np.random.randint() function
array = np.random.randint(1, 21, size=15, dtype='I')

# to print original array
print("Original array:")
print(array)
# after replacing the maximum value by zero
a = array.reshape(3,5)

print("Updated Array:")
print(a)

# after replacing the maximum value by zero
array[array.argmax()] = 0

print("Updated Array:")
print(array)