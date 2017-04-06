def stringMethods(string):
    print("Inside stringMethods")
    string = string.upper()
    print("Using s.upper() on string:", string)
    string = string.lower()
    print("Using s.lower() on STRING:", string)
    string = "sTrInG"

def problem1():
    i = 2
    j = 9
    k = "3"
    x = 3.0
    y = 2.5
    print(j%i)
    print(k*i)
    print(j/i)
    print(j//i)
    print(x*y)


def main():
    string = "string"
    stringMethods(string)
    problem1()


main()