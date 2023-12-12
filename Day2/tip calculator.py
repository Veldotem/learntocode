print("Welcome to the Tip calculator")
total_amount = input("\nPlease enter the total amount you paide today (use . to seperate decimals):\n")
people = input("\nHow many people attended the Meal?\n")
tip = input("\nHow much do you want to tip?\n")

total_amount_f = float(total_amount)
people_int = int(people)
tip_int = int(tip)

amount_w_tip =round(total_amount_f+(total_amount_f*(tip_int/100)),2)
amount_pp = round(amount_w_tip/people_int,2)
rest = round(amount_w_tip - (amount_pp*people_int),2)
print(f"the total amount including Tip is {amount_w_tip}€\nThis means everyone has to pay {amount_pp}€\nDividing equaly leavs a rest of {rest}€ to reach the total amount including tip")

print(type(total_amount_f))
print(type(people_int))
print(type(tip_int))