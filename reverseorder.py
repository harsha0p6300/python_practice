#1. Reverse the order of words in a sentence.

user=input("Enter something: ")

word=user.split()
print(" ".join(word[::-1]))

# #or
sentence = input("Enter a sentence: ")
words = sentence.split()
print(" ".join(words[::-1]))

#or

def revrse(text):
    word=text.split()
    return " ".join(word[::-1])
print(revrse("harsha is good"))