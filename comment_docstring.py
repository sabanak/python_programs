#this is comment

def add(a,b):
    """this function is for adding two numbers"""
    return a+b
print(add(2,3))
print("access docstring using __doc__")
print(add.__doc__)
print("access docstring using help()")
help(add)
