#2) Write a program to merge two dictionaries. If a key exists in both dictionaries, add their values.
dict1={
    "a":10,
    "b":20
}

dict2={
    "b":30,
    "c":40
}

for key in dict2:
    if key in dict1:
        dict1[key]+=dict2[key]
    else:
        dict1[key]=dict2[key]
print(dict1)