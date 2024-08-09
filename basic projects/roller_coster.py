print("welcome to our roller coaster automate ticketing system")
print("make sure your age not less than 13 or more than 50")
age = int(input("Please enter your age: "))
cost = 0
if age >= 13 and age <= 15:
    print("welcome to our kids.")
    cost += 10
if age >= 15 and age <= 18:
    print("welcome to our teenagers.")
    cost += 15

if age >= 18 and age <= 30:
    print("you are eligible. most welcome to our youngster ride.")
    cost += 35
if age >= 30 and age <= 50:
    print("you are eligible. welcome to our senior ride.")
    cost += 20
if age > 50:
    print("Sorry, we are unable to accommodate your age group.")
    exit()

food = input("Do you want to eat food? (yes/no): ")

if food.lower() == "yes":
    cost += 5
    print("Enjoy your meal!")
rest = input("Do you want to rest? (yes/no): ")

if rest.lower() == "yes":
    cost += 2
    print("Take rest comfortably!")
    print("thank you for our roller coaster ride and other services.i hope you enjoyed it. Your total cost is ₹", cost)