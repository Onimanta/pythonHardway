# -*- coding: utf-8 -*-

cantons = {
    'NE': 'Neuchâtel',
    'VD': 'Vaud',
    'FR': 'Fribourg',
    'BE': 'Berne',
    'GE': 'Genève'
}

cities = {
    'Chaux-de-fonds': 'NE',
    'Lausanne': 'VD',
    'Bulle': 'FR',
    'Bienne': 'BE',
    'Meyrin': 'GE'
}

print "The abbreviation of all of the canton: ", cantons.keys()

print "Is Nyon in the cities?"
if 'Nyon' in cities:
    print "Yes"
else:
    print "No"

print "Ok, so let's put it in."
cities['Nyon'] = 'VD'
print cities