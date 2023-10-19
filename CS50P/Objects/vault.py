# Operator overloading
# in this example the + operator is used to add 

class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)

print(f"Weasley: {weasley}")
print(f"Potter: {potter}")
print(f"Total: {total}")