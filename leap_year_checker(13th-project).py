
def is_leap_year(year):

    if year % 400 == 0:
        print("leap year")
    elif year % 100 != 0 and year % 4 == 0:
        print("leap year")
    else:
        print("Not Leap Year")

year = int(input("Enter your year : "))
is_leap_year(year)

