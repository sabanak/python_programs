class Computer:
    def __init__(self,brand_name,operating_system,color):
        self.brand_name=brand_name
        self.operating_system=operating_system
        self.color=color
    def getspecs(self):
        self.brand_name = "Lenovo"
        self.operating_system="Windows_10_Home"
    def displayspecs(self):
        print("BRAND NAME        : ", self.brand_name)
        print("OPERATING SYSTEM  : ",self.operating_system)
class Desktop(Computer):
    def __init__(self,weight):
        self.weight=weight
    def getspecs1(self):
        self.weight = "2.49KG"
        self.color = "Platinum_Gray"
class Laptop(Desktop):
    def displayspecs1(self):
        print("COLOR             : ",self.color) #Laptop class Inherit the methods of Computer class from Desktop class
        print("WEIGHT            : ",self.weight) #Laptop Class Inherit the attribute weight of Desktop class
objectlaptopclass=Laptop('')
objectlaptopclass.getspecs()
objectlaptopclass.displayspecs()
objectlaptopclass.getspecs1()
objectlaptopclass.displayspecs1()