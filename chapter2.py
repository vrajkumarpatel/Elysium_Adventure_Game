"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: chapter2.py
Purpose: Navigate the research deck with a locked corridor and an unconscious
         subject. Choose to search, wake, or bypass the lock, each affecting
         items and status for later chapters.
"""

from player import banner, divider, show_hud, choose, clear_screen, colorize, print_art


def run_chapter2(player):
    """Run Chapter 2 with the unconscious subject and corridor lock scenario.

    Returns:
        str: Identifier for the next chapter or an ending ("fail").
    """
    # Prepare visuals and show the subject art
    clear_screen()
    banner("Chapter 2 – Research Deck / Mind-Controlled Subject")
    print_art("subject.txt")
    print("The research deck is eerily silent—the faint rhythmic whirring of subject cells.")
    print("Objective: Reach the Main Lab beyond a locked corridor.")
    print("An unconscious, mind-controlled subject lies near the lock panel.")
    show_hud(player)
    divider("=")
    # Optional danger after repeated loops back to dock
    if player.loops_to_dock >= 3:
        print("Warning: Repeated returns have drawn attention—patrols are thicker here.")

    # Present choices around the subject and the locked corridor
    choice = choose([
        "Search the subject [gain keycard + note_gamma7; helps Ch3/Ch5]",
        "Wake the subject [alarmed if subdue; affects Ch3]",
        "Bypass the lock manually [gain bypassed_lock + swift; helps Ch4]",
        "Go back to the docking bay [loop to Ch1; suspicion after 3]",
    ])
    # Tip: press Q to quit from any menu
    if choice == "quit":
        print(colorize("Quitting game.", fg="yellow", bold=True))
        return "quit"

    # Choice 1: find a keycard and note, then proceed
    if choice == "1":
        player.has_keycard = True
        player.add_item("note_gamma7")
        print("\nYou find a keycard clipped under the subject's sleeve.")
        print("A torn note reads: 'Gamma-7 ... not in control...' You pocket it.")
        print("Keycard acquired. You badge through to the Main Lab.")
        return "chapter3"

    # Choice 2: wake the subject; subdue sets you to 'alarmed'
    if choice == "2":
        print("\nThe subject lunges with mechanical precision.")
        # A small sub-menu when the subject wakes up
        sub = choose([
            "Subdue the subject",
            "Hesitate",
        ])
        # Allow quitting here too
        if sub == "quit":
            print(colorize("Quitting game.", fg="yellow", bold=True))
            return "quit"
        if sub == "1":
            player.set_status("alarmed")
            print("\nYou restrain the subject and secure the area. Proceeding to the Main Lab.")
            return "chapter3"
        else:
            print("\nYou hesitate and the subject overpowers you.")
            print(colorize("FAIL: Fatal injuries sustained.", fg="red", bold=True))
            return "fail"

    # Choice 3: manually bypass the lock; blocked if too 'alarmed'
    if choice == "3":
        if player.status == "alarmed":
            print("You are too unstable to attempt this option.")
            return "chapter2"
        player.add_item("bypassed_lock")
        player.set_status("swift")
        print("\nYou bridge the circuit and bypass the lock. It cycles open quickly.")
        print("Status updated: swift.")
        return "chapter3"

    # Choice 4: loop back to Chapter 1 and increment suspicion counter
    print("\nYou return to the docking bay to reconsider your approach.")
    player.loops_to_dock += 1
    return "chapter1"
