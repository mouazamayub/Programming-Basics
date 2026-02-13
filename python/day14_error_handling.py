while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid Input! Please enter a valid number.")
print("Valid Number: ",number)
