#The perimeter of a rectangle with length 9 & width 7
l=9
w=7
p=2*(l+w)
print("Perimeter of rectangle is "+str(p))
print(" ")

#Your name stored as variable
n=input("Enter your name")
print("Your name '"+n+"' is stored in variable n")
print(" ")

#Python is great, it's wild!
print("Python is great, it's wild!")
print(" ")

#The difference between Beth’s age (57) and Tom’s (34)
B=57
T=34
Difference=B-T
print("Difference between their ages is "+str(abs(Difference)))
print(" ")

#2 to the 10th power
print("2 to the 10th power is "+str(2**10))
print(" ")

#7 factorial minus 5 factorial
sf=1
ff=1
for i in range(7,1,-1):
    sf=sf*i
for j in range(5,1,-1):
    ff=ff*j
print("Factorial of 7 is "+str(sf)+" and factorial of 5 is "+str(ff))
print("Their difference is "+str(sf-ff))
print(" ")

#Your forename multiplied by 5
n=input("Enter your forename")
print("Forename multiplied by 5: ")
print(n*5)
print(" ")

#Your name left justified 15 spaces
n=input("Enter your name")
print("Your name left justified 15 spaces is ")
print(n.ljust(15))
print(" ")

#PI to 5 decimal places
import math
pi = math.pi
npi = format(pi, ".5f")
print("Value of Pi to 5 decimal places: "+str(npi))
print(" ")

#A variable with the name def that stores the number 7
def_=7
print(def_)
print(" ")

#200 modulus 12
print("200 modulus 12 is "+str(200%2))
print(" ")

#7.2 as an integer value
f=7.2
print(str(f)+" as integer value is "+str(int(f)))
print(" ")

#The Unicode encoding for your name
n=input("Enter your name")
print("The unicode encoding for your name is "+str(n.encode()))