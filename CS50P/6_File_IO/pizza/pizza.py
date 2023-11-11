# Pizza menu CSV import and read
# Outputs to tabular format
import sys
from tabulate import tabulate
import csv

def main():
    # Check for command line validity - The program should exit via sys.exit. if...
    if len(sys.argv) < 2:   # user does not specify exactly one command-line argument
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:     # user does not specify exactly one command-line argument
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.csv'):  # specified file’s name does not end in .csv,
        sys.exit("Not a CSV file")
   
    try:
        # Open csv file
        with open(sys.argv[1], newline = '') as csvfile:
            pizza_menu = csv.reader(csvfile)
            tabulate_menu(pizza_menu)
               
    except FileNotFoundError:
        sys.exit("File not found")
# https://pypi.org/project/tabulate/        
def tabulate_menu(pizza_menu):
    table = pizza_menu
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    
if __name__ == "__main__":
    main()