
size = input("Welcome to Python Pizza, what size should your Pizza be?\small edium ore large?\n")
e_pep = input("Do you want extra peperoni on the Pizza?")
e_che = input("Do you want extra cheese on top?")

if size.casefold()=="small":
    price = 15
elif size.casefold()=="medium":
    price = 20
elif size.casefold()=="large":
    price=25

if e_pep.casefold()=="yes":
    if size.casefold()=="small":
        price+=2
    else:
        price+=3

if e_che.casefold()=="yes":
    price+=1

print(f"Your total for the Pizza will be {price}$!")