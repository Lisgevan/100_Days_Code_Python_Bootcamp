# 31. Random Module
'''
import random

random_number = random.random()
if random_number < 0.5:
    print("Heads")
else:
    print("Tails")
'''

# 33. Who will pay the bill?
'''
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friend = random.choice(friends)
print(random_friend)
'''

# 35. Day 4 Project: Rock Paper Scissors
'''
'''
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

options = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(1,2)

print("You chose")
print(options[users_choice])
print("Computer chose")
print(options[computer_choice])

if (users_choice == 0 and computer_choice == 1) or (users_choice == 1 and computer_choice == 2) or (users_choice == 2 and computer_choice == 0):
    print("You loose")
elif users_choice == computer_choice:
    print("It's a draw")
else:
    print("You win!")






