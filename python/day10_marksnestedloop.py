student_no=1

marks = [
    [89,90,79,80,94],         # Student 1
    [76,98,80,74,87],         # Student 2
    [74,88,93,92,60]          # Student 3
]
for student in marks:
    total = 0
    for score in student:
        total += score
    print("Student ",student_no)
    print("Total:", total)
    percentage = total/len(student)
    print("Percentage:", percentage)
    print()
    student_no +=1
