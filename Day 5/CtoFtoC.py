## function to convert celcius to fahrehient
def CtoF(celsius):
    return (celsius*9.0/5.0) + 32
# function to convert fahrehient to celcius
def FtoC(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

## enter cjoice to perfrom action
choice = int(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius: \n"))
## convert celcius to fahrehient
if choice == 1:
    temp = float(input("\nEnter temperature in Celsius: \n"))
    fahrenheit = CtoF(temp)
    print (temp, "Celcius temprature is ", fahrenheit, "in Fahrenheit")
## convert fahrehient to celcius
elif choice == 2:
    temp = float(input("\nEnter temperature in Fahrenheit: \n"))
    celsius = FtoC(temp)
    print (temp, "Fahrenheit temprature is ", celsius, "in Celsius")
else:
    print("Invalid choice. Please enter 1 or 2.")