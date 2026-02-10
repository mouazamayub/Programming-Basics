def calculate_total(student_marks):
    total = 0
    for mark in student_marks:
        total += mark
    return total


marks = [
    [89, 90, 79, 80, 94],
    [76, 98, 80, 74, 87],
    [74, 88, 93, 92, 60]
]

student_no = 1

for student in marks:
    total = calculate_total(student)
    percentage = total / len(student)

    print("Student", student_no)
    print("Total:", total)
    print("Percentage:", percentage)
    print()

    student_no += 1
