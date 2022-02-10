#import keyword
#print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if'
#'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getData(self):
        self.name=input("enter your name")
        self.marks=(input("enter your marks"))
    def putData(self):
        print("Name :",self.name, '\t',"Marks :" ,self.marks)
classobject=student('','')
classobject.getData()
classobject.putData()