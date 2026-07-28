#Create a NumPy array and replace all values greater than 50 with 100.
import numpy as np
arr=np.array([10, 25, 55, 70, 45, 90, 30])

def fun(li):
    for i in range(len(li)):
        if li[i]>50:
            li[i]=100
    return li

print(fun(arr))

#or using NumPy Boolean Indexing (Recommended)

arr=np.array([10, 25, 55, 70, 45, 90, 30])
arr[arr>50]=100
print(arr)
