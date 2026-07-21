#3) Write a Python program to print all prime numbers between 1 and 100.


for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)


#or

for num in range(2,101):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
