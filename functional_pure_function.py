#pure functions results will only depends on its arguments otherwise it will be impure function
def sqrt(x):
    """"this program is for finding square root of a number"""
    return x*x
print(sqrt.__doc__)
print(sqrt(6))