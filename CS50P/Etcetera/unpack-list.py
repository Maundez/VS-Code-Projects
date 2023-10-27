# The * symbol allows us to unpack the list passing individual values to the variables
# Without this, the entire list would be passed just to galleons
# Works with lists and tuples as they reserve order
# Does not work with sets
def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")

# Also works like this
# print(total(galleons=100, sickles=50, knuts=25), "Knuts")