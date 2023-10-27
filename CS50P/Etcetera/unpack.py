# args returns a list: Positional: (100, 50, 25)
# kwargs returns a dict: Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}
# Can pass either *args and *kwargs to another function

def f(*args, **kwargs):
#    print("Positional:", args)
    print("Named:", kwargs)
    
f(galleons=100, sickles=50, knuts=25)
# Returns "Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}" - a dict"# 

# f(100, 50, 25)
# Returns "Positional: (100, 50, 25)"
