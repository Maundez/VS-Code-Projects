# for multiple names
# code accepts names entered at the prompt e.g. python.names_2.py Steve Sheridan Donny and prints each on a separate line
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
# sys.argv accepts a slice(segment) number to get a part of the list so that it doesn't return names_2.py as a name.
# a negative value e.g.  sys.argv[1:-1]: would not return the ed value
for arg in sys.argv[1:]:
    print("hello, my name is", arg)