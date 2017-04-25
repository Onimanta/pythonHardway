# Import argv from the sys module
from sys import argv

# Put the parameters passed to script into variables
script, filename = argv

# We use the "open" function with the filename of our text file as an argument
# to create a file object in the "txt" variable
txt = open(filename)

# We print the filename to the user
print "Here's your file %r:" % filename
# We use the "read" function to print text contained in the file object
print txt.read()
# We close the file with the "close" function
txt.close()

print "Type the filename again:"
# We take the filename from the input of the user
file_again = raw_input("> ")

# Same operation as before but with the filename taken from "raw_input"
txt_again = open(file_again)

# Print again with "read" function
print txt_again.read()
txt_again.close()