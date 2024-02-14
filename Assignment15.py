#5. Write a program which can produce a dictionary where the keys are numbers between 1 and 20 (both
#included) and the values are the square of keys. The program should print the values only.
dictionary={}
for i in range(1,20+1):
    dictionary[i]=i*i
print(dictionary.values())