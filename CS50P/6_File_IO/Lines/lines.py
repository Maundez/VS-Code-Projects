import sys

def main():
    # Check for command-line argument validity
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.py'):
        sys.exit("Not a Python file")

    try:
        # Open the file and count the lines of code
        with open(sys.argv[1], 'r') as file:
            print(count_lines_of_code(file))
    except FileNotFoundError:
        sys.exit("File not found")

def count_lines_of_code(file):
    # Set a counter
    loc = 0
    for line in file:
        # Check if line is not a comment or blank
        if not line.lstrip().startswith('#') and line.strip():
            loc += 1
    return loc

if __name__ == "__main__":
    main()
