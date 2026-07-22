# Write a Python program to *count the number of uppercase and lowercase characters* in a string.
def word_case(text):
    upper=0
    lower=0
    for char in text:
        if char==char.upper() and char.isalpha():
            upper+=1
        elif char==char.lower():
            lower+=1
    return upper,lower

user=str(input("Enter a string: "))
upper,lower=word_case(user)
print("Uppercase",upper)
print("Lowercase",lower)