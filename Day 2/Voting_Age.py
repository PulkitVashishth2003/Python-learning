Age = int(input("Enter your age: \n"))
try:
    if Age < 0:
        print("Age cannot be negative.")
    elif Age < 18:
        print("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a valid age.")