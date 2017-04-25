def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))
that = 35 + 74 - 180 * 50 / 2
# At last there is no need to worry about the priority of operations so I keep the line above
# that = 35 + (74 - (180 * (50 / 2)))


print "That becomes: ", what, "Can you do it by hand?"
print "My try at it: ", that

# I write a formula and try to create it with my functions
formula = 123.0 / 4.0 + 20.0 * 44.0 - 11.0
with_functions = substract(add(divide(123.0,4.0),multiply(20.0, 44.0)),11.0)

print "\nResult of the formula: ", formula
print "Result of the formula with functions: ", with_functions