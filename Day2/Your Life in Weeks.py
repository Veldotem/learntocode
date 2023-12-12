print("welcome to the weeks left calculator!\n\n")
age = input("please enter you Age:\n")
print(type(age))
weeks_lived = int(age)*52
weeks_left= 4680-weeks_lived
print(f"You have {weeks_left} weeks left")