def student_result (student_marks):
    total = sum (student_marks)
    percentage = total / len(student_marks)
    return total, percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"
marks = [
    [90,87,75,89,92],
    [91,99,90,97,95],
    [94,76,77,85,98]
]

student_no = 1
for student in marks:
    total, percentage = student_result(student)
    grade = calculate_grade(percentage)
    print("Student", student_no)
    print("Total: ", total)
    print("Percentage: ", percentage)
    print("Grade: ", grade)
    print()
    student_no += 1
