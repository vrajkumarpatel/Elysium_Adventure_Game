"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: chapter4.py
Purpose: Decide how to act in the ventilation shafts during lockdown—analyze
         a device, follow the trail, send a distress signal, or return to the
         lab. Choices set items/status and can trigger success/failure.
"""

from player import banner, divider, show_hud, choose, clear_screen, colorize, print_art


def run_chapter4(player):
    """Run Chapter 4 with options: analyze device, trail deeper, distress signal, return."""
    # Prepare visuals and show shafts art
    clear_screen()
    banner("Chapter 4 – Ventilation Shafts / Lockdown Event")
    print_art("shafts.txt")
    print("The log pointed to Test Subject Gamma-7, but the cell is empty.")
    print("A faint oil trail leads into dark utility shafts; a discarded control device lies nearby.")
    print("Objective: Decide your action in the shafts during lockdown.")
    show_hud(player)
    divider("=")
    # Special flavor/effects
    if player.lab_leaves >= 2:
        print("Note: The lab was empty when you left twice—something is wrong.")

    # Main choices around the device and the oil trail
    choice = choose([
        "Analyze the device [gain control_device; unlocks Ch5 best ending]",
        "Follow the trail deeper [to Ch5; safer with stealth/swift]",
        "Send a fake distress signal [patrol_routes enables evade to Ch5]",
        "Go back to the lab [staged death hint if clue_mind_control]",
    ])
    # Press Q to quit this chapter menu
    if choice == "quit":
        print(colorize("Quitting game.", fg="yellow", bold=True))
        return "quit"

    # Choice 1: analyze and take control device for later use
    if choice == "1":
        player.add_item("control_device")
        player.control_device = True
        print("\nYou analyze the device: signal patterns implicate a familiar rival—now the mastermind.")
        print("You pocket the control device for later use.")
        return "chapter5"

    # Choice 3: distress signal; patrol intel can help you evade
    if choice == "3":
        print("\nYou broadcast a counterfeit distress signal.")
        if player.has_item("patrol_routes"):
            # Sub-menu for choosing how to act after sending a distress signal
            sub = choose([
                "Use patrol intel to evade and slip toward the pods",
                "Hold position and wait for response",
            ])
            # Allow quitting from the sub-menu too
            if sub == "quit":
                print(colorize("Quitting game.", fg="yellow", bold=True))
                return "quit"
            if sub == "1":
                print("You route around response teams using timing windows.")
                return "chapter5"
            print("You wait—bad choice. Teams triangulate your position.")
            print(colorize("FAIL: Security flags your location and catches you on sight.", fg="red", bold=True))
            return "fail"
        print(colorize("FAIL: Security flags your location and catches you on sight.", fg="red", bold=True))
        return "fail"

    # Choice 2: follow trail; risk higher if flagged/compromised
    if choice == "2":
        print("\nYou follow the oil trail through the ducts toward the Escape Pod Bay.")
        if player.status in {"flagged", "compromised"}:
            print("The patrol spots you! You fail.")
            return "fail"
        if player.status in {"stealth", "swift"}:
            print("Bonus: Your stealth/speed helps you avoid a patrol entirely.")
        return "chapter5"

    # Choice 4: go back to the lab; reveals staged death if you found the clue
    print("\nYou double back to the lab. The Lead Researcher lies dead—too late.")
    if player.has_item("clue_mind_control"):
        print("You notice inconsistencies—this looks staged to erase evidence.")
    print(colorize("FAIL: Evidence compromised. Mission ends.", fg="red", bold=True))
    return "fail"
