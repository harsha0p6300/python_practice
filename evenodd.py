#Write a Python program to count the number of even and odd numbers in a list.
def count_eo(list1):
    even_count=0
    odd_count=0
    for num in list1:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count
    
list1=[1, 2, 3, 4, 5, 6, 7]
evens,odd=count_eo(list1)
print("Even count are",evens)
print("Odd count are",odd)
