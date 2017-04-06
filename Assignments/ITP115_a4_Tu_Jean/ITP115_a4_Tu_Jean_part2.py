# Jean Tu
# ITP 115, Spring 2017
# Assignment 4: Word Jumbled and encryption
# 02/12/2017
# Description:
#   This is the encryption, but we don't shift spaces or punctuation

originalAlpha = "abcdefghijklmnopqrstuvwxyz" # the original alphabet string
specialCharacters = " ,./<>?;:\'\"[]{}`~!@#$%^&*()_+-=0123456789"

#Takes in how much to shift and will return the new shifted message
def shiftAlpha(shift):
    shiftedAlpha = originalAlpha[shift:len(originalAlpha)] + originalAlpha[0:shift]
    return shiftedAlpha

def encryptMessage(shiftedAlpha, message):
    newMessage = ""
    for i in message:
        if specialCharacters.find(i) != -1: # if it was in there, let it be the same
            newMessage = newMessage + i
        else:
            index = originalAlpha.index(i)
            newMessage = newMessage + shiftedAlpha[index]
   # print (newMessage)
    return newMessage

def decryptMessage(shiftedAlpha, encryptedMessage):
    decryptedMessage = ""
    for i in encryptedMessage:
        if specialCharacters.find(i) != -1:
            decryptedMessage = decryptedMessage + i
        else:
            index = shiftedAlpha.index(i)
            decryptedMessage = decryptedMessage + originalAlpha[index]

    return decryptedMessage


def main():
    message = input("Enter a message: ")
    shift = int(input("Enter a number to shift by (0-25): "))
    print("Encrypting message....")
    shiftedAlpha = shiftAlpha(shift)
    encryptedMessage = encryptMessage(shiftedAlpha, message)
    print("         Encypted message: ", encryptedMessage)
    print("Decrypting message....")
    decryptedMessage = decryptMessage(shiftedAlpha, encryptedMessage)
    print("      Decrypted message:", encryptedMessage )
    print("      Original message:", decryptedMessage)

main()