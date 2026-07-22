4. #Write a Python program to *check whether a number is an Armstrong number*.

def armstrong(num):
    digit=str(num)
    n=len(digit)

    total=0
    for d in digit:
        total+=int(d)**n
    return total==num

user=int(input("Enter a Number: "))
if armstrong(user):
    print(user,"is an Armstrong number")
else:
    print(user,"is not a armstrong number")


#or
def is_armstrong(num):
    temp = num
    n = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10
    return total == num
print(is_armstrong(153))