"""
Author: Vrajkumar Patel
Date: 12/2/2025
File: player.py
Purpose: Defines the Player class (tracks name, items, status, flags) and
         simple terminal UI helpers (colors, banners, HUD, clear screen,
         ASCII art printing) used across the game.
"""

class Player:
    """Represents the player and tracks state across chapters."""

    def __init__(self, name: str):
        # Save the player's display name
        self.name = name

        # Inventory items and current status (like undercover, stealth)
        self.inventory = []  # list of strings
        self.status = "healthy"  # e.g., healthy, compromised, injured, alarmed

        # Important booleans used by endings and gates
        self.has_keycard = False
        self.has_regulator = False

        # Track optional loop counts to trigger extra story flavor/effects
        self.loops_to_dock = 0
        self.lab_leaves = 0

        # Flexible flags for storyline (e.g., identified_gamma7)
        self.flags = {}
        # Quick access boolean for device usage
        self.control_device = False

    def add_item(self, item: str) -> None:
        """Add an item to the player's inventory if not already present."""
        if item not in self.inventory:
            self.inventory.append(item)

    def has_item(self, item: str) -> bool:
        """Check if the player has a specific item in inventory."""
        return item in self.inventory

    def set_status(self, status: str) -> None:
        """Update the player's current status string."""
        self.status = status


# Simple terminal UI helpers to make chapters visually clear and easy to use.
USE_COLOR = True

COLOR_CODES = {
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}

def colorize(text: str, fg: str | None = None, bold: bool = False) -> str:
    # Wrap text with ANSI codes if colors are enabled
    if not USE_COLOR or fg is None:
        return text
    code = COLOR_CODES.get(fg, 37)
    prefix = "\033[1;" if bold else "\033["
    return f"{prefix}{code}m{text}\033[0m"
def banner(title: str) -> None:
    # Print a bold chapter/title banner
    line = "═" * (len(title) + 8)
    colored_title = colorize(f"▶▶ {title} ◀◀", fg="cyan", bold=True)
    print(f"\n{line}\n{colored_title}\n{line}")


def divider(char: str = "-") -> None:
    # Draw a horizontal rule for visual separation
    print(char * 60)


def show_hud(player: Player) -> None:
    # Draw the player's status area (name, status, key items, inventory)
    divider("-")
    keycard = colorize("Yes", fg="green") if player.has_keycard else colorize("No", fg="red")
    regulator = colorize("Yes", fg="green") if player.has_regulator else colorize("No", fg="red")
    inventory = ", ".join(player.inventory) if player.inventory else "(empty)"
    status_color = {
        "healthy": "green",
        "undercover": "cyan",
        "stealth": "cyan",
        "swift": "cyan",
        "injured": "yellow",
        "alarmed": "yellow",
        "compromised": "red",
        "flagged": "yellow",
    }.get(player.status, "white")
    status_display = colorize(player.status, fg=status_color, bold=True)
    print(f"  {colorize('Player:', fg='magenta', bold=True)} {player.name}")
    print(f"  {colorize('Status:', fg='magenta', bold=True)} {status_display}    {colorize('Keycard:', fg='magenta', bold=True)} {keycard}    {colorize('Regulator:', fg='magenta', bold=True)} {regulator}")
    print(f"  Inventory: {inventory}")
    divider("-")


def choose(options):
    """Render a simple numbered menu and return the selected option.

    - Shows 1..N for each option in the list
    - Also shows [Q] to let the player quit from any menu
    - Returns the chosen number as a string (e.g., "1") or "quit" if Q
    """
    print("")
    # Print each option with its number
    for i, opt in enumerate(options, start=1):
        idx = colorize(f"[{i}]", fg="cyan", bold=True)
        print(f"  {idx} {opt}")
    # Show the quit shortcut
    qidx = colorize("[Q]", fg="cyan", bold=True)
    print(f"  {qidx} Quit game")
    # Build a prompt and a set of valid inputs ("1".."N")
    prompt = colorize(f"Select 1-{len(options)} or Q: ", fg="yellow", bold=True)
    valid = {str(i) for i in range(1, len(options) + 1)}
    while True:
        inp = input(prompt).strip()
        # If the player types Q/q, return "quit" so chapters can exit
        if inp.lower() == "q":
            return "quit"
        # If the input is a valid number, return it
        if inp in valid:
            return inp
        # Otherwise, ask again with a friendlier prompt
        prompt = colorize(f"Please enter 1-{len(options)} or Q: ", fg="yellow")


def clear_screen() -> None:
    # Clear the terminal screen (Windows or Unix)
    import os
    os.system("cls" if os.name == "nt" else "clear")


def print_art(filename: str, fg: str = "cyan") -> None:
    # Load and print ASCII art from the assets/ folder
    import os
    base = os.path.dirname(__file__)
    path = os.path.join(base, "assets", filename)
    if not os.path.exists(path):
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            art = f.read()
        print(colorize(art, fg=fg, bold=True))  # colorize art for visibility
    except Exception:
        pass

