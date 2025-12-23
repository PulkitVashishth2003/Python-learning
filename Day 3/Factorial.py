number = int(input("enter the number whose factorial you want to find: "))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print("The factorial of ",number, "is",factorial)