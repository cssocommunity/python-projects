#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
x_letters = int(input("How many letters would you like in your password?\n")) 
x_symbols = int(input(f"How many symbols would you like?\n"))
x_numbers = int(input(f"How many numbers would you like?\n"))



password = [random.choice(letters) for i in range(x_letters)]
password += [random.choice(symbols) for i in range(x_symbols)]
password += [random.choice(numbers) for i in range(x_numbers)]


("Your password is :", ''.join(password))

random.shuffle(password)
password = ''.join(password)

print(f"your password is : {password}")