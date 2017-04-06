# Jean Tu
# ITP 115, Spring 2017
# Assignment 2: Vending Machine & Choose Your Own Adventure Game
# 1/28/2017
# Description:
# This assignment simulates a purchase made in money that was used in Harry Potter
# This assignment also has a "Choose Your Adventure" story as part 2

#Part 1
choice = " "
itemBought = " " #to be able to know what type of item the user decided to buy
cost = 0    #how much should the user expect to pay for the item they've selected to buy
while choice == " ":
    print("Please select an item from the vending machine : ")
    print(" a) Butterbeer: 58 knuts")
    print(" b) Quill: 10 knuts")
    print(" c) The Daily Prophet: 7 knuts ")
    print(" d) Book of Spells 400 knuts ")
    choice = input("> ")
if choice.lower() == "a":
    itemBought = "Butterbeer"
    cost = 58
elif choice.lower() == "b":
    itemBought = "Quill"
    cost = 10
elif choice.lower() == "c":
    itemBought = "The Daily Prophet"
    cost = 7
elif choice.lower() == "d":
    itemBought = "Book of Spells"
    cost = 400
else:
    print("You have entered an invalid option. You will be given Butterbeer for 58 knuts")
    itemBought = "Butterbeer"
    cost = 58

insta = " "
coupon = 0
while insta == " ":
    insta = input("Will you share this on Instagram? (y/n): ")
if insta.lower() == "y":
    coupon = 5
    print("Thanks! You get 5 knuts off your purchase")
elif insta.lower() == "n":
    coupon = 0
else:
    print("You have entered an invalid option. No coupon will be used")
    coupon = 0

"""
Doing the math
1 knut    = 1   knut
1 sickle  = 29  knuts
1 galleon = 493 knuts
"""
galleon = 493
change = galleon - cost + coupon #the change is after removing the cost, give them $ back if they have a coupon
#Do the math portion here:
sickle = change//29
sickConv = sickle*29  #converting the number on how many knuts were converted to sickle's
knuts = (change-sickConv) # the amount of sickles left over
print("")
print("You bought a", itemBought, "for", str(cost), "knuts (with coupon of", coupon,
      "knuts) and paid with one galleon")
print("Here is you change (", str(change), "knuts):")
print("Sickles:", sickle)
print("Knuts:", knuts)


#Part 2

#MUST be able to handle capital & lower case letters
#If the user entered an INVALID option, tell them that they have entered incorrectly
    # Give the user a default choice for choosing something incorrect

print("")
print("Welcome to a choose your own adventure game. \n")
springBreak = " "
while springBreak == " ":
    print("You are about to plan your trip to go to another country for Spring Break that is coming up in about "
          "three weeks. \nYou want to do something with your friends, but your family also has plans to go somewhere. "
          "It's your senior year,\nso it's going to be the last Spring break you get before you enter the work force. \n")
    print("You choose to:")
    print("a) Spend spring break with your family.")
    print("b) Spend spring break with your friends.")
    print("c) Do neither, you want to spend spring break by yourself.")
    springBreak = input("> ")
if springBreak.lower() == "a":  #spring break with family
    print("")
    print("Because you've decided to spend spring break with your family, you don't actually have to plan out \n"
          "anything because your parents will do that for you. They will take care of the reservations,\n"
          "transportation and all of the food expenses. All that you have to do is decide where you would like to go.")
    print("")
    print("You decided that you would like to go to: ")
    print("a) Rome")
    print("b) The Bahamas")
    print("c) Taiwan")
    print("d) Hawaii")
    location = input()
    print("")
    if location.lower() == "a":
        print("You've choosen to go to Rome! Have fun!")
    elif location.lower() == "b":
        print("Have fun basking in the sun in the Bahamas!!")
    elif location.lower() == "c":
        print("Take some time to try the stinky tofu!!")
    elif location.lower() == "d":
        print("Let yourself relax as you hit up all the beaches")
    else:
        print("ERROR: You selected an invalid option")
elif springBreak.lower() == "b": #Spring break w/ friends
    print("You've decided to ditch your family and spend spring break with your friends. Your friends want \n"
          "each person that is going on the trip to decide on a role to take on. \n")
    print("")
    print("The role you'd like to take on is:")
    print("a) Trip Planner")
    print("b) Budget Person")
    print("c) Gatherer of supplies")
    print("d) None, you decided you'd rather spend that time with family!")
    role = input()
    print("")
    if role.lower() == "a":
        print("Congrats, you've taken on the role as Trip Planner!")
    elif role.lower() == "b":
        print("Congrats, you've taken on the role as Budget Person")
    elif role.lower() == "c":
        print("Congrats, you've taken on the role as the Gatherer of supplies")
    elif role.lower() == "d":
        print("Good for you, you've decided that you wanted to spend time with family <3")
    else:
        print("ERROR: You did not select a valid option")
elif springBreak.lower() == "c": #spring break alone
    print("")
    print("You've decided to spend spring break alone. There have been many contributing factors that made you \n"
          "choose this decision. Your family and friends respect your decision and will leave you \n "
          "alone for the whole week that you are on spring break")
    print("")
    print("You've decided to spend spring break alone because: ")
    print("a) You are an introvert and want to spend time alone")
    print("b) You just wanted some time to explore on your own")
    print("c) You just hate people")
    print("d) You've actually changed your mind and want to see your family & friends")
    alone = input()
    print("")
    if alone.lower() == "a":
        print("Enjoy your nice break from people")
    elif alone.lower() == "b":
        print("Have a reat time exploring! Be sure to check out Yelp for suggestions!")
    elif alone.lower() == "c":
        print("Okay.....")
    elif alone.lower() == "d":
        print("Great choice, spend time with those you love")
    else:
        print("ERROR: You did not select a valid option")
else: #did not select a correct option
    print("ERROR: You did not select a valid option")
print("")
print("THE END")