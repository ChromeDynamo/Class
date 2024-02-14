#4. Write a program that can accept two strings as input and print the string with maximum length as an
#output. If two strings have the same length, then the program should print both the strings.
a=str(input("Input a string value"))
b=str(input("Input a string value"))
if len(a)>len(b):
    print("Longer string is "+a)
elif len(b)>len(a):
        print("Longer string is "+b)
elif len(a)==len(b):
            print("Since the given strings are equal in length, the given strings are "+a+" and "+b)