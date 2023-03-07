# version: 0.1
# author: picklez

from arrays_to_csv import *

array1 = [0, 1, 2, 3, 'zero', 'one', 'two', 'three']
array2 = [ [0, 1, 2, 3], ['zero', 'one', 'two', 'three'] ]
print(array1)
A_1D_to_CSV("array1", array1)
print()
print(array2)
A_2D_to_CSV("array2", array2)