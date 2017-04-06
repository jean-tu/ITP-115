# for i in range(0,50,5):
#     print(i, end=" ")
#   the code above returns: 0 5 10 15 20 25 30 35 40 45

#for num in range(3):
#    print(num + 2)
# prints 2
#3
#4

# msg = "spamalot"
# for letter in msg:
# 	print(letter.upper(), end=" ")
# #result is S P A M A L O T

# maxValue = int(input("Enter a number: "))
#
# total = 0
# for num in range(maxValue+1):
#     total = total + num
# print(total)

msg = input("Enter a saying: ")
vowels = "aeiou"
string = ""
for letter in msg:
    if letter in vowels:
    # if "a" == letter or "e" == letter or "i" == letter or "o" == letter or "u" == letter:
        string = string+ letter + " "
print("The combination of all the CONSTANTS in your saying is", string)
