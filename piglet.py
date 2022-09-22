"""
Write a console program that implements a simple 1-player dice game called "Piglet" (based on the game "Pig"). The player's goal is to accumulate as many points as possible without rolling a 1. Each turn, the player rolls the die if they roll a 1, the game ends and they get a score of 0. Otherwise, they add this number to their running total score. The player then chooses whether to roll again, or end the game with their current pototal. Here is an example dialogue where the user plays until rolling a 1, which ends the game with 0 points:

Welcome to Piglet!
You rolled a 5
Roll again? yes
You rolled a 4
Roll again? yes
You rolled a 1
You got 0 points.
Here is another example dialogue where the user stops early and gets to end the game with 10 points:

Welcome to Piglet!
You rolled a 6
Roll again? y
You rolled a 2
Roll again? y
You rolled a 2
Roll again? n
You got 10 points.
"""
def piglet():
  print("Welcome to Piglet!")
  randomNum=random.randint(0,10)
  print("You rolled a",randomNum)
  if(randomNum==1):
      print("You got",0,"points")
  sum=randomNum
  while True:
      randomNum1 =random.choice([1, 2, 3, 4, 5, 6])
      answer=input("Roll again? ")
      if answer=="yes" or answer=="y":
          print("You rolled a",randomNum1)
          sum+=randomNum1
          if randomNum1==1:
              print("You got 0 points.")
              break
      else:
          print("You got",sum,"points.")
          break
