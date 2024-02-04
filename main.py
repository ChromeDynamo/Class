print("I love burgers")
print("every bit of it")

#variables
first_name = "Chrome"
last_name = "Dynamo"
full_name = first_name+" "+last_name
print("The name is "+full_name)
#print(type(full_name))
age = 17
age += 1
print("Age is "+str(age))
#print(type("Age is "))
#print(type(age))
height = 173.74
#print(type(height))
print("Height is "+str(height)+"cm")
human=True
print("Human?"+" "+str(human))
#print(type(human))
#variables=str, int, float, bool

#multiple assignment = allows us to assign multiple variables at the same time using one line of code
name, age, height = "chrome", 18, 173.74
print(name)
print(age)
print(height)
spongebob=patrick=squidward="Cartoon"
print("spongebob is "+spongebob)
print("patrick is "+patrick)
print("squidward is "+squidward)

#stringe methods
print(len(name))
print(name.find("o")) #starts from 0
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("c"))
print(name.replace("c","C"))
print(name*5)

#type cast convert data type of a value to another data type
x=1
y=2.0
z="3"
x=float(x)
y=str(y)
z=int(z)
print(x)
print(y)
print(z)

#user input
name=input("What is your name?")
age=input("How old are you?")
height=float(input("How tall are you in cm?"))
age=int(age)+1
print("Hello"
      " "+name)
print("You will be "+str(age)+" in a year")
print("You are "+str(height)+"cm tall")

