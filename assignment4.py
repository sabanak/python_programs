#BMI calculator
def BMI(weight,height):
    return weight/(height*height)
weight=int(input("Enter you weight in kilograms"))
height=float(input("Enter your height in meters"))
print(BMI(weight,height))