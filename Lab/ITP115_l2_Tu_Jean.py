# Jean Tu
# ITP 115, Spring 2017
# Lab L2
# jeantu@usc.edu

import random

coffeeSize = input("What size coffee do you want (S, M, L)? ")
choose = input("Would you like a random temperature drink?(y/n) ")
if choose == "y":
    temperature = random.randrange(200) + 1
else:
    temperature = int(input("What temperature would you like (in degrees)? "))
blend = input("What type of beans / blend would you like? ")
cream = input("Would you like room for cream (y/n)? ")

if coffeeSize == "S" or  coffeeSize == "s":
    size = "small"
elif coffeeSize == "M" or coffeeSize == "m":
    size = "medium"
elif coffeeSize == "L" or coffeeSize == "l":
    size = "large"
else:
    size = "large (b/c you didn't enter a selected size)"

if temperature > 175:
    temp = "hot"
elif temperature < 175 and temperature > 0:
    temp = "iced"
else:
    temp = "iced (b/c you didn't enter a positive number)"

if cream == "y":
    creamBool = "with cream."
elif cream == "n":
    creamBool = "with no cream."
else:
    creamBool = "with no cream (b/c you didn't enter y/n)."

print()
print("You ordered a", size, temp, blend, creamBool)
