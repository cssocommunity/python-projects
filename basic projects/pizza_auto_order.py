print("thank, you for choosing pizza automatic delivery")
size = input("what size pizza do you want (small, medium, large)? ")

cost = 0.00
if size.lower() == "small":
    cost += 12.50
if size.lower() == "medium":
        cost += 17.00
if size.lower() == "large":
            cost += 22.50
peperoni =input("do you want pepperoni? (yes/no) ")
if peperoni.lower() == "yes":
         cost += 1.50
mushrooms = input("do you want mushrooms? (yes/no) ")
if mushrooms.lower() == "yes":
              cost += 1.00
cheese = input("do you want cheese? (yes/no) ")
if cheese.lower() == "yes":
                   cost += 1.00
else:
                   cost += 0.50

print(f"your total cost is ${cost}")