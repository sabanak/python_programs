#a higher order function is the function which uses other functions as it's arguments
def add(a,b):
    """this program is for finding sum of two numbers"""
    return a+b
print(add.__doc__)
print(add(34,54))
def add_twice(add,x,y):
    """this function will use first function add as it's argument"""
    return add(x,y)
print(add_twice.__doc__)
print(add_twice(add,76,23))
