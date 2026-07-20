#count the number of vowels in the string

def count_vow(text):
    vowels="AEIOUaeiou"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count
user=str(input("Enter a String: "))
print(count_vow(user))

