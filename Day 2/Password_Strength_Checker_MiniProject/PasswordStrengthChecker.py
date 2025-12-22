passcode = input("Enter your password: ")
length = len(passcode)
# check for length
if length < 8:
    print("Weak password: Password must be at least 8 characters long.")
else:
    print("Length condition fulfilled.")
# check for special character
has_special = any(not char.isalnum() for char in passcode)
if has_special == False:
    print("Weak password: Password must contain at least one special character.")
else:
    print("Special character condition fulfilled.")
# check for upper case, lower case and numerical characters
has_upper = any(char.isupper() for char in passcode)
if has_upper == False:
    print("Weak password: Password must contain at least one Upper Case Alphabet.")
else:
    print("Upper Case Aplhabet condition fulfilled.")
has_lower = any(char.islower() for char in passcode)
if has_lower == False:
    print("Weak password: Password must contain at least one Lower Case Alphabet.")
else:
    print("Lower Case Alphabet condition fulfilled.")
has_num   = any(char.isdigit() for char in passcode)
if has_num == False:
    print("Weak password: Password must contain at least one numerical character.")
else:
    print("Numerical character condition fulfilled.")

# gives final result
if (length >= 8) and has_special and has_upper and has_lower and has_num:
    print("\nStrong password!\n")  
else:
    print("\nPlease try again to create a strong password.\n")