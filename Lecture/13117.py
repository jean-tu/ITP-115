# string = "Hello"
# print(string[-2])


# msg = "Hello everyone!"
# segment = msg[4:9]
# print(segment)
#
# msg = "This is a new statement"
# msg[2] = "j"
# print(msg)


# things = ["emu", "pig"]
# stuff = ["dog", "cat", "boa"]
# things += stuff #adding the 2 lists together
# print(things)
# grabBag = stuff[0:2]
# print(grabBag)

foods = ["pizza", "sushi", "ice cream", "french fries"]

for item in foods:
    for letter in item:
        print(item, letter)

# choice = "y"
# while choice.lower() == "y":
#     #add new items to our food list
#     newItem = input("What would you like to add: ")
#     foods.append(newItem)
#     choice = input("would you like to add another? (y/n): ")
# print(foods)
#
# # print()
# # l = foods[1:4]
# # print(l)
#
# favFood = input("what is your favorite food?")
# if favFood in foods:
#     print("Yes, we have", favFood, "in our list")
# else:
#     foods.append(favFood)
