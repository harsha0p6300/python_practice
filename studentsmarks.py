#Create a Student class with name and marks. Add display() and is_pass() methods. OOPS concept
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks",self.marks)
    def is_pass(self):
        if self.marks>=35:
            print("Result:Pass")
        else:
            print("Result:Fail..!")
student1=student("Harsha",85)

student2=student("Rakesh",33)
student1.display()
student1.is_pass()
print()
student2.display()
student2.is_pass()
print()