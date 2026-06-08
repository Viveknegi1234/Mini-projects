## PYTHON -##

## EXAMPLE- ( ROCK , PAPER , SCISSORS) - ##
import random  

def get_choices():                                                    ## (def get_choice(): is function)##
 player_choice = input("Enter a choice( rock,paper,scissors ):")       ## (player_name = variable)##
 options = ["rock","paper","scissors"]
 computer_choice =  random.choice(options)                            ##(used random for make choices random )##
 choices = {"player": player_choice , "computer": computer_choice }
 return choices

def check_win(player, computer):
 print(f"You choose {player} , computer choose {computer}")
 if (player == computer):
  return "it's a tie"
 elif (player == "rock" and computer == "scissors"):
  return " rock smasher scissors ! You win hurray! "
 elif (player == "rock" and computer == "paper"):
  return " paper coveres rock  ! You loose faaahh! "
 
 elif (player == "paper" and computer == "scissors"):
  return " paper cut by  scissors ! You loose faaahh! "
 elif (player == "paper" and computer == "rock"):
  return " paper coveres rock  ! You win hurray! "

 elif (player == "scissors" and computer == "rock"):
  return " rock smasher scissors ! You loose faaahhh! "
 elif (player == "scissors" and computer == "paper"):
  return " scissors cut paper  ! You win hurray! "
 
 
choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)