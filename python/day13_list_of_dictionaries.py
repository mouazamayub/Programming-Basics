students = [
    {
        "name": "Ali",
        "age": 21,
        "marks": [90, 87, 92, 85, 78]
    },
    {
        "name": "Ahmed",
        "age": 20,
        "marks": [97, 76, 89, 92, 96]
    },
    {
        "name": "Zara",
        "age": 21,
        "marks": [91, 97, 95, 89, 90]
    }
]
for student in students:
    total = sum(student["marks"])
    percentage = total / len(student["marks"])

    print("Name: ",student["name"])
    print("Age: ",student["age"])
    print("Total Marks: ", total)
    print("Percentage: ", percentage)
    print()