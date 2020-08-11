import time
import random


def print_pause(message_to_print):

    print(message_to_print)
    time.sleep(1)


# ASK THE PLAYER IF HE WANT TO PLAY AGAIN
def restar_game():
    # Options the player may have in the field
    s = input("Would you like to play again? (y/n)\n")
    if s == "y":
        print_pause("Excellent! Restarting the game ...")
        play()
    elif s == "n":
        print("THANKS FOR PLAYING! See you next time.")
        exit()
    else:
        restar_game()


# FIGTH DESITION
def fight(creature, collections, weapon, p_weapon, p_creature):

    # The damage that the creature and the weapon may
    # cause is multiplied by a randon number in order
    # to determinate who win the figth
    # The pobability that the weapon get a win is higher that the creature
    creature_damage = p_creature * random.randint(1, 5)
    weapon_damage = p_weapon * random.randint(3, 7)
    if weapon in collections:
        if weapon_damage > creature_damage:
            print_pause("As the " + creature + " moves to attack,\
you unsheath your new sword.")
            print_pause("The " + weapon + " shines brightly in your hand \
as you brace yourself for the attack.")
            print_pause("But the " + creature + " takes one look at your \
shiny new toy and runs away!")
            print_pause("You have rid the town of " + creature)
            print_pause("YOU ARE VICTORIOUS!!")
            restar_game()
        else:
            print_pause("As the " + creature + " moves to attack,\
you unsheath your new sword.")
            print_pause("The " + weapon + " shines brightly in your hand \
as you brace yourself for the attack.")
            print_pause("But the " + creature + " resist your attack!")
            print_pause("Both are very hurt, but the " + creature + "recover \
first and attack you")
            print_pause("unfortunately You have been defeated this time!")
            restar_game()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the pirate.")
        print_pause("You have been defeated!")
        print_pause("GAME OVER!")
        restar_game()


# # WHAT HAPPEN IN CAVE
def cave(creature, collections, weapon, p_weapon, p_creature):

    # Options the player may have in the field
    if weapon in collections:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff.\
It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(creature, collections, weapon, p_weapon, p_creature)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found  sthe magical " + weapon + "!")
        print_pause("You discard your silly old dagger and take the sword \
with you.")
        print_pause("You walk back out to the field.")
        collections.append(weapon)
        field(creature, collections, weapon, p_weapon, p_creature)


# # WHAT HAPPEN IN HOUSE
def house(creature, collections, weapon, p_weapon, p_creature):

    # Options the player may have in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a \
" + creature + ".")
    print_pause("Eep! This is the " + creature + "'s house!")
    print_pause("The " + creature + " attacks you!")
    if weapon in collections:
        n = "0"
        while n != "1" or n != "2":
            n = input("Would you like to (1) fight or (2) run away?\n")
            if n == "1":
                fight(creature, collections, weapon, p_weapon, p_creature)
            elif n == "2":
                print_pause("You run back into the field. Luckily, you don't \
seem to have been followed.")
                field(creature, collections, weapon, p_weapon, p_creature)

    else:
        n = "0"
        while n != "1" or n != "2":
            print_pause("You feel a bit under-prepared for this, what with \
only having a tiny dagger.")
            n = input("Would you like to (1) fight or (2) run away?\n")
            if n == "1":
                fight(creature, collections, weapon, p_weapon, p_creature)
            elif n == "2":
                print_pause("You run back into the field. Luckily, you don't \
seem to have been followed.")
                field(creature, collections, weapon, p_weapon, p_creature)


# WHAT HAPPEN IN THE FIELD
def field(creature, collections, weapon, p_weapon, p_creature):

    # Options the player may have in the field
    op = input('''
    Enter 1 to knock on the door of the house.\n
    Enter 2 to peer into the cave.\n
    What would you like to do?\n
    (Please enter 1 or 2.)\n''')
    if op == "2":
        cave(creature, collections, weapon, p_weapon, p_creature)
    elif op == "1":
        house(creature, collections, weapon, p_weapon, p_creature)
    else:
        print("NO VALID OPTION")
        field(creature, collections, weapon, p_weapon, p_creature)


# INTRODUCTION
def intro(creature, collections, weapon, p_weapon, p_creature):

    # Introduction to the story
    print_pause("You find yourself standing in an open field,\
filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature + " is somewhere around \
here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) \
dagger.")
    field(creature, collections, weapon, p_weapon, p_creature)
# START GAME


def play():

    # Names of the creatures and the weapons
    creatures = ["Pirate", "Gorgon", "Wicked fairie", "Dragon"]
    weapons = ["Sword of Ogoroth!", "Amethyst Staff", "The Sword of \
Truth", "Vorpal Sword "]

    # The power of each weapon and creature acording to the index position
    creatures_power = [4, 5, 6, 7]
    weapons_power = [6, 7, 8, 9]
    collections = []
    index_weapon = random.randint(0, 3)
    weapon = weapons[index_weapon]
    p_weapon = weapons_power[index_weapon]
    index_creature = random.randint(0, 3)
    creature = creatures[index_creature]
    p_creature = creatures_power[index_creature]
    intro(creature, collections, weapon, p_weapon, p_creature)


play()
