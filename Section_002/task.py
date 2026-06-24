# 15. Type Error, Type Checking and Type Conversion
'''
print("NUmber of letters in your name: " + str(len(input("Entar your name: "))))
'''

# 16. Mathematical Operations in Python
'''
print(3*3+3/3-3) # 7
print(3*(3+3)/3-3) # 3
'''

# 18. Day 2 Project: Tip Calculator
'''
'''

print("Welcome to the tip calculator!")
total_bill = int(input("What is the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_num = int(input("How many people to split the bill? "))

amount_per_person = total_bill*(1+tip_percentage/100)/people_num

print(f"Each person should pay: ${round(amount_per_person, 2)}")