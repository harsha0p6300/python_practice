#3. Create a *4×4 NumPy array* and find its *transpose, shape, and size*.
import numpy as np

arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ])

print(arr.transpose())
print(arr.shape)
print(arr.size)
