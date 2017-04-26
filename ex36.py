from sys import exit
from random import choice

# This is the weapon of the player. It's declared globally because it keep it with him during all the adventure.
global weapon
# This is the list of the usable weapons of the game. We also declare it globally so it stay persistent
global weapons
weapons = ['bat', 'trash lid', 'dead fish']

def random_area(areas):
    """Make the player go to a random area
    :param areas: list of areas of the game from : monster, big_monster, choose_intruder,
                  two_monsters, clones_monster
    """
    area = choice(areas)
    if area == 'monster':
        monster()
    elif area == 'big_monster':
        big_monster()
    elif area == 'choose_intruder':
        choose_intruder()
    elif area == 'two_monsters':
        two_monsters()
    elif area == 'clones_monster':
        clones_monster()

def start():
    """It's the first area. Here the player choose a weapon and enter the dungeon."""
    i = 1

    print "You are in a large, empty area. There's nothing here."
    print "On the ground there's %d items. Which one do you take?" % len(weapons)
    for item in weapons:
        print "%d. %s" % (i, item)
        i += 1

    item = int(raw_input("> "))

    if item <= len(weapons) and item > 0:
        weapon = weapons[item - 1]
        weapons.pop(item - 1)
        print "After picking the item you wander randomly trough the area."
    else:
        weapon = None
        print "You tried to take an item but you missed it."
        print "Never mind.. You start to wander randomly trough the area."


def monster():
    """First enemy of the game. Easy to beat."""
    print "After a moment, you find a man asleep on a chair. What do you do?"
    print "1. Sneak behind him and continue forward"
    print "2. Wake him up"
    if weapon:
        print "3. Use your %s" % weapon
    else:
        print ""

    man = raw_input("> ")

    if man == "1":
        print "You pass behind the chair and go away from the man."
        random_area(['big_monster', 'choose_intruder'])
    elif man == "2":
        print "The man wakes up."
        print "Now he's standing, pointing at you with a bazooka on his shoulder. What do you do ?"
        print "1. Run for your life"
        print "2. Try to discuss with him to understand why he does that"

        waked_up_man = raw_input("> ")

        if waked_up_man == "1":
            "After running to death you realize you came back from where you came from."
            start()
        elif waked_up_man == "2":
            dead("The man shoots you and you explode in a rain of blood.")
        else:
    elif man == "3":
        if weapon == "bat":
            print "You hit him in the knees with your bat. The man finishes off on the ground. Crying."
            print "Sadly, your bat is now broken."
            weapon = None
            print "You continue your way randomly."
            random_area(['big_monster', 'choose_intruder'])
        elif weapon == "trash lid":
            print "The man wakes up, takes a bazooka out of his pocket and shoots at you."
            print "You give a big hit in the rocket with your trash lid and send it back to the man."
            print "He explodes in a rain of blood."
            print "Sadly, your trash lid is brocken now."
            weapon = None
            print "You continue your way randomly."
            random_area(['big_monster', 'choose_intruder'])
        elif weapon == "dead fish":

        else:

    else:
        print "You do nothing.. and it's maybe better like that."
        monster()

def big_monster():
    """Here the player will have to find a way ta pass by a big monster."""

def choose_intruder():
    """Here there is going to be an enigma to resolve."""

def two_monsters():
    """Here the player will have to fight two enemies at the same time."""

def clones_monster():
    """"An enemy clone himself with a secret technique and attack the player! Which is the true one?"""

def dead(why):
    """Tell the player why he/she's dead and end the adventure."""
    print why, "Good job!"
    exit(0)

start(weapons)