# leap years are devidable by 4 with no remainder
# except every year that is devidable by 100 with no remainder
#unless the year is also devisable by 400

year = int(input("Please enter a Year to check if it is/was a leap year:\n"))

if year%4==0:
    print("The year meets the first criteria to be a leap year!\n\n")
    if year%100==0:
        print("The year failed the second criteria!\nChecking exception\n\n")
        if year%400==0:
            print("The exception is met! The year is a leap year!\n\n")
        else:
            print("The exception was not met! The year is not a leap year!\n\n")
    else:
        print("The second criteria was met! The year is a leap year!\n\n")
else:
    print("The year is not a leap year!\n")