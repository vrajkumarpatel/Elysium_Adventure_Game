"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: chapter5.py
Purpose: Final confrontation at the Escape Pod Bay. Decide to fight, use the
         control device, surrender, or attempt escape without the Regulator.
         Outcomes determine whether you win or the mission ends.
"""

from player import banner, divider, show_hud, choose, clear_screen, colorize, print_art


def run_chapter5(player):
    """Run Chapter 5 with a clear checklist for escape."""
    # Prepare visuals and show pod bay art
    clear_screen()
    banner("Chapter 5 – Confrontation at Escape Pod Bay")
    print_art("podbay.txt")
    print("The escape pod bay is small: Gamma-7 clutches the Regulator; the Mastermind waits.")
    print("Objective: Escape before corporate security arrives.")
    show_hud(player)
    divider("=")

    print("You arrive at the Escape Pod Bay. Subject Gamma-7 clutches the Core Regulator.")
    print("The true Mastermind watches, ready to flee.")
    # Present final decision options for the confrontation
    choice = choose([
        "Fight the Mastermind [gain regulator; WIN]",
        "Use the control device on Gamma-7 [requires control_device; BEST WIN]",
        "Surrender to the Mastermind [you are framed]",
        "Attempt to escape without the Regulator [special scene if undercover+patrol_routes]",
    ])
    # Press Q to quit if you don't want to continue
    if choice == "quit":
        print(colorize("Quitting game.", fg="yellow", bold=True))
        return "quit"

    # Choice 1: fight to secure the Regulator and win
    if choice == "1":
        if player.status == "alarmed":
            print("\nYou engage the Mastermind. The fight is tense under lockdown pressure.")
        elif player.status == "undercover":
            print("\nYou step forward confidently. The Mastermind hesitates, misreading your cover.")
        else:
            print("\nYou engage the Mastermind. A precise strike disarms them.")
        player.has_regulator = True
        print("You seize the Core Regulator and launch an escape pod.")
        print(colorize("WIN: You escaped Elysium with the Regulator and exposed the plot.", fg="green", bold=True))
        return "win"

    # Choice 2: use control device for a best outcome (checks apply)
    if choice == "2":
        if player.status == "alarmed":
            print("You are too unstable to attempt this option.")
            return "chapter5"
        if not player.control_device:
            print("You lack the device to attempt this.")
            return "chapter5"
        if player.has_item("control_device") or player.control_device:
            player.has_regulator = True
            print("\nYou pulse the device. Gamma-7 blinks free of control and turns on the Mastermind.")
            print("With the Regulator secured, you board an escape pod and launch.")
            if player.flags.get("identified_gamma7"):
                print("Gamma-7: 'You saw me for who I was—thank you.'")
            print(colorize("WIN: You freed Gamma-7 and escaped with the Regulator.", fg="green", bold=True))
            return "win"
        print("\nYou fumble without the control device. Gamma-7 remains controlled.")
        print(colorize("FAIL: The Mastermind escapes while security detains you.", fg="red", bold=True))
        return "fail"

    # Choice 3: surrender leads to a framed ending
    if choice == "3":
        print("\nYou surrender. The Mastermind frames you and launches a pod.")
        print(colorize("FAIL: You're left to take the blame.", fg="red", bold=True))
        return "fail"

    # Choice 4: escape attempt without the Regulator (fails)
    print("\nYou try to escape without the Regulator.")
    if player.status == "undercover" and player.has_item("patrol_routes"):
        print("You use patrol intel to time your move, but a final lock halts you.")
        print(colorize("FAIL: You nearly escape, but security captures you as the pod seals.", fg="red", bold=True))
    else:
        print(colorize("FAIL: Security captures you; the Mastermind gets away.", fg="red", bold=True))
    return "fail"
