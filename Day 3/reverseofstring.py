string = input("Enter the string: ")
#reversing the string by loop
stringlength = len(string)
reversestring = ""
for i in range(stringlength,0,-1):
    reversestring = reversestring + string[i-1]
print("Reversed string is:",reversestring)