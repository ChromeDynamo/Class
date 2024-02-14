#3. With a program to take as an input an integer number n, and generate a dictionary that contains (i, i*i)
#where “i” lies between 1 and n (both included). The program should then print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n=int(input("Enter an integer"))
dictionary={}
for i in range(1,n+1):
    dictionary[i]=i*i
print(dictionary)
