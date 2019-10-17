# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:39:06 2019

@author: diego
"""
from random import randint       
#create a list of play options
t = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]

#assign a random play to the computer
computer = t[randint(0,4)]

#set player to False
player = 0
c=0
j=0
p=0
def my_function(player):
    player = input("Rock, Paper, Scissors, Spock, Lizard? ")
    return player

def my_combat(player,computer,c,j,p):
        if player == computer:
            print("Tie!")
            j=j
            c=c
        elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                    c=c+1
                elif computer == "Spock":
                    print("You lose!", computer, "vaporizes", player)
                    c=c+1
                else:
                    print("You win!", player, "smashes", computer)
                    j=j+1
        elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                    c=c+1
                elif computer == "Lizard":
                    print("You lose!", computer, "eats", player)
                    c=c+1
                else:
                    print("You win!", player, "covers", computer)
                    j=j+1
        elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                    c=c+1
                elif computer == "Spock":
                    print("You lose...", computer, "smashes", player)
                    c=c+1
                else:
                    print("You win!", player, "cut", computer)
                    j=j+1
        elif player == "Lizard":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                    c=c+1
                elif computer == "Scissors":
                    print("You lose...", computer, "decapitate", player)
                    c=c+1
                else:
                    print("You win!", player, "cut", computer)
                    j=j+1
        elif player == "Spock":
                if computer == "Lizard":
                    print("You lose...", computer, "poison", player)
                    c=c+1
                elif computer == "Paper":
                    print("You lose...", computer, "disprove", player)
                    c=c+1
                else:
                    print("You win!", player, "cut", computer)
                    j=j+1
        else:
                    print("That's not a valid play. Check your spelling!")
                    p=p-1
        return c,j,p

p0 = input("Enter number of games: ")
p0 = int(p0)
h=[0,0,0]
while p<p0:
        player = my_function(player)
        h=my_combat(player,computer,c,j,p)
        p=h[2]+1
        c=h[0]
        j=h[1]
    #player was set to True, but we want it to be False so the loop continues
        computer = t[randint(0,4)]
        if j==(p0+1)/2:
            break
        elif c==(p0+1)/2:
            break
print("Player won", j)
print("Computer won", c)
print("Total number of games was", p)
if j>c:
    print("Player won more games")
elif c>j:
    print("Computer won more games")
else:
    print("Tie")
