import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

user = int(input("Enter your choice (rock = 0 /paper = 1 /scissors = 2): "))
if user >= 3 or user < 0:
    print("Invalid number, you lose!")
else:
    print(f"Your choice:\n{game[user]}")

computer = random.randint(0,2)
print(f"{computer} \n {game[computer]}")

if user == computer:
    print("It's a tie!")
    

if user == 'rock'and computer == 'scissors':
    print("you win")
elif computer == 'rock' and user == 'scissors':
    print("computer wins")
elif computer > user:
    print("computer wins")
elif user > computer:
    print("you win")

