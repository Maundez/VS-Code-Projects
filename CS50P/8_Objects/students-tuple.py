# Returning a tuple - use brackets - immutable(non-editable)
# Returning a list - use square brackets - mutable. Need to know the position of each item
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
    