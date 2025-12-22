try:
    number = int(input("Enter the number to find : \n"))
    if number == 0:
        print("thr number is equal to zero")
    elif number < 0:
        print("the number is less than zero and negative")
    elif number > 0:
        print("the number is greater than zero and postive")
except ValueError:
        print("invalid outcome")