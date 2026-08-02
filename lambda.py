#Create a lambda function to square a number.
square=lambda x:x**2
a=int(input("Enter a number to be squared: "))
print(square(a))

# #Create a lambda function to add two numbers.
sum=lambda x,y:x+y
result=sum(3,5)
print(result)

#Create a lambda function to check if a number is even.
even=lambda x:"even" if x%2==0 else "odd"
a=even(3)
print(a)