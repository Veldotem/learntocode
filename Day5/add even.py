target=int(input("please enter the target number:\n"))
total_even = 0
total_odd = 0
for number in range(1, target+1):
    if number % 2 == 0:
        total_even += number
    else:
        total_odd += number

print(f"the total even is {total_even}\n2the total odd is {total_odd}")