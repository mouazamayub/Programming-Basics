marks = [50,94,45,67]
print("Total Students:",len(marks))

marks.insert(2,79)
print("After Insert:",marks)
print("Total Students:",len(marks))

removed = marks.pop()
print("Removed:",removed)
print("Now:",marks)

marks.sort()
print("Sorted:",marks)