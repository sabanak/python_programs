x=lambda a:a+2
print(x(5))

x=lambda a,b:a*b
print(x(2,6))

x=lambda a,b:a*b+5
print(x(2,6))

#In lamda function we can pass any number of argument and can have single expression
#syntax lamda arguments:expression

x=lambda a,b,c:a*b+5+c
print(x(2,6,8))


#how to use lambda in functions

def multiply(n):
    return lambda a:a*n
num1=multiply(6)
print(num1(11))


#in the same lambda function we can define more than one variable
def multiply(n):
    return lambda a:a*n
num1=multiply(6)
print(num1(11))
num2=multiply(7)
print(num2(11))