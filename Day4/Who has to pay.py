import random

names = input("Please enter the names in the following Format:\n\nName1, Name2, ...\n\n")
s_names = names.split(", ")

ran_num = random.randint(0,len(s_names)-1)

print(f"{s_names[ran_num]} has to pay the bill!")
print(ran_num)
print(s_names)
print(len(s_names))
