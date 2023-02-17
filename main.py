# Welcome Message
print("========================")
print("Welcome to the UMBC")
print("Car Customization Form!")
print("========================")
print()
# Ask about the Make and Model of desired car
print("(For multiple choice problems, please enter the letter of the selection you're looking for)")
print()
print("~ Make & Model ~")
print("1. What model of car are you ordering?")
print("  a. Ford")
print("  b. Honda")
print("  c. Nissan")
print("  d. Toyota")
# Saves their answer
model = input("Please enter 'a' - 'd': ")
print()
print("Would you like to upgrade from the 4-door option to the 2-door option?")
# Saves their answer
doorUpgrade = input("Please enter 'yes' or 'no': ")
print()
#Ask about desired Exterior elements of desired car
print("~ Exterior ~")
print("What color would you like your car to be?")
# Saves their answer
color = input("You may enter the name of any color you'd like: ")
print()
print("Would you like the deluxe weather package?")
# Saves their answer
weatherUpgrade = input("Please enter 'yes' or 'no': ")
print()
print("~ Interior ~")
print("Which engine would you like your car to have?")
print("  a. I-4 Entry Engine")
print("  b. V-6 Performance Engine")
print("  c. Eco Diesel Engine")
# Saves their answer
engine = input("Please enter 'a' - 'c': ")
print()
print("6. Would you like heated seats?")
# Saves their answer
seatHeat = input("Please enter 'yes' or 'no': ")
print()
# Separate answers from the questions
print("========================")
print()
# Display summary of chosen options
print("~ Summary ~")
print()
print(f"Model Option: {model}")
print(f"Upgrade to 2-Door: {doorUpgrade}")
print(f"Desired Color: {color}")
print(f"Upgrade to Deluxe Weather: {weatherUpgrade}")
print(f"Engine Option: {engine}")
print(f"Upgrade to Heated Seats: {seatHeat}")