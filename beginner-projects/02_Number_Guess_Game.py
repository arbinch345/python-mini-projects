import random

number = random.randint(1, 50)
print(number)
attempts = 5
is_running = True

while is_running:
    guess = int(input("Guess the number: "))

    if guess > 50:
        print("Limit Exceed! The number should be less than 50!")
    
    elif guess == number:
        print(f"You got it! The number is {number}")
        break

    elif guess > number:
        print("Guess lower!")
    
    elif guess < number:
        print("Guess High!")

    else:
        print("Try again!")   

    attempts -= 1

    print(f"Guessing reamins: {attempts}")

    if attempts == 0:
        print("Attempts finished!")
        print(f"The number was {number}")
        break

print("Thanks for playing!")