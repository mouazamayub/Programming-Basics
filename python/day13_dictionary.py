student = {
    "name":str(input("enter")),
    "marks":int(input("enter marks")),
}
total = 0
for mark in student["marks"]:
    total += mark
percentage = total / len(student["marks"])
print("Name: ",student["name"])
print("Total: ",total)
print("Percentage: ",percentage)
