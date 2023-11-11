# The ** symbol allows us to unpack the dict passing individual values to the variables
# It passes 'galleons=100, sickles=50, knuts=25' to the total() function

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

# Also works like this
# print(total(galleons=100, sickles=50, knuts=25), "Knuts")