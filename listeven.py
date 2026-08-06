#Given a list of numbers, use a lambda function with filter() to print only the even numbers.
list1=[12, 15, 18, 21, 24, 27]
even=filter(lambda x:x%2,list1)
print(list(even))


#by using the function
def even_list(list2):
    return list(filter(lambda x:x%2,list2))

print(even_list([12, 15, 18, 21, 24, 27]))