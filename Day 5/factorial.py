## function to calculate factorial using recursion
def factorial(n):
    if n==0 or n==1:
           return 1
    else:
        return n* factorial(n-1)
## taking input for factorial calculation
number = int(input("Enter a number to find its factorial: "))
## checking if factotial number is needed to calculate
if number<0:
        print("Factorial is not defined for negative numbers.")
else:
        factorialnumber = factorial(number)
        print ("Factorial of", number, "is", factorialnumber)