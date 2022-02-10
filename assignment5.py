#Function which handles divide by zero exception
try:
    def div(a,b):
        return a/b
    a=int(input("Enter first number"))
    b=int(input("Enter second number as zero"))
    print(div(a,b))
except ZeroDivisionError:
    print("An error occured due to zero division error")
