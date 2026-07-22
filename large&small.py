#Write a Python program to find the largest and smallest number in a list.
list1=[12, 45, 7, 89, 23, 56]
large=max(list1),min(list1)
print(large)

#using sorting method

list1=[12, 45, 7, 89, 23, 56]
sorted_list1=sorted(list1)
print("Smallest",sorted_list1[0])
print("Largest",sorted_list1[-1])