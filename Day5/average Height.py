student_heights = [156, 187, 193, 176, 173, 167, 145, 168, 175, 184, 186, 186]
total_height = 0
average_height = 0
num_students = 0

for student in student_heights:
    total_height += student
    num_students += 1

avg_height = total_height/num_students
print(f"total height: {total_height}")
print(f"number of Students: {num_students}")
print(f"Average Height: {avg_height}cm")

