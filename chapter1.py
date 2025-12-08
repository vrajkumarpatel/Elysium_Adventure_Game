"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: chapter1.py
Purpose: Introduces the station and lets the player gather intel, hack a
         terminal, or sneak through maintenance shafts. Choices influence
         later chapters through items and status changes.
"""

from player import banner, divider, show_hud, choose, clear_screen, colorize, print_art


def hack_puzzle() -> bool:
    # Small two-step puzzle to simulate hacking for a temporary pass
    banner("Terminal Hack Puzzle")
    print("Solve two quick steps to obtain a temporary pass.")
    divider("-")
    print("Step 1: Reverse the code string exactly.")
    print("Code: A7-2B")
    ans1 = input("Enter reversed: ").strip()
    correct1 = "B2-7A"
    if ans1 != correct1:
        print("Incorrect reversal.")
        return False
    divider("-")
    print("Step 2: Enter the sum of digits shown.")
    print("Digits: 8, 1, 6")
    ans2 = input("Enter total: ").strip()
    if ans2 != "15":
        print("Incorrect total.")
        return False
    print("Access challenge completed.")
    return True


def run_chapter1(player):
    """Run Chapter 1 with clear visuals and simple choices.

    Returns:
        str: Identifier for the next chapter or an ending ("fail").
    """
    # Prepare the screen and show chapter visuals
    clear_screen()
    banner("Chapter 1 – Enter Elysium Station")
    print_art("station.txt")
    print("The cold void of space contrasts with the buzzing neon of the docking bay.")
    print("Your mission timer starts now.")
    divider("=")
    print("Objective: Infiltrate the station quietly.")
    print("How to play: Enter the number of your choice and press Enter.")
    show_hud(player)

    # Present the main choices for Chapter 1
    choice = choose([
        "Talk to dock workers [gain patrol_routes; helps Ch4, Ch5]",
        "Hack a terminal [keycard if solve; flagged; affects Ch3/Ch4]",
        "Search for a maintenance shaft [status stealth; helps Ch4]",
        "Return to shuttle bay [mission ends]",
    ])
    # Tip: you can press Q to quit at any selection screen
    if choice == "quit":
        print(colorize("Quitting game.", fg="yellow", bold=True))
        return "quit"
    if choice == "quit":
        print(colorize("Quitting game.", fg="yellow", bold=True))
        return "quit"

    # Choice 1: gain patrol routes and go undercover
    if choice == "1":
        # Gather intel; improves clarity for later choices.
        player.add_item("patrol_routes")
        player.set_status("undercover")
        print("\nDock workers share patrol timing and routes. You note quiet windows.")
        print("Intel added: patrol routes.")
        print("Bonus: If undercover, the Mastermind may hesitate later.")
        return "chapter2"

    # Choice 2: attempt a terminal hack to print a keycard
    if choice == "2":
        print("\nYou approach a public terminal to spoof credentials.")
        success = hack_puzzle()
        if success:
            player.has_keycard = True
            player.set_status("flagged")
            print("Temporary pass printed. Status updated: flagged. Keycard acquired.")
            print("A silent alarm logs your presence. This may affect later chapters.")
            return "chapter2"
        else:
            player.set_status("compromised")
            print("Access attempt logged. No pass issued. Status updated: compromised.")
            print("A drone briefly scans your position before moving on.")
            return "chapter2"

    # Choice 3: take the maintenance route to become stealthy
    if choice == "3":
        player.set_status("stealth")
        print("\nYou slip into a narrow maintenance shaft toward research levels.")
        print("Status updated: stealth.")
        return "chapter2"

    # Choice 4: leave the mission early (ends the story here)
    print("\nYou step back into the shuttle bay. The station's neon fades to cold metal.")
    print("Corporate investigators replace you. The theft spirals into cover-ups.")
    print(colorize("GAME OVER", fg="red", bold=True))
    return "fail"
