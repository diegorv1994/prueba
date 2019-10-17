# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:33:48 2019

@author: diego
"""

# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
import random

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.
lis=['stone','paper','scissors']

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...
x=5

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games
w=3

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.
def my_function(lis):
  return random.choice(lis)

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.
def my_election(x): 
    x = input ("Enter stone, paper or scissors: ")
    y = 0
    while y<1:
        if x in lis:
            y=y+1
        else:
            print('Invalid entry enter stone, paper or scissors')
            x = input ("Enter stone, paper or scissors: ")
    return x

# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
def combat(x,y): 
    if my_election(x) == my_function(y):
        print("tie")
    
# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated

    
# Create two variables that accumulate the wins of each participant


# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.

    
# Print by console the winner of the game based on who has more accumulated wins
          
          
# An input is requested and stored in a variable
#test_text = input ("Enter a number: ")

# Converts the string into a integer. If you need
# to convert the user input into decimal format,
# the float() function is used instead of int()
#test_number = int(test_text)

# Prints in the console the variable as requested
#print ("The number you entered is: ", test_number)
        
from random import randint       
#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = 0
c=0
j=0
p=0

#set player to True
p0 = input("Enter number of games: ")
p0 = int(p0)
while p<p0:
        player = input("Rock, Paper, Scissors?")
        p=p+1
        if player == computer:
            print("Tie!")
            j=j
            c=c
        elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                    c=c+1
                else:
                    print("You win!", player, "smashes", computer)
                    j=j+1
        elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                    c=c+1
                else:
                    print("You win!", player, "covers", computer)
                    j=j+1
        elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                    c=c+1
                else:
                    print("You win!", player, "cut", computer)
                    j=j+1
        else:
                    print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
        computer = t[randint(0,2)]
        if j==(p0+1)/2:
            break
        elif c==(p0+1)/2:
            break
if j>c:
    print("Player won")
elif c>j:
    print("Computer won")
else:
    print("Tie")
        