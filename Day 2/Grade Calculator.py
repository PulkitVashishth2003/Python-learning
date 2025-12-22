try:
    number = int(input("Enter the number of grades you want to input: "))
    if number >= 90:
        print("A")
    elif 90 <= number >= 80:
        print("B")
    elif 80 <= number >= 70:
        print("C")
    elif 70 <= number >= 60:    
        print("D")
    elif number < 60:
        print("F")
except ValueError:
    print("Invalid input. Please enter a numerical grade.")