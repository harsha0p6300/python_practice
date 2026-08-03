class Employee:
    company="Asus" #This is class attribute

    def __init__(self,salary,name,bond,company): #__init__ =constructor is used to initialze the object
        self.salary=salary #create ab instance attribute of name salary and assign it with salary
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.Salary is {self.salary}. The bond is for {self.bond} years")

e1=Employee(34000,"John",3,"Tesla")
print(e1.company) #Will always print instance attribute whenever 
print(Employee.company) #This will always print the class attribute

#Object introspection
print(dir(e1))