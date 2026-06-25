# 39. Highest Score
'''
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(sum(student_scores))

print(max(student_scores))
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)
'''

# 40. for loops and the range() function
'''
total = 0
for num in range(1, 101):
    total += num
print(total)
'''

# 41. Day 5 Project: Create a Password Generator
'''
import random


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6' ,'7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?: "))
nr_numbers = int(input("How many numbers would you like in your password?: "))
nr_symbols = int(input("How many symbols would you like in your password?: "))

password_list = []
for i in range(0, nr_letters):
    rnd_letter = letters[random.randint(0, len(letters)-1)]
    password_list.append(rnd_letter)
for i in range(0, nr_numbers):
    rnd_number = numbers[random.randint(0, len(numbers)-1)]
    password_list.append(rnd_number)
for i in range(0, nr_symbols):
    rnd_symbol = symbols[random.randint(0, len(symbols)-1)]
    password_list.append(rnd_symbol)
    
random.shuffle(password_list)
print("".join(password_list))
'''
