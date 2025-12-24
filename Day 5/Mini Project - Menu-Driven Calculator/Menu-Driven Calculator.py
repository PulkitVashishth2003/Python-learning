def add(x,y):
        return x+y
def subtract(x,y):
        return x-y
def multiply(x,y):
        return x*y
def divide(x,y):
        return x/y
def power (x,y):
        return x**y
def modulas (x,y):
        return x%y 


while True:
    choice = int(input("Menu :\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5. Power\n6.Modulas\nEnter your choice (1-6): "))
    if choice == 1:
            a,b = map (int, input("Enter two numbers: \n").split())
            answer = add(a,b)
            print("Addition =", answer)
    elif choice == 2:
            a,b = map (int, input("Enter two numbers: \n").split())
            answer = subtract(a,b)
            print("Subtraction =", answer)
    elif choice == 3:
            a,b = map (int, input("Enter two numbers: \n").split())
            answer = multiply(a,b)
            print("Multiplication =", answer)
    elif choice == 4:
            a,b = map (int, input("Enter two numbers: \n").split())
            answer = divide(a,b)
            print("Division =", answer)
    elif choice == 5:
            a,b = map (int, input("Enter two numbers: \n").split())
            answer = power(a,b)
            print("Power =", answer)
    elif choice == 6:
            a,b = map (int, input("Enter two numbers: \n").split())
            answer = modulas(a,b)
            print("Modulas =", answer)
    else:
            print("Invalid choice")
            break