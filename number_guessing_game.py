import random  # helps picking a random number
import time

def play_game():
    num = random.randint(1, 100)
    attempts = 0

    def locate_number(guess, num):
        result  = abs(guess - num)
        if result >= 50:
            print("You are in the ARCTIC!!")
        elif result >= 10:
            print("You are freezing")
        elif result > 5 and result < 10:
            print("You are warmer")
        elif result > 3 and result <= 5:
            print("Your are hot")
        elif result > 1 and result <= 3:
            print("SMOOKING!!!")
        elif result <=1:
            print("THE SUN!!!")

    print("\nWelcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    difficulty = input("\nChoose a difficulty. Type 'easy', 'medium' or 'hard': ")
    start = int(time.time())

    if difficulty.lower() == 'easy':
        print(f"You have chosen the {difficulty} mode. You have 10 attempts remaining to guess the number.\n")
        max_attempts = 10
    elif difficulty.lower() == 'medium':
        print(f"You have chosen the {difficulty} mode. You have 5 attempts remaining to guess the number.\n")
        max_attempts = 5
    elif difficulty.lower() == "hard":
        print(f"You have chosen the {difficulty} mode. You have 3 attempts remaining to guess the number.\n")
        max_attempts = 3
    else:
        print("Invalid difficulty. Defaulting to medium")
        max_attempts = 5
        print(f"You have chosen the medium mode. You have 5 attempts remaining to guess the number.\n")
    
    while attempts <= max_attempts:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid Value")
            continue
        if guess == num:
            print(f"You got it! The answer was {num}.")
            attempts += 1
            print(f"You guessed in {attempts} attempts.")
            end = int(time.time())
            print(f"It took you {end - start} seconds")
            break
        elif guess > num:
            locate_number(guess, num)
            attempts += 1
            print(f"You have {max_attempts-attempts} attempts remaining to guess the number.\n")
        elif guess < num:
            locate_number(guess, num)
            attempts += 1
            print(f"You have {max_attempts-attempts} attempts remaining to guess the number.\n")
        if attempts == max_attempts:
            print("You have run out of guesses, you lose.")
            print(f"The number was {num}")
            break

while True:
    play_game()
    play_again = input("Do wou want to play again (yes or no): ")
    if play_again != "yes":
        print("Thanks for playing!")
        break
