#1. Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included). The numbers should be printed on the output screen.
#(Bonus point if you can print all the numbers on a single line)
for i in range(2000,3200):
    x=i%7
    y=i%5
    if x==0 and y!=0:
        print(i,end=" ")
print("")


