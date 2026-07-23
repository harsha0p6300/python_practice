#Remove duplicate characters while preserving the first occurrence.

def charc(text):
    seen=set()
    result=[]
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return " ".join(result)

print(charc("Programming"))

            