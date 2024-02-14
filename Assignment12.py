#2. Write a program that can compute the factorial of a given number. The number whose factorial is to be
#computed is input from the keyboard.
#(Hint: Factorial of 3, also written as 3! = 3 X 2 X 1. Similarly, 5! = 5 X 4 X 3 X 2 X 1 )
a=int(input("Enter a number"))
f=1
for i in range(a,1,-1):
    f=f*i
print("Factorial of given number is "+str(f))
