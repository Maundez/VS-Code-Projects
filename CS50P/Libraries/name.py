# sys - contains functionality based on the system
# docs.python.org/3/library/sys.html 
# argv - list of all the words that the user passes in the prompt (arguments)

import sys

if len(sys.argv) < 2:    # We are after a single argument. Position 0 in the string is taken by the filename so Position 1 (2nd value) is our argument.
    sys.exit("Too few arguments")   # sys.exit is a built in command that exits the script if True
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    

print("hello, my name is", sys.argv[1])