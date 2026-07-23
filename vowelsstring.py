#Replace all vowels in a string with *.
def vowels(text):
    vowel="AEIOUaeiou"
    star=[]
    for char in text:
        if char in vowel:
            star.append("*")
        else:
            star.append(char)
    return "".join(star)

user=input("Enter a string: ")
print(vowels(user))

