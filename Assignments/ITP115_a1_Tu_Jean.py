# Jean Tu
# ITP 115, Spring 2017
# Assignment 1: Mad Libs
# jeantu@usc.edu

#5 strings, 3 int, 1 float
# 2 values must be used in mathmatical calculation (add, multiply, etc)
person = input("Enter a name: ")
transportation = input("Enter a verb [in terms of transportation] in past tense: ")
location = input("Enter a location: ")
color = input("Enter a color: ")
emotion = input("Enter an emotion: ")
intTeeth = int(input("How many times do you brush your teeth a day? "))
intPlush = int(input("How many stuffed animals do you have? "))
intShoes = int(input("Guesstimate how many pairs of shoes you have: "))
calculationFeatures = intPlush * intShoes
floatRandom = float(input("Enter a number with a decimal: "))

print("_" + person + "_ " + transportation + "_",
      "into a Ferrari dealership in", "_" + location + "_,", "They had then came a cross a dealer and the dealer had",
      "_" + str(intTeeth) + "_ hats on his head, \n and he said  that it is always a conversation starter. But" , "_" + person + "_",
      "felt", "_" + emotion + "_", "and didn't care.  \n They just went on to tell the dealer the type of car they wanted. It had to be a" ,
      "_" + color + "_", "4-door sedan, with \n ",  "_" + str(calculationFeatures) + "_", "additional add-ons",
      "with a", "_" + str(floatRandom) + "_", "rating in safety! Luckily, the dealer said that they had", "_" + str(intShoes) + "_",
      "cars like that for him to choose from \n, but only", "_" + str(intPlush) + "_", "met his criteria.")