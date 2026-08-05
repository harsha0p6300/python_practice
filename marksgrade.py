#2.Create a Student class with methods to calculate the average marks and grade.
class student:
    def __init__(self,name,science,mathematics,English,Grammer):
        self.name=name
        self.science=science
        self.mathematics=mathematics
        self.English=English
        self.Grammer=Grammer
#for calculating the average
    def calculate_avg(self):
        avg=(self.science+self.mathematics+self.English+self.Grammer)/3
        return avg
#For calculating the Grade
    def calculate_grade(self):
        avg=self.calculate_avg()
        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=55:
            return "C"
        else:
            return"Failed..!"

#creating an object
s1=student("Harsha",90,41,63,50)

#Display the details
print("student Name:",s1.name)
print("Marks:",s1.calculate_avg())
print("Grade:",s1.calculate_grade())
        