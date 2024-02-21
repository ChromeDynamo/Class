def result(a,b):
    if b == 0:
        print("Cannot divide by 0")
    else:
        d = float(a) / float(b)
        r = format(d, ".2f")
        print("Result: " + str(r))
a=input("Enter a number")
b=input("Enter another number")
result(a,b)
