def get_valid_marks (subject):
    while True:
        try:
            mark = int(input(f"Enter marks for {subject}: "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100")
                continue
            return mark
        except ValueError:
            print("Invalid Input")

def calculate_grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 75:
        return "Grade B"
    elif percentage >= 60:
        return "Grade C"
    else:
        return "Fail"

students = []

num_students = int(input("How Many Students? "))
for i in range (num_students):
    print(f"\nEntering Details of Student {i+1}")


    student = {}
    student["Name"] = input("Enter Student Name: ")

    marks = []
    subjects = ["Math", "Science", "Urdu", "Social Studies", "English"]

    for subject in subjects:
        mark = get_valid_marks(subject)
        marks.append(mark)

    student["marks"] = marks

    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    student["total"] = total
    student["percentage"] = percentage
    student["grade"] = grade
    students.append(student)

print("\nFinal Results")
for student in students:
    print("----------------------")
    print("Name: ", student["Name"])
    print("Marks: ", student["marks"])
    print("Total: ", student["total"])
    print("Percentage: ", f"{student['percentage']:.2f}")
    print("Grade: ", student["grade"])