"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: main.py
Purpose: Starts the game, asks for the player's name, and runs chapters
         in sequence. Shows the title art and uses a loop to move between
         chapters until you win or the mission ends.
"""

from player import Player, banner, divider, clear_screen, print_art
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5


def main():
    """Entry point: create player and run chapter sequence until win/fail."""
    # Clear the screen and show the title/banner to start the game
    clear_screen()
    banner("Elysium Station – Sci-Fi Adventure Game")
    print_art("title.txt")  # prints ASCII art from assets/title.txt if present
    print("Tip: Enter the number of your choice at each step.")
    divider("=")
    # Ask for a name and require at least one character
    # Ask the player for a name and make sure it's not empty
    name = input("Enter your investigator name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter your investigator name: ").strip()

    # Make the Player object with the chosen name
    # Create the Player object to track inventory, status, and flags
    player = Player(name=name)

    # Map chapter identifiers to their run functions.
    # Map available chapter names to their run functions
    # Map chapter names to their run functions so we can jump between them
    chapters = {
        "chapter1": chapter1.run_chapter1,
        "chapter2": chapter2.run_chapter2,
        "chapter3": chapter3.run_chapter3,
        "chapter4": chapter4.run_chapter4,
        "chapter5": chapter5.run_chapter5,
    }

    # Start at chapter 1 and keep going until a final result is returned
    # Start at Chapter 1 and loop until a final result comes back
    current = "chapter1"
    while True:
        next_id = chapters[current](player)  # run the current chapter
        if next_id in chapters:
            # Move to the next chapter by its id
            current = next_id
            continue
        elif next_id == "win":
            # Player reached a winning ending
            print("\nMission complete. Congratulations, Investigator!")
            break
        elif next_id == "fail":
            # Player reached a failing ending
            print("\nMission failed. Better luck next time.")
            break
        elif next_id == "quit":
            # Player chose to quit from a chapter menu
            print("\nExiting game. Goodbye.")
            break
        else:
            # If a chapter returns something unexpected, end the game safely
            print(f"\nUnexpected chapter id '{next_id}'. Ending game.")
            break


if __name__ == "__main__":
    main()
