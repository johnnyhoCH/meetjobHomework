# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:13:17 2022

@author: user
"""

import random

play_again = None

while play_again != "N": 
    choice = ["rock","papper","scissors"]
    computer = random.choice(choice)
    player = input("rock,papper or scissors? \nPlayer: ").lower()
    print("Computer: ",computer)
    
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You Lost!")
        elif computer == "scissors":
            print("You win!")
    elif player == "papper":
        if computer == "scissors":
            print("You Lost!")
        elif computer == "rock":
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("You Lost!")
        elif computer == "papper":
            print("You win!")
    else:
        print("choose again!")
        
    play_again = input("play again? (Y/N)  ").upper()

else:
    print("Bye!!")
    