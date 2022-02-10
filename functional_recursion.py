#recursion is a function call itself.It must have a base case
#factorial of a number
# def factorial(x):
#     """this is a recursive function to find factorial of a number"""
#     if x==1:
#         return 1
#     else:
#         return x*factorial(x-1)
# print(factorial.__doc__)
# x=int(input("enter number"))
# print("Factorial is :",factorial(x))

#gcd of two numbers
# def gcd(x,y):
#     """program for finding gcd """
#     reminder=x%y
#     if reminder==0:
#         return y
#     else:
#         return gcd(y,reminder)
# x=int(input("enter number x:"))
# y=int(input("enter number y:"))
# print(gcd.__doc__)
# print("GCD is :",gcd(x,y))

#fibnocci series
def fib(n):
    """this program is for finding fibnocci series"""
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter number"))
print(fib.__doc__)
for i in range(n):
    print(i,"=",fib(i))
