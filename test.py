# -*- coding: utf-8 -*-

from random import choice, randint # Used to make "random" choices

def print_list(list):
    """Print a list to the player so that he can have a visual feedback.
    Can't print lists which have more than 10 elements for display reason.
    """
    enemies = ""
    numbers = ""
    i = 1
    for ennemy in list:
        enemies += ennemy
        numbers += "%d " % i
        i += 1
    print enemies
    print numbers

list = ['O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ']
toFind = randint(0, len(list) - 1)
i = 0

print_list(list)

while i < 4:
    position = int(raw_input("> "))
    list[position - 1] = 'X '
    if position - 1 == toFind:
        list = ['X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ']
        print_list(list)
        print "Found"
        exit()
    elif position - 1 > toFind:
        print_list(list)
        print "the number to find is smaller"
    elif position - 1 < toFind:
        print_list(list)
        print "the number to find is bigger"
    else:
        print "What?"

    i += 1

print "dead x_x"
print "position was %d" % toFind + 1