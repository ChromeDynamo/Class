def Addition(a,b):
    print("Addition of given numbers is "+str(a+b))
def Subtraction(a,b):
    if a>b:
        print("Subtraction of given numbers is "+str(a-b))
    else:
        print("Subtraction of given numbers is "+str(b-a))
def Multiplication(a,b):
    print("Multiplication of given numbers is "+str(a*b))
def Divisition(a,b):
    print("Division of given numbers is "+str(a/b))
def Truncated_Division(a,b):
    print("Truncated division of given numbers is "+str(a//b))
def Modulus(a,b):
    print("Modulus of given numbers is "+str(a%b))
def Exponentiation(a,b):
    print("Exponentiation of "+str(a)+" to "+str(b)+" is "+str(a**b))
    print("Exponentiation of "+str(b)+" to "+str(a)+" is "+str(b**a))
a=int(input("Enter an integer"))
b=int(input("Enter another integer"))

print("Options:")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
print("5 for Truncated Division")
print("6 for Modulus")
print("7 for Exponentiation")

c=int(input("Enter your choice"))
if c==1:
    Addition(a,b)
elif c==2:
    Subtraction(a,b)
elif c==3:
    Multiplication(a,b)
elif c==4:
    Divisition(a,b)
elif c==5:
    Truncated_Division(a,b)
elif c==6:
    Modulus(a,b)
elif c==7:
    Exponentiation(a,b)
else:
    print("Invalid output. Only numbers from 1 to 7 accepted")