

def main():
    a = 6

    errorHappened = True
    while errorHappened == True:
        try:
            b = int(input("Enter a number: "))
            print("\t***just asked for input")

            print(a, "divided by", b, "is", a/b)
            print("just did divisions")
        except ZeroDivisionError:
            print("Oops! Cannot divide by 0")
        except ValueError:
            print("Oops! You didn't follow directions when I politely asked for a number")
        else:
            errorHappened = False
        print("just finished the try/except code")

main()