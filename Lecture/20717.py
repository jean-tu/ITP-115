##functions
# import random
#
# def healthTip():
#     num = random.randrange(4)
#     if num == 0:
#         print("Drink  more water")
#     elif num == 1:
#         print("An apple away keeps the doctor away!")
#     elif num == 2:
#         print("Wash your hands")
#     else:
#         print("Get 8 hours of sleep per night")
#
# healthTip()

# def inspirationalQuote(day):
#     if day.lower() == "monday":
#         print("Just getting started -- limitless potential!")
#     elif day.lower() == "tuesday" or day.lower() == "wednesday" or day.lower() == "thursday":
#         print("Hang in there - doing great!")
#     elif day.lower() == "friday":
#         print("Yay!")
#     elif day.lower() == "saturday" or day.lower() == "sunday":
#         print("It's the weekend! Live it up!")
#     else:
#         print("Are you sure that's a day of the week?")
#
# today = input("What day of the week is it?: ")
# inspirationalQuote(today)


def salesTax(county):
    percent = 0
    if county.lower() == "los angeles":
        percent = 9.25
    elif county.lower() == "ventura":
        percent = 8.5
    else:
        percent = 7
    return percent

countyName = input("What county do you live in? (Los Angeles or Ventura): " )
print(salesTax(countyName))