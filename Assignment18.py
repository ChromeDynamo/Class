#8. Write a program to convert Celsius (C) values into Fahrenheit (F). The program should ask for Celsius
#value from the user and print the Fahrenheit value as an output.

#Formula to Convert Celsius o Fahrenheit: [ F = C * ( 9 / 5 ) + 32 ]
C=int(input("Enter value in Celsius"))
F=C * ( 9 / 5 ) + 32
print("Value in Farenheit is "+str(F)+"F")