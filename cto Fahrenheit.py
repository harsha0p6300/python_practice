#Using map(), convert the following list of temperatures from Celsius to Fahrenheit.
celsius=[0, 25, 30, 40]
faah=map(lambda x:x*9/5+32,celsius)
print(list(faah))