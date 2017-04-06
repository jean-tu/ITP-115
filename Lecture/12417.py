# name = input("Enter your name: ")
# while not name: #basically a check to see if name is empty or not
#     name = input("Enter your name: ")
#
# print(name)

choice = "y"
while choice.lower() == "y":
    num = int(input("Enter a positive number: "))
    total = 0
    count = 0
    while num > 0:
        if(num%2 == 0):
            #print(num)
            total = total + num
            count = count + 1
        num = num - 1
    average = total/count
    print("The sum is", total, "The average is", average)
    choice = input("Do you want to add up numbers again (y/n)? ")

