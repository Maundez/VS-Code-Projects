# Purpose of the Code
# The code aims to loop through a list of dictionaries, where each dictionary represents information about a student in the Harry Potter universe. 
# It prints the name, house, and associated animal for each student, separating these values by a comma.

# Initialize a list of dictionaries, each representing a student's information.
students = [
    {"name": "Hermoine", "house": "Griffyndore", "animal": "Otter"},
    {"name": "Harry", "house": "Griffyndore", "animal": "Stag"},
    {"name": "Ron", "house": "Griffyndore", "animal": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "animal": None}
]

# Loop through each student dictionary in the 'students' list
for student in students:
    print(student["name"], student["house"], student["animal"], sep=", ")