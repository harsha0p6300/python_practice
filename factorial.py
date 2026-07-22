def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
user=int(input("Enter a Number to calculate the factorial: "))
print("The factorial is",factorial(user))


#or
def facto(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
num = int(input("Enter a number: "))
print(facto(num))
