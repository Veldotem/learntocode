print("Welcome to the Love Calculator, please follow the steps to see if you found your True Love.\n")

name1 = input("Please enter the first full name:")
name2 = input("please enter the second full name:")

low_name1 = name1.lower()
low_name2 = name2.lower()

c_name = low_name1+low_name2

t = c_name.count("t")
r = c_name.count("r")
u = c_name.count("u")
e = c_name.count("e")
l = c_name.count("l")
o = c_name.count("o")
v = c_name.count("v")
e = c_name.count("e")

digit1 = t+r+u+e
digit2 = l+o+v+e

score = int(str(digit1) + str(digit2))

if score <=10 or score >=90:
    print(f"Your score is {score}. You will go together like Mentos and Cola")
elif score >40 and score <50:
    print(f"Your score is {score}. You are alright together")
else:
    print(f"Your score is {score}.")


print(type(score))
