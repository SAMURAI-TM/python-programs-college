
# Program to print day of the week based on number input


number = int(input("Enter a number (1 to 7): "))


if number == 1:
    print("Sunday")
elif number == 2:
    print("Monday")
elif number == 3:
    print("Tuesday")
elif number == 4:
    print("Wednesday")
elif number == 5:
    print("Thursday")
elif number == 6:
    print("Friday")
elif number == 7:
    print("Saturday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
