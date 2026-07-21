# Given a list of numbers, create a new list containing only the even numbers using list comprehension.

n=[10, 15, 20, 25, 30, 35]
even_num=[num for num in n if num%2==0]
print(even_num)


#or
def even_num(user):
    for num in user:
        if num % 2 == 0:
            print(num)
user = list(map(int, input("Enter a list of numbers: ").split()))
even_num(user)


#or
def ev_num(user):
    even=[]

    for num in user:
        if num%2==0:
            even.append(num)
    return even
user=list(map(int,input("Enter a list of numbers: ").split()))
print(ev_num(user))