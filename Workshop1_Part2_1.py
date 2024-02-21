#1.Write a Python program that prompts the user for two integer values and displays the results
#of the first number divided by the second, with exactly two decimal places displayed.
import math
a=input("Enter a number")
b=input("Enter another number")
if b==0:
    print("Cannot divide by 0")
else:
    d=float(a)/float(b)
    r=format(d,".2f")
    print("Result: "+str(r))