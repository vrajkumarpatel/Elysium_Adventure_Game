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
    clear_screen()
    banner("Elysium Station – Sci-Fi Adventure Game")
    print_art("title.txt")
    print("Tip: Enter the number of your choice at each step.")
    divider("=")
    # Ask for a name and require at least one character
    name = input("Enter your investigator name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter your investigator name: ").strip()

    # Make the Player object with the chosen name
    player = Player(name=name)

    # Map chapter identifiers to their run functions.
    # Map available chapter names to their run functions
    chapters = {
        "chapter1": chapter1.run_chapter1,
        "chapter2": chapter2.run_chapter2,
        "chapter3": chapter3.run_chapter3,
        "chapter4": chapter4.run_chapter4,
        "chapter5": chapter5.run_chapter5,
    }

    # Start at chapter 1 and keep going until a final result is returned
    current = "chapter1"
    while True:
        next_id = chapters[current](player)
        if next_id in chapters:
            current = next_id
            continue
        elif next_id == "win":
            print("\nMission complete. Congratulations, Investigator!")
            break
        elif next_id == "fail":
            print("\nMission failed. Better luck next time.")
            break
        else:
            # Defensive fallback if a chapter returns an unexpected identifier.
            print(f"\nUnexpected chapter id '{next_id}'. Ending game.")
            break


if __name__ == "__main__":
    main()
