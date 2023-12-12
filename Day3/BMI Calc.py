height = input("please enter your heigt\n")
mass = input("please enter your body weight\n")

weight = int(mass)
height_float = float(height)

bmi = weight / height_float ** 2

if bmi <18:
    print(f"Your BMI is {bmi}. This means you are underweight. You should change your dietary plan!\n")
elif bmi<25:
    print(f"Your BMI is {bmi}. You are in the norm. Stay in shape you are looking good!\n")
elif bmi<30:
    print(f"Your BMI is {bmi}. You could loose some weight but still looking good!\n")
elif bmi<40:
    print(f"Your BMI is {bmi}. You should loose some weight to lower your BMI and live a healthy life!\n")
else:
    print(f"Your BMI is {bmi}. 170You should really losse weight to get into a healthy lifestyle.\nPlease visit a doctor to make the transition as healthy for you as possible.\n")
