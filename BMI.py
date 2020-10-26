"""This is a BMI calculator"""
print("This is a BMI calculator")
name=str(input("Enter your name: "))
mass=int(input("Enter Your Weight in kg's: "))
height=float(input("Enter your weight in meters: "))
BMI=mass/(height*height)
print(f'Hey {name}, your height is {height} and your BMI is {BMI} ')
