''' here we calculation of bmi index tool by using the formula
H = height 
w = weight 

'''
from turtle import right


a = input( "what's your height? ")# type: ignore

b = input(" what's your weight? ") # type: ignore

h = float(a)

w = int(b)

bmi = w / (h * h)
bmi_string = str(bmi)
print ("you bmi index is " + bmi_string)


if bmi_string > '17':
    print("you are overweight")
elif bmi_string > '24':
    print("you are obese")
elif bmi_string > 30:
    print("you are clinically obese")
elif bmi_string > 35:
    print("you are morbidly obese")

# now, i finished my code by understand and solving the problem