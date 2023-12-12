#control flow if/else

water_level = 50

if water_level > 80:
    print("Draining Water!")
else:
    print("Continue")

#nested if/elif statements

age = 21
height = 123

if height >=120:
    print("you are able to ride the roller coaster")
    if age <12:
        print("You may pay the lowest price of 5$!\n")
    elif age <=18:
        print("You may pay the lowered price of 7,5$!\n")
    else:
        print("You have to pay the full price!\n")
else:
    print("You are not allowed to ride the roller coaster, as you are not tall enough")


#multiple if statements

age = 0
height = 0
price = 0.00
want_photo = "No"

age = int(input("Please enter your age:\n"))
height = int(input("please enter your height in cm:\n"))

print("we are now checking if you are able to ride the rollercoaster!\n")

if height>120:
    print("You are tall enough to ride the rollercoaster!\n")
    if age<12:
        print("You are eligable for the childrens price of 5$!\n")
        price = 5
    elif age<18:
        print("You are eligable for the teen price of 7$!")
        price = 7
    elif age >= 18 and age >= 45 and age <= 55:
        print("You can ride for free")
        price = 0
    else:
        print("You have to pay the full price!")
        price = 12
    want_photo = input("Do you want a Photo of the ride afterwards?\n")
    if want_photo.casefold() == "yes":
        price+=3
    print(f"You have to pay {price}$!\n")
else:
    print("You need to be taller to be allowed on the rollercoaster!\n")

# logical operators

#and A and B have to be true for the overall to be true
#or: A or B can to be true or both for the overall to be true
#not