# Supporting switches
# The term argv refers to "argument values". 
# In Python, argv is a list in the sys module that contains the command-line arguments passed to the script. 
# The first item in this list, argv[0], is the name of the script itself.

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    """
    The -n is considered a "switch" or "option", and the value that follows it (when used on the command line) is the "argument" for that switch.

    In command-line terminology:

    A "switch" or "option" usually refers to a named command-line flag, often prefixed by - (single character) or -- (full word). It's used to modify the behavior of the command.
    An "argument" is a value or data that you pass to a switch or directly to the command itself.
    """
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")

