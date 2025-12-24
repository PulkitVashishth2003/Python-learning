## function to check the string is palindrome/????
def palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        print(string, "is palindrome")
    else:
        print(string, "is not palindrome")
string = input("Enter a string: ")
## calling out the function to check palindrome
pal = palindrome(string)