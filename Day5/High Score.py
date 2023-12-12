student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highscore = 0

for student in student_scores:
    if student > highscore:
        highscore = student
    else:
        print("continue")

print(f"the highest score is {highscore}!")