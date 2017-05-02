from random import choice, randint # Used to make "random" choices

"""
Problems:
x We can die after an input even if we find the right answer
x Player don't know that he have a limited amount of try => no pressure
- We can input 2 time the same number and it only waste a try without feedback
- To much text at each try
"""

def print_clones(list):
    """Print a list to the player so that he can have a visual feedback.
    Can't print lists which have more than 10 elements for display reason.
    """
    enemies = ""
    numbers = ""
    i = 1
    for enemy in list:
        enemies += enemy
        numbers += "%d " % i
        i += 1
    print enemies
    print numbers

def clones_monster():
    clones = ['O ' for i in range(10)]
    original = randint(0, len(clones) - 1) # We choose a random number that the player will have to find (from 0 to the length of the 'clones' tab)
    nbAssault = 1
    hitlist = range(1, len(clones) + 1) # used to know if the player already tried to hit an enemy

    print original
    while nbAssault < 4:
        print_clones(clones)
        print "which one?"
        hit = raw_input("> ")
        hit = int(hit)
        if hit in hitlist:
            del hitlist[hit - 1] # We remove number the player choose so that it miss if he try the same number two again
            clones[hit - 1] = 'X '

            if hit - 1 == original:
                print "win!"
                exit()
            elif hit - 1 > original:
                print "plus petit"
            elif hit - 1 < original:
                print "plus grand"
            else:
                dead("dead")

            print "fin if 1"
            nbAssault += 1
        else:
            dead("miss")

def dead(why):
    print why
    exit()

clones_monster()