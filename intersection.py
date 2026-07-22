# Write a Python program to *find the intersection (common elements)* of two lists.
def intersection(list1,list2):
    common=[]
    for num in list1:
        if num in list2:
            common.append(num)
    return common
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(intersection(list1,list2))