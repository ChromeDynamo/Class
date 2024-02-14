#9. Write a program which accepts a string as input from the keyboard. If the input string is "even" or
#"EVEN" or "Even", print the even numbers from the list (my_numbers) given below. If the string is "odd" or
#"ODD" or "Odd", print the odd numbers from the list. Otherwise simply print “Unknown Input!”

#my_numbers = [7, 2, 4, 11, 19, 24, 66, 1, 42, 22, 37, 5, 3, 92, 73]

a=str(input("Enter 'even' or 'odd': "))
my_numbers=[7, 2, 4, 11, 19, 24, 66, 1, 42, 22, 37, 5, 3, 92, 73]
if a.lower()=="even":
    for n in my_numbers:
        if n%2==0:
            print(n)
elif a.lower()=="odd":
    for n in my_numbers:
        if n%2!=0:
            print(n)
else:
    print("Invalid Input")
