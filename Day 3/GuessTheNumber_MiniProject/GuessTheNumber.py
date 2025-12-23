import random
print("Welcome to 'Guess The Number' game!")
number_to_guess = random.randint(1,100)
attempts = 0
while True:
    user_guess = int(input("Please enter your guess (between 1 and 100):"))
#### logic building 
    try:
        attempts +=1
        if user_guess == number_to_guess:
            print("Congratulations! It is correct!")
            print("You took ", attempts, " attempt to guess", number_to_guess)
            break
        elif user_guess < number_to_guess:
            print("your guess is too low. Try again!")
        else:
            print("your guess is too high. Try again!")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
