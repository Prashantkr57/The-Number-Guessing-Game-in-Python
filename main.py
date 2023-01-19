import random

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
my_num = random.randint(1, 100)

def is_match(mnum, gnum):
  if mnum > gnum:
    return 1
    
  elif gnum > mnum:
    return -1
    
  elif gnum == mnum:
    return 0
    

difficulty_level = input("Chose a difficulty. Type 'easy'or 'hard': ")

if difficulty_level == 'easy':
  attempt_remaining = 10
else:
  attempt_remaining = 5

while attempt_remaining != 0:
  print(f"You have {attempt_remaining} attempts remaining to guess the number.")
  print(my_num)
  guess_num = int(input("Make a guess: "))
  attempt_remaining -= 1
  match_check = is_match(my_num, guess_num)
  if match_check == 1:
    print("Too Low!")
    print("Guess Again")

  elif match_check == -1:
    print("Too High!")
    print("Guess Again")

  elif match_check == 0:
    print("You Guessed it right!")
    attempt_remaining = 0
  
  