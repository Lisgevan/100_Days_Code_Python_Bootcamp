# 23. Introducing the Modulo
'''
number = int(input("Please give me a number to check: "))

if number%2==0:
    print("This is an even number")
else:
    print("This is an odd number")
'''

# 26. Pizza Order Practice
'''
# Small Pizza (S): $15
# Medium Pizza (M): $20
# Large Pizza (L): $25
# Add pepperoni to small pizza: +$2
# Add pepperoni to medium or large pizza: +$3
# Extra cheese: +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you wnant? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
bill = 0

if size == "s":
    bill +=15
elif size == 'm':
    bill +=20
else:
    bill += 25
    
if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'y':
    bill += 1
    
print(f"Your final bill is ${bill}.")
'''

# 28. Day 3 Project: Treasure Island
'''
from turtle import right


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
choise = input('    Type "left" or "right"\n')

if choise != "left":
    print("You fell into a hole. Game Over.")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    choise = input('   Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choise != "wait":
        print("Attacked by trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choise = input('   One red, one yellow and one blue. Which colour do you choose?\n')
        if choise == "red":
            print("Burned by fire. Game Over.")
        elif choise == "blue":
            print("Eaten by beasts. Game Over.")
        elif choise == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
'''
