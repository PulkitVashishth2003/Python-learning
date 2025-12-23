number = int(input("Enter the number upto whose sum you want :: "))
#by formula of sum of n natural numbers
sum = number*(number+1)/2
print("The sum of first", number, "numbers is :: ", sum," by formula")
#by use of loop 
sumloop = 0
for i in range(1,number+1):
    sumloop = sumloop + i
print("The sum of first", number, "numbers is :: ", sumloop," by loop")