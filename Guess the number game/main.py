#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,number, turns):
  """Checks answer against guess. Returns the number of turns remaining"""
  if guess > number:
    print("Too high. ")
    return (turns-1)
  elif guess < number:
    print("Too Low")
    return (turns-1)
  elif guess == number:
    print(f"You got it! The answer is {number}")

def set_difficulty():
  difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return(EASY_LEVEL_TURNS)
  else:
    return(HARD_LEVEL_TURNS)

def game():
  #Choose a random number between 1 and 100
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number betwen 1 and 100.")
  number = randint(1,100)

  turns = set_difficulty()
  

  guess = 0
  while guess != number: 
    print(f"You have {turns} attempts remaining to guess the number")
    #Let the user guess a number
    guess = int(input("Guess a number: "))
    turns = check_answer(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    

game()  