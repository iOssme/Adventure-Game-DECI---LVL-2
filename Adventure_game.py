import random
from colorama import Fore, Style
import time

# Global variables
score = 0
game_active = True
has_dagger = False
magical_item = None
enemy_fairy = None

# Arrays
FAIRY_TYPES = ["Frost Fairy", "Fire Fairy", "Shadow Fairy", "Nature Fairy"]
MAGICAL_ITEMS = ["Enchanted Amulet", "Fairy Dust Potion", "Magical Flute"]


def get_valid_delay():
    """Prompt user for a valid delay time."""
    while True:
        try:
            delay = int(input("Enter delay seconds (1-6): "))
            if 1 <= delay <= 6:
                return delay
            print(
                Fore.RED + "Enter a number between 1 and 6." + Style.RESET_ALL
            )
        except ValueError:
            print(Fore.RED + "Enter valid number." + Style.RESET_ALL)


DELAY = get_valid_delay()


def print_pause(message, pause=DELAY):
    """Print a message and pause for a specified time."""
    print(message)
    time.sleep(pause)


def update_score(points):
    """Update the player's score."""
    global score
    score += points
    print(f"Your current score: {score}")


def start_game():
    """Initialize the game and set the scene."""
    global enemy_fairy
    enemy_fairy = random.choice(FAIRY_TYPES)
    print_pause(
        f"You find yourself in a dense, eerie forest haunted by a "
        f"{Fore.YELLOW}{enemy_fairy}.{Style.RESET_ALL}"
    )
    print_pause("Ancient trees tower above you, branches tangled and ominous.")
    print_pause(
        "Fallen leaves cover the forest floor, creating a quiet atmosphere."
    )
    print_pause(
        f"Villagers whisper that the {Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL} "
        "is particularly dangerous, its presence felt in the eerie silence."
    )


def win_game():
    """Handle the win condition."""
    global game_active
    print_pause(
        f"{Fore.GREEN}Congratulations! You've defeated the "
        f"{Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL}"
        f"{Fore.GREEN} and saved the forest!{Style.RESET_ALL}"
    )
    update_score(10)
    print_pause(f"Final score: {score}")
    print_pause(f"{Fore.GREEN}You WIN!{Style.RESET_ALL}")
    game_active = False


def lose_game():
    """Handle the lose condition."""
    global game_active
    print_pause(
        f"{Fore.RED}Oh no! The {Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL}"
        f"{Fore.RED} has overpowered you.{Style.RESET_ALL}"
    )
    print_pause(f"Final score: {score}")
    print_pause(f"{Fore.RED}Game Over!{Style.RESET_ALL}")
    game_active = False


def random_event():
    """Generate a random event during gameplay."""
    events = [
        "A friendly woodland creature appears and gives you a hint.",
        "You stumble upon a magical spring that restores your energy.",
        "A sudden gust of wind reveals a hidden path.",
        "You hear the fairy's laughter echoing through the trees.",
    ]
    print_pause(random.choice(events))


def explore_forest():
    """Handle the forest area events."""
    print_pause("You returned to the dense, eerie forest.")
    if random.random() < 0.5:
        random_event()
    update_score(5)


def follow_path():
    """Handle the path following sequence."""
    global magical_item
    print_pause(
        f"You follow the {Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL} "
        "trail deeper into the forest."
    )
    print_pause(f"You encounter the {Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL}!")
    update_score(1)
    magical_item = random.choice(MAGICAL_ITEMS)
    if has_dagger and magical_item:
        print_pause("You draw the silver dagger you found earlier.")
        print_pause(
            f"The {Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL} "
            "recoils at the sight of the magical weapon!"
        )
        win_game()
    else:
        print_pause("You're defenseless against the powerful fairy.")
        lose_game()


def look_around():
    """Handle the look around action."""
    global has_dagger, magical_item
    print_pause(f"{Fore.GREEN}Search for a weapon{Style.RESET_ALL}")
    print_pause("Nearby, you find a fallen tree with a hidden compartment.")
    has_dagger = True
    magical_item = random.choice(MAGICAL_ITEMS)
    print_pause(
        f"Inside, you find a silver dagger and a "
        f"{Fore.LIGHTBLACK_EX}{magical_item}!{Style.RESET_ALL}\n"
        f"rumored to vanquish magical beings like the "
        f"{Fore.YELLOW}{enemy_fairy}{Style.RESET_ALL} haunting these woods."
    )

    while True:
        print_pause("1. Go back to the forest.")
        print_pause("2. Cross the bridge")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return explore_forest()
        elif choice == "2":
            return cross_bridge()
        else:
            print(f"{Fore.RED}Invalid choice. Try again.{Style.RESET_ALL}")
    update_score(2)
    print_pause("You take both items, feeling more prepared for what lies ahead.")


def cross_bridge():
    """Handle the bridge crossing action."""
    print_pause("The bridge is destroyed when you cross it.")
    print_pause(f"{Fore.LIGHTWHITE_EX}It's a fairy's curse.{Style.RESET_ALL}")
    update_score(-2)
    lose_game()


def game_choice():
    """Handle the main game choice menu."""
    while True:
        print_pause("1. Follow a faint trail")
        print_pause("2. Have a look around")
        print_pause("3. Cross the bridge")
        response = input("What would you like to do? ").strip().lower()
        if response == "1":
            return follow_path
        elif response == "2":
            return look_around
        elif response == "3":
            return cross_bridge
        else:
            print(f"{Fore.RED}Invalid choice. Try again.{Style.RESET_ALL}")


def play_game():
    """Main game loop."""
    global game_active, score, magical_item
    game_active = True
    score = 0
    magical_item = None

    start_game()
    while game_active:
        next_action = game_choice()
        next_action()


def main():
    """Main function to run the game."""
    while True:
        play_game()
        while True:
            again = input("Would you like to play again? (y/n): ").strip().lower()
            if again == "y":
                break  # Restart the game
            elif again == "n":
                print("Thanks for playing!")
                return  # End the game
            else:
                print(f"{Fore.RED}Please enter a valid answer{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
