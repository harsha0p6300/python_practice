#Check whether one string is a rotation of another
def rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1 == str2:
            return True
        str1 = str1[1:] + str1[0]
    return False
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(rotation(str1, str2))


    

