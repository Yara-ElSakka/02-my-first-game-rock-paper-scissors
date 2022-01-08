# Yara's first game in Python
# rock, paper, scissors Game :)
# 29.11.2021

# my magic
from random import *

# my variables:
gameOptions = ["rock", "paper", "scissors"]
playerAnswer = input("Let's Play!\nPlease choose one of the options:\nrock, paper or scissors?\n")
computerAnswer = choice(gameOptions)

# print out the answers
print(f"Your choice: {playerAnswer}\nComputer choice: {computerAnswer}\n")

# check who is the winner
# case 1: if both have the same answer:
if computerAnswer == playerAnswer:
    print("it is a tie !!!")

# case 2: if player choose rock:
if playerAnswer == "rock" and computerAnswer == "scissors":
    print("Congrats !!! You WON !!!")

if playerAnswer == "rock" and computerAnswer == "paper":
    print("sorry !!! You LOST !!!")

# case 3: if player choose paper:
if playerAnswer == "paper" and computerAnswer == "rock":
    print("Congrats !!! You WON !!!")

if playerAnswer == "paper" and computerAnswer == "scissors":
    print("sorry !!! You LOST !!!")

# case 4: if player choose scissors:
if playerAnswer == "scissors" and computerAnswer == "paper":
    print("Congrats !!! You WON !!!")

if playerAnswer == "scissors" and computerAnswer == "rock":
    print("sorry !!! You LOST !!!")

# case 5: if player choose something not in the list:

if playerAnswer == "yara":
    print("yara is the developer of this game but choose something else please ")

if playerAnswer != "scissors" and playerAnswer != "rock" and playerAnswer != "paper" and playerAnswer != "yara":
    print("Please !!! Choose only: rock, paper or scissors !!!")

# end of code