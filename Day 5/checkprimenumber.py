## function that perform prime checking
def primenumber(number):
    if number>1:
        for i in range(2,number):
            if(number%i==0):
                return 0
        return 1
    elif number == 1:
        return 0
    else:
        return -1
## take number as input for checking
number = int(input("Enter a number: "))

## call function by giving number as argument
checkprime = primenumber(number)
if checkprime ==1:
    print(number," is a prime number.")
elif checkprime == 0:
    print(number, " is not prime nnumber")
else:
    print("invalid input")


