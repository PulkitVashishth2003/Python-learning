def max(x,y,z):
    if x >= y and x>= z:
        return x
    elif y >= z and y>= x:
        return y
    else :
        return z


## take multiple inputs from user and find maximum of three numbers
x,y,z = map(int,input("Enter three number:").split())
## calling out function to find max of 3
maxofthree = max(x,y,z)
## print the maximum number
print("The maximum of three numbers is:",maxofthree)