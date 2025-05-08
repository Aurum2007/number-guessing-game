import random  # helps picking a random number
import time

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
    
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("Can you guess what it is?")

difficulty = input("\nChoose a difficulty. Type 'easy', 'medium' or 'hard': ")
start = int(time.time())

if difficulty.lower() == 'easy':
  print(f"You have chosen the {difficulty} mode. You have 10 attempts remaining to guess the number.\n")

  while attempts <= 10:
    guess = int(input("Make a guess: "))
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
      print(
          f"You have {10-attempts} attempts remaining to guess the number.\n")
    elif guess < num:
      locate_number(guess, num)
      attempts += 1
      print(
          f"You have {10-attempts} attempts remaining to guess the number.\n")

    if attempts == 10:
      print("You have run out of guesses, you lose.\n")

if difficulty.lower() == 'medium':
  print(
      f"You have chosen the {difficulty} mode. You have 5 attempts remaining to guess the number.\n"
  )

  while attempts <= 5:
    guess = int(input("Make a guess: "))
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
      print(f"You have {5-attempts} attempts remaining to guess the number.\n")
    elif guess < num:
      locate_number(guess, num)
      attempts += 1
      print(f"You have {5-attempts} attempts remaining to guess the number.\n")

    if attempts == 5:
      print("You have run out of guesses, you lose.")
      break

if difficulty.lower() == 'hard':
  print(f"You have chosen the {difficulty} mode. You have 3 attempts remaining to guess the number.\n")

  while attempts <= 3:
    guess = int(input("Make a guess: "))
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
      print(f"You have {3-attempts} attempts remaining to guess the number.\n")
    elif guess < num:
      locate_number(guess, num)
      attempts += 1
      print(f"You have {3-attempts} attempts remaining to guess the number.\n")

    if attempts == 3:
      print("You have run out of guesses, you lose.")
      break
