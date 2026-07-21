#Write a Python program to print all duplicate elements in a list.
def duplicates(lst):
    found = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in found:
                found.append(lst[i])
    return found

user = list(map(int, input("Enter the numbers: ").split()))
print(duplicates(user))



