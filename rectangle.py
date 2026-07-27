#Create a Rectangle class with area() and perimeter() methods.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

#Taking user inputs
x=int(input("Enter the length of the rectangle: "))
y=int(input("Enter the width of the rectangle: "))

#creating object
rec=Rectangle(x,y)

#calling methods
area=rec.area()
perimeter=rec.perimeter()

print("Area",area)
print("perimeter",perimeter)

