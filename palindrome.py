#Write a Python program to check whether a string is a palindrome.
def palindrome(text):
    if text==text[::-1]:
        return "Its is a Palindrome"
    else:
        return "its not a palindrome"
print(palindrome("madam"))

#or

def palindrome(string):
    return "it is palindrome" if string=="".join(reversed(string)) else "its not a palindrome"
user=str(input("Enter a string: "))
print(palindrome(user))