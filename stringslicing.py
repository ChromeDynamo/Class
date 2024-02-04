#stringslicing=create a substring by extracting elements from another string
#              indexing[] or slice()
#              [start:stop:step]
name="Chrome Dynamo"
first_name=name[0:6:1]
last_name=name[7:13:1]
reversed_name=name[::-1]
print(first_name)
print(last_name)
print(reversed_name)

def f(x):
    y=x+2
    return y
print(f(5))