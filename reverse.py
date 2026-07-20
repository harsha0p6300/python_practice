#reverse a string using a slicing
x=lambda x:x[::-1]
print(x("Anudeep"))

#reverse a string using the reverse keyword
def rev(n):
    return "".join(reversed(n))
user=str(input("Enter a string: "))
print(rev(user))
    
#reverse a string without using slicing and reversed keyword
string="Harsha"
text=""
for char in string:
    text=char+text
print(text)
