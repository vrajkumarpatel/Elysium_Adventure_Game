"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: chapter3.py
Purpose: Investigate the Main Lab, question or accuse the Lead Researcher,
         or search quietly for logs. Choices grant clues, set status, and
         direct you toward the ventilation shafts chapter.
"""

from player import banner, divider, show_hud, choose, clear_screen, print_art, colorize


def run_chapter3(player):
    """Run Chapter 3 with Lead Researcher and branching actions."""
    # Prepare visuals and show lab art
    clear_screen()
    banner("Chapter 3 – Main Lab Investigation")
    print_art("lab.txt")
    print("The main lab is a mess—broken equipment, spilled chemicals, and a frantic researcher.")
    print("Objective: Investigate the theft and gather evidence.")
    show_hud(player)
    divider("=")
    # Researcher reacts differently if flagged/compromised
    if player.status in {"flagged", "compromised"}:
        print("The Researcher watches you warily, noticing your presence in audit logs.")

    # Present choices for how to proceed in the lab
    choice = choose([
        "Question the Researcher [gain clue_mind_control; helps Ch4 staged-death]",
        "Search the lab quietly [gain Gamma-7 ID; helps Ch5]",
        "Accuse the Researcher [status alarmed; increases risk Ch4]",
        "Leave the lab [loop to Ch2; special consequence after 2 leaves in Ch4]",
    ])
    # You can press Q here to quit the game immediately
    if choice == "quit":
        print(colorize("Quitting game.", fg="yellow", bold=True))
        return "quit"

    # Choice 1: ask questions and gain a mind-control clue
    if choice == "1":
        player.add_item("clue_mind_control")
        print("\nHe slips and mentions entrainment thresholds and override delays.")
        print("Clue added: mind-control tech parameters.")
        return "chapter4"

    # Choice 2: search quietly and discover Gamma-7 evidence
    if choice == "2":
        player.add_item("identified_subject:Gamma-7")
        player.flags["identified_gamma7"] = True
        print("\nYou find a hidden log: 'Subject Gamma-7 accessed vents; device control logged.'")
        print("Lead points toward ventilation shafts.")
        return "chapter4"

    # Choice 3: accuse the Researcher which triggers lockdown
    if choice == "3":
        player.set_status("alarmed")
        print("\nYou accuse him. He panics and triggers lockdown protocols immediately.")
        print("Footsteps grow louder in the corridor—security is converging.")
        return "chapter4"

    # Choice 4: leave the lab and go back toward the research deck
    print("\nYou leave the lab to rethink your approach.")
    player.lab_leaves += 1
    return "chapter2"
