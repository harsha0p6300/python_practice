#2. Count the frequency of elements in a list using a dictionary.
list1=[1, 2, 2, 3, 1, 1]

def count_freq(li):
    freq={}

    for item in li:
        if item not in freq:
            freq[item]=1
        else:
            freq[item]+=1
    return freq
print(count_freq(list1))
