def print_ast(n,string):
    print(string*n)
n = int(input("Enter the number of times to print the string: "))
string = str(input("Enter a string( Enter to use '*'): "))
if string:
    print_ast(n,string)
else:
    print_ast(n,"*")
