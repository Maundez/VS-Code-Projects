# Returning a tuple - use brackets - immutable(non-editable)
# Returning a dict - use parenthesis - mutable (editable). More structured with keys and values.
# Dicts use square brackets and strings in quotes, either single or double depending on the context.
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravensclaw"
    print(f"{student['name']} from {student['house']}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
            
if __name__ == "__main__":
    main()
    