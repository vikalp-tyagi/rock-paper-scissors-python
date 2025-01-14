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
def instructions():
    """Displays game instructions."""
    
    instructions=[
    "WELCOME TO ROCK PAPER SCISSOR GAME",
    "\nHow To Play",
    ">> Enter either 'rock', 'paper', or 'scissor' as your choice",
    ">> Rock smashes scissor",
    ">> Scissor cuts paper",
    ]

    for instruction in instructions:
        print(instruction)

# Main code
choices = ["rock", "paper", "scissor"]
win_conditions = {
    "rock": "scissor",  # Rock beats Scissor
    "paper": "rock",    # Paper beats Rock
    "scissor": "paper", # Scissor beats Paper
}

def play_game():
    """Main function to play the game."""
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissor): ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose from 'rock', 'paper', or 'scissor'.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif win_conditions[user_choice] == computer_choice:
            print(f"{user_choice.capitalize()} beats {computer_choice}. You win!")
        else:
            print(f"{computer_choice.capitalize()} beats {user_choice}. You lose!")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nThanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    instructions()
    play_game()
