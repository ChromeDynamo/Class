#7. Write a program which can generate a list where the values are square of numbers between 1 and 20
#(inclusive). The program should only print the last 5 elements of the list.
list=[]
for i in range(1,20+1):
    list.append(i*i)
print("Last five elements are ",list[-5:])