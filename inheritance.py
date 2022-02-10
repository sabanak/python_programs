# #single inheritance
# class student:
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         self.name=input("enter name")
# class hod(student):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def putData(self):
#         self.hodname=input("enter hod name")
#     def display(self):
#         print("student name is\t",self.name)
#         print("hod name is\t",self.hodname)
# objectderivedclass=hod('')
# objectderivedclass.getData()
# objectderivedclass.putData()
# objectderivedclass.display()

#single inheritance by using code reusability
# class student:
#     def __init__(self,name,hodname):
#         self.name=name
#         self.hodname=hodname
#     def getData(self):
#         self.name=input("enter name")
# class hod(student):
#     def putData(self):
#         self.hodname=input("enter hod name")
#     def display(self):
#         print("student name is\t",self.name)
#         print("hod name is\t",self.hodname)
# objectderivedclass=hod('','')
# objectderivedclass.getData()
# objectderivedclass.putData()
# objectderivedclass.display()


#multilevel inheritance
# class student:
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         self.name=input("enter name")
# class hod(student):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def put(self):
#         self.hodname=input("enter hod name")
# class department(hod):
#     def __init__(self,department):
#         self.department=department
#     def putData(self):
#         self.department=input("enter department name")
#     def display(self):
#         print("student name is\t",self.name)
#         print("hod name is\t",self.hodname)
#         print("department is\t",self.department)
# objectsecondderivedclass=department('')
# objectsecondderivedclass.getData()
# objectsecondderivedclass.put()
# objectsecondderivedclass.putData()
# objectsecondderivedclass.display()

#multilevel inheritance by using code reusability
class student:
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def getData(self):
        self.name=input("enter name")
class hod(student):
    def __init__(self,hodname):
        self.hodname=hodname
    def put(self):
        self.hodname=input("enter hod name")
class department(hod):
    def putData(self):
        self.department=input("enter department name")
    def display(self):
        print("student name is\t",self.name)
        print("hod name is\t",self.hodname)
        print("department is\t",self.department)
objectsecondderivedclass=department('')
objectsecondderivedclass.getData()
objectsecondderivedclass.put()
objectsecondderivedclass.putData()
objectsecondderivedclass.display()

#multiple inheritance
# class student:
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         self.name=input("enter name")
# class hod:
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def get(self):
#         self.hodname=input("enter hod name")
# class department(student,hod):
#     def __init__(self,department):
#         self.department=department
#     def put(self):
#         self.department=input("enter department")
#     def display(self):
#         print("student name is\t", self.name)
#         print("hod name is\t", self.hodname)
#         print("department is\t", self.department)
# objderivedclass=department('')
# objderivedclass.getData()
# objderivedclass.get()
# objderivedclass.put()
# objderivedclass.display()