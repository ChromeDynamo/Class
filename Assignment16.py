#6. Write a program which can generate and print a list where the values are square of numbers between 1 and
#20 (both included).
list=[]
for i in range(1,20+1):
    list.append(i*i)
print(list)
def ordered(n1,n2):
    return n1>n2
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
if num1>num2:
    a=bool(ordered(num1,num2))
    print("It is "+str(num1)+" being greater is "+str(a))
else:
    a=bool(ordered(num2,num1))
    print("It is "+str(num2)+" being greater is "+str(a))
