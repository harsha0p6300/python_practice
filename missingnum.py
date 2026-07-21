#Given a list containing numbers from 1 to n, where one number is missing, find the missing number
def miss_num(arr):
    n=len(arr)+1

    for i in range(1,n+1):
        if i not in arr:
            return i

user=list(input("ENter the list of number: "))
print(miss_num(user))

