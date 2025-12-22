number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = number_1 + number_2
    print ("Additiction is : ", result)
elif operation == "-":
    result = number_1 - number_2
    print ("Subtraction is : ", result)
elif operation == "*":
    result = number_1 * number_2
    print ("Multiplication is : ", result)
elif operation == "/":
    if number_2 != 0:
        result = number_1 / number_2
        print ("Division is : ", result)
    else:
        print("Error: Division by zero is not allowed.")    