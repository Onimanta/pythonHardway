name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54 # centimeter
weight = 180 # lbs
weight_kg =  weight * 0.45 # kilogramme
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usualy %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)