#count the word frequency 

def  wfreq(text):
    words=text.split()
    frequency={}

    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency

text="data science data analytics"
print(wfreq(text))