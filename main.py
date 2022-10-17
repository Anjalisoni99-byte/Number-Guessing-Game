from art import logo
import random
easy_attempts = 10
hard_attempts = 5

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_attempts
  else:
    return hard_attempts

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  flag=True
  while flag:
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            turns = check_answer(guess, answer, turns)
            if turns == 0:
                print("You've run out of guesses, you lose.")
                return
            elif guess != answer:
                print("Guess again.")
    ans=input("Do you want to play again? Type yes or no")
    if ans=='no':
        flag=False
        break
  print("Thank you for playing !!")

game()

