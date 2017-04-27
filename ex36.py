from sys import exit
from random import choice

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
    else:
        start()

def use_weapon(weapon, foe):
    """Test the use of a weapon on a foes and print the result.
    It also tell the player that the weapon is broken and remove it from him.
    :return worked: Tell if the use of the weapon worked on the foe.
    """

    worked = False

    if weapon == 'bat':

        if foe == 'man':
            print "The man wakes up as you take your bat off of your pocket."
            print "You hit him in the knees with your bat. The man finishes off on the ground. Crying."
            worked = True
        elif foe == 'two_monsters':
            print ""
        else:
            print "The %s didn't worked on the %s." % (weapon, foe)
            worked = False

    elif weapon == 'trash lid':

        if foe == 'man':
            print "The man wakes up, takes a bazooka out of his pocket and shoots at you."
            print "You give a big hit in the rocket with your trash lid and send it back to the man."
            print "He explodes in a rain of blood."
            worked = True
        elif foe == 'monster':
            print "You put your lid in front of you, close your eyes and run with all your strength on the monster."
            print "He wants to stop you with is paw but you hit it with all your might and put it back."
            print "The angry monster take a step back and you go trough him."
            worked = True
        else:
            print "The %s didn't worked on the %s." % (weapon, foe)
            worked = False

    elif weapon == 'dead fish':

        if foe == 'man':
            print "You take your dead fish out of your pocket and start swinging it around."
            print "The smell is waking up the man, it looks like he's not feeling good."
            print "The man starts to become all green, he can't breath anymore. He fall on the ground, dead."
            worked = True
        elif foe == 'monster':
            print "You throw the dead fish in his face."
            print "The monster, disgusted, goes back home (some says that he becomes a family monster)."
            worked = True
        elif foe == 'choose_intruder':
            print ""
        else:
            print "The %s didn't worked on the %s." % (weapon, foe)
            worked = False

    else:
        print "Where did you get that weapon?! Ok, let's say it work.."
        worked = True

    print "Sadly, your %s is now broken." % weapon
    weapon = None
    return worked

def start():
    """It's the first area. Here the player choose a weapon and enter the dungeon."""
    i = 1
    global weapon
    global weapons

    print "You are in a large area. There's almost nothing here, just some big piles of trash here and there."
    if len(weapons) > 0 and not weapon:
        print "On the ground there's %d items. Which one do you take?" % len(weapons)
        for item in weapons:
            print "%d. %s" % (i, item)
            i += 1

        item = int(raw_input("> "))

        if item <= len(weapons) and item > 0:
            weapon = weapons[item - 1]
            weapons.pop(item - 1)
            print "After picking the item you wander randomly trough the area."
            monster()
        else:
            weapon = None
            print "You tried to take an item but you missed it."
            print "Never mind.. You start to wander randomly trough the area."
            monster()
    else:
        print "You don't really know where to go so you wander randomly trough the area."
        monster()

def monster():
    """First enemy of the game. Easy to beat."""
    global weapon
    global weapons

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
            print "After running to death you realize you came back from where you came from."
            start()
        elif waked_up_man == "2":
            dead("The man shoots you and you explode in a rain of blood.")
        else:
            print "You stare at the man with an empty look on your face."
            dead("He shoots you and you explode in a rain of blood.")

    elif man == "3":

        if use_weapon(weapon, 'man'):
            print "You continue your way randomly."
            random_area(['big_monster', 'choose_intruder'])
        else:
            dead("The man wakes up and stares at you. You're scared to death(literally).")

    else:
        print "You do nothing.. and it's maybe better like that."
        monster()

def big_monster():
    """Here the player will have to find a way ta pass by a big monster."""
    global weapon
    global weapons
    print "After walking for a moment you arrive in an other area."
    print "You're feeling something special about that place, like if the destiny bring you there.."
    print "You hear a loud noise coming from a bit further. It seems like it's from something really big."
    print "You look in the direction of the noise and see a gigantic dragon-like monster."
    print "There seems to be something really cool behind the monster so you decide to go face him."
    print "It seems that your presence is really pisses him off, he want you to get out of here."
    monster_moved = False

    while True:
        print "What do you do?"
        print "1. Run and pass behind the monster"
        print "2. Insult the mother of the monster"
        if weapon:
            print "3. Use your %s" % weapon
        else:
            print ""

        monster = raw_input("> ")

        if monster == "1" and monster_moved:
            print "You dodge the monster as he runs toward you and pass behind."
            print "The monster rush into a big pile of trash."
            print "A steamroller which was a the top of the pile of trash fall and smash the monster in parts."
            print "After you stopped to watch the spectacle, you continue your way."
            two_monsters()
        elif monster == "1" and not monster_moved:
            dead("The monster watch you run at him and eats you like you were a running biscuits")
        elif monster == "2" and monster_moved:
            print "The monster takes you in is mouth before you can finish your sentence."
            print("He sends you flying in the air, burns you with is breath of fire and eats you as fall.")
        elif monster == "2" and not monster_moved:
            print "The monster really don't liked what you did. He runs at you to crush you."
            monster_moved = True
        elif monster == "3":

            if use_weapon(weapon,'monster'):
                print "After you tamed the monster, you continue your way."
                two_monsters()
            else:
                print "The monster return next to the cool thing."

        else:
            dead("That don't worked really well..")

def choose_intruder():
    """Here there is going to be an enigma to resolve."""
    print "After wandering a moment, you arrive in front of a massive metal door. It must be well over 100 meters high."
    print "The door is placed between two huge piles of trash and an enormous snake is wrapped around it. It seems to be a Python.."
    print "After coming closer to the door you notice a small cathodic screen and something which looks like a keyboard."
    print "You have the impression of hearing a voice coming from the snake."
    print "\"I want a dictionary called x which contains the values 2, 7 and 13.\""
    print "Not sure what that means.. You're now in front of the keyboard. What do you do ?"

    while True:
        print "1. Try to type something"
        print "2. Give a kick to the door"
        if weapon:
            print "3. Use your %s" % weapon
        else:
            print ""

        keyboard = raw_input("> ")

        if keyboard == "1":
            print "You put your fingers on the keyboard and see a \"prompt\" appear on the little screen."
            door_input = raw_input(">> ")
            check_python_input(door_input)
        elif keyboard == "2":
            print "The screen explode and it blows your head away"
        elif keyboard == "3":
            print ""
        else:
            print ""

def two_monsters():
    """Here the player will have to fight two enemies at the same time."""
    print "TWO MONSTER"

def clones_monster():
    """"An enemy clone himself with a secret technique and attack the player! Which is the true one?"""
    print "CLONES MONSTER"

def dead(why):
    """Tell the player why he/she's dead and end the adventure."""
    print why, "Good job!"
    exit(0)

# This is the weapon of the player.
# It will be declared globally in each functions so it remains persistent during all the adventure.
weapon = None
# This is the list of the usable weapons of the game.
# We also declare it globally in each functions so it stay persistent
weapons = ['bat', 'trash lid', 'dead fish']

exec "nimp"