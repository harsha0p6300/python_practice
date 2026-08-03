fst1=int(input("Enter the first Number: "))
fst2=int(input("Enter the second Number: "))
o=int(input(" \n1.Addition(+)\n2.Substraction(-)\n3.Multiplication(*)\n4.Division(/)\nEnter the opration to perform:"))

match o:
    case 1:
        print(f"The sum of {fst1} & {fst2} is {fst1+fst2}")
    case 2:
        print(f"The sub of {fst1} & {fst2} is {fst1-fst2}")
    case 3:
        print(f"The product of {fst1} & {fst2} is {fst1*fst2}")
    case 4:
        if o==0:
            print("ZeroDivisionError: division by zero cant able to divide with the zero")
        else:
            print(f"The Division of {fst1} & {fst2} is {fst1/fst2}")
    case _:
        print(("Invalid operator..!"))
