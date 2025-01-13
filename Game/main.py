'''
==============================
LICENSE AND COPYRIGHT NOTICE
==============================

rock-paper-scissors-python
Copyright (C) 2024 vikalp-tyagi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For more information or to contact the author, please reach me at:
Email: vickyt.1309@gmail.com

See the GNU General Public License for more details:
Link: https://www.gnu.org/licenses/
'''

import random

# Instructions
print("WELCOME TO ROCK PAPER SCISSOR GAME")
print("\nHow To Play")
print(">> Enter either 'rock', 'paper' or 'scissor' as your choice")
print(">> Rock smashes scissor")
print(">> Paper covers rock")
print(">> Scissor cuts paper")

# Main code
while True:
    a = input("\nEnter a choice : ")
    c = ["rock", "paper", "scissor"]
    b = random.choice(c)
    
    if a.lower()=="rock" or a.lower()=="paper" or a.lower()=="scissor":
        print(f"\nYou choose {a.lower()}, computer chooses {b}...")
        if a.lower() == b:
            print(f"Both players selected {a}. It's a tie!")
        elif a.lower() == "rock":
            if b == "scissor":
                print("Rock smashes scissor! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif a.lower() == "paper":
            if b == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissor cuts paper! You lose.")
        elif a.lower() == "scissor":
            if b == "paper":
                print("Scissor cuts paper! You win!")
            else:
                print("Rock smashes scissor! You lose.")
    else:
        print('\nPlease enter either \'rock\', \'paper\' or \'scissor\'')
            
    d = input("\nPlay again? (y/n): ")
    if d.lower() != "y":
        break
