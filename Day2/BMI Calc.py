height = input("please enter your heigt\n")
mass = input("please enter your body weight\n")

weight = int(mass)
height_float = float(height)

bmi = weight / height_float ** 2

bmi_int = str(bmi)

print("your BMI is: " + bmi_int)