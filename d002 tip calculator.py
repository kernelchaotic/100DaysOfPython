# Day 2 of 100 Days of Python: A Tip Calculator
print("Welcome to the tip calculator!")
print("Please answer all questions in numbers. \n")

total_bill = int(float(input("What was the total bill? $")))
people_split = int(input("How many people will the bill be split amongst? "))
percentage_tip = int(input("What percentage of a tip would you like to give? 10, 15, 20, etc. "))

total_tip = total_bill * (percentage_tip / 100)
divided_bill = (total_bill + total_tip) / people_split

print("\nYour total tip will be $" + str(total_tip) + ".")
print("Each person should pay $" + str(divided_bill) + " for a total cost of $" + str(total_bill + total_tip) + ".")
