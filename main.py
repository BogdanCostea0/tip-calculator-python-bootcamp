

print("Welcome to the tip calculator")

total = float(input("What was the total bill?"))

how_many_people = float(input("How many people you want to split the bill?"))

percentage = float(input("What percentage would you like to give ?"))

tip = (total + percentage/100*total)/how_many_people

print("Total tip per person is:", round(tip,2))
