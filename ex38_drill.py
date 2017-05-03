from random import choice

cards = range(1, 14)
deck = []

print "Let's pull cards in the deck."
for family in ['PI', 'CA', 'TR', 'CO']:
    for card in cards:
        deck.append([card, family])

print "Here is the deck: "
def print_deck(deck):
    output = ""
    for card in deck:

        if card[0] % 13 == 0:
            output += str(card) + "\n"
        else:
            output += str(card)

    print output

print_deck(deck)

print "Where is the two of Heart?"
for card in deck:
    if card == [2, 'CO']:
        hand = card

print "Here it is: ", hand

print "Now let's pick a random card in the deck: ", choice(deck)

print "To finish I will sort the deck: "
deck.sort()
print_deck(deck)