#10. Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of
#the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and
#five print “Fizz Buzz”.
for i in range(1,20):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
