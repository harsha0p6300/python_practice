#Find the second largest number of a given list
l1=[2,4,6,8,10]
n=sorted(l1)[-2]
print(n)

#Write a program to remove duplicate elements from a list without maintaining the original order
l2=[3,4,2,6,9,8,9,4,2]
unique_num=(list(set(l2)))
print(unique_num)

#or

numbers=[10,20,10,30,70,30,40]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)