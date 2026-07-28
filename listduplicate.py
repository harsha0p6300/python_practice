#1.Find duplicate elements in a list.
def list_duplicate(list):
    seen=[]
    dup=[]
    for num in list:
        if num in seen:
            if num not in dup:
                dup.append(num)
        else:
            seen.append(num)
    return dup

list1=[1,2,3,4,3,4,5,6,1]
print(list_duplicate(list1))
