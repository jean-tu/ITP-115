# Jean Tu
# ITP 115, Spring 2017
# Lab L4
# jeantu@usc.edu

#ord(Letter) = letter--> ASCII
#chr(num) = ASCII --> letter


print("What would you like to do?: ")
print("a) See the ASCII code for the alphabet")
print("b) Translate a word into its ASCII code")
choice = input("Select a or b: ")
print("")
if choice.lower() == "a": #ask if upper or lower
    upperOrLower = input("Do you want to see the alphabet in upper (u) or lower (l): ")
    if(upperOrLower.lower() == "u"):
        for upper in range(65, 91,1):
            print(chr(upper))
    elif(upperOrLower.lower() == "l"):
        for lower in range(97, 123, 1):
            print(chr(lower))
    else:
        print("You have entered an invalid option!!")
elif choice.lower() == "b": #convert their own word into ASCII
    convertWord = input("Enter the word that you would like to translate into ASCII: ")
    for letter in convertWord:
        print(letter, ":", str(ord(letter)))
else:
    print("You did not enter a valid option....I said a or b")
