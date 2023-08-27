import time
import random


def playgame():
    # Sets up the game to be played
    colors = [
        'yellow',
        'purple',
        'pink'
        ]
    boss = [
        'wicked fairie',
        'dragon',
        'monster',
        'wizard',
        'witch',
        'gorgon'
        ]
    building = [
        'house',
        'cabin',
        'castle'
        ]
    params = {}
    params['color'] = random.choice(colors)
    params['boss'] = random.choice(boss)
    params['building'] = random.choice(building)
    params['bag'] = []
    intro(params)


def intro(params):
    # Intro
    print_pause("You find yourself standing in an open field, filled with " +
                f"grass and {params['color']} wildflowers.")
    print_pause(f"Rumor has it that a {params['boss']} is somewhere around " +
                "here, and has been terrifying the nearby village.")
    print_pause(f"In front of you is a {params['building']}.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) " +
                "dagger.")
    field(params)


def print_pause(text):
    # Print then pause 2 seconds
    print(text)
    time.sleep(2)


def fight(params):
    # Things that happen when the player fights
    if 'sword' in params['bag']:
        print_pause(f"As the {params['boss']} moves to attack, you unsheath " +
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as " +
                    "you brace yourself for the attack.")
        print_pause(f"But the {params['boss']} takes one look at your" +
                    "shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {params['boss']}. You " +
                    "are victorious!")
        replay()
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {params['boss']}.")
        print_pause("You have been defeated!")
        replay()


def cave(params):
    # Things that happen in the cave
    print_pause("You peer cautiously into the cave.")
    if "sword" in params['bag']:
        print_pause("You've been here before, and gotten all the good stuff." +
                    " It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword " +
                    "with you.")
        params["bag"].append("sword")
    print_pause("You walk back out to the field.")
    field(params)


def field(params):
    # Things that happen when the player runs back to the field
    while True:
        print(f"\nEnter 1 to knock on the door of the {params['building']}.")
        print("Enter 2 to peer into the cave.")
        print("What would you like to do?")
        choice = input('(Please enter 1 or 2)\n')
        if choice == '1':
            house(params)
            break
        elif choice == '2':
            cave(params)
            break


def house(params):
    # Things that happen to the player in the house
    print_pause(f"You approach the door of the {params['building']}.")
    print_pause(f"You are about to knock when the door opens and out steps " +
                f"a {params['boss']}.")
    print_pause(f"Eep! This is the {params['boss']}'s {params['building']}!")
    print_pause(f"The {params['boss']} attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only " +
                "having a tiny dagger.")
    while True:
        choice = input("Would you like to (1) fight or (2) run away? ")
        if choice == '2':
            print_pause("You run back into the field. Luckily, you don't " +
                        "seem to have been followed.")
            field(params)
            break
        elif choice == '1':
            fight(params)
            break


def replay():
    # Asks the player if they want to play again
    while True:
        choice = input("Would you like to play again? (y/n)").lower()
        if choice == "y":
            print_pause("Excellent! Restarting the game ...")
            playgame()
            break
        elif choice == "n":
            print_pause("Thanks for playing! See you next time.")
            break


playgame()
