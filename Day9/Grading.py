student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80 and student_scores[student] <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 70 and student_scores[student] <= 80:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Failed"

for student in student_grades:
  print(f"{student}: {student_grades[student]}\n")