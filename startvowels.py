# Count how many words start with a vowel.
def start_vowel(sentence):
    spl=sentence.split()
    vowels='AEIOUaeiou'
    count=0
    for word in spl:
        if word[0] in vowels:
            count+=1
    return count

sentence="hai im harsha vardhan"
print(start_vowel(sentence))

#or

def start_vowel(sentence):
    return sum(1 for word in sentence.split() if word[0] in 'AEIOUaeiou')
user=input("Enter a sentences: ")
print(start_vowel(user))