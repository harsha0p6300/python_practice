# #7. Find the longest word in a sentence.
def long_word(sentence):
    words=sentence.split()
    return max(words, key=len)

sentence=input("Enter a sentences: ")
print(long_word(sentence))

#or

def long_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            long = word
    return long
sentence = input("Enter a sentence: ")
print("Longest word:", long_word(sentence))
