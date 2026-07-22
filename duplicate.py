#Write a Python program to print all duplicate elements in a list.
def duplicates(lst):
    found = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in found:
                found.append(lst[i])
    return found

user = list(map(int, input("Enter the numbers: ").split()))
print(duplicates(user))

#or

#Given two lists, print the common elements without duplicates.
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
duplicate=list(set(list1) & set(list2))
print(duplicate)

#or
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]

common=list(set(filter(lambda x:x in list1,list2)))
print(common)