#2.Write a Python program that prompts the user for two floating-point values and displays the
#results of the first number divided by the second, with exactly two decimal places displayed.
a=float(input("Enter a float value"))
b=float(input("Enter another float value"))
if b==0:
    print("Cannot divide by 0")
else:
    d=a/b
    r=format(d,".2f")
    print("Result: "+str(r))