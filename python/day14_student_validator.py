def get_valid_marks(subject):
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
    if percentage >=90:
        return "Grade A"
    elif percentage >= 75:
        return "Grade B"
    elif percentage >= 60:
        return "Grade C"
    else:
        return "Fail"
    
student = {}
student["Name"] = input("Enter Students Name: ")

marks = []
subjects = ["Math", "Science", "Urdu"]
for subject in subjects:
    mark = get_valid_marks(subject)
    marks.append(mark)
student["marks"] = marks

total = 0
total += mark
total = sum(marks)

percentage = total / len(marks)
grade = calculate_grade(percentage)

print("\n Student Result")
print("Name: ",student["Name"])
print("Marks: ",student["marks"])
print("Total: ", total)
print("Percentage: ", f"{percentage:.2f}")
print("Grade: ",grade)