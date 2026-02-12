student = {
    "name":"Ali",
    "marks":[80, 75, 90],
}
total = 0
for mark in student["marks"]:
    total += mark
percentage = total / len(student["marks"])
print("Name: ",student["name"])
print("Total: ",total)
print("Percentage: ",percentage)
