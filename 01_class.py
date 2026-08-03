#Class:Class is a blueprint or a template/ EG.From for an Exam that contains name, age, electives, fathers name etc

#object: Specific instance that is created in the template (class) Eg: Form which contains the data for John Doe


class Employee:
    company="Hp"

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        return 34000

e1=Employee() # An object of class Employee is created here 
print(e1.get_salary())

e2=Employee()
print(e2.get_salary())

