# Pizza menu CSV import and read
# Outputs to tabular format
import sys
from tabulate import tabulate
import csv
from datetime import datetime

def main():
    # Check for command line validity - The program should exit via sys.exit. if...
    if len(sys.argv) < 3:   # user does not specify exactly two command-line arguments
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:     # user does not specify exactly two command-line arguments
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):  # specified file’s name does not end in .csv,
        sys.exit("Not a CSV file")
    
    data = read_csv(sys.argv[1])
    # Get the time to use as a unique filename for testing multiple outputs
    now = datetime.now()
    export_filename = str(now.strftime("%H-%M-%S") + " - " + sys.argv[2])
    # export_filename = str(sys.argv[2])
    
    write_csv(export_filename, data)
   
# Open and read file
def read_csv(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        sys.exit("File not found")
    except PermissionError:
        sys.exit("Permission denied: Unable to access the file")
    except csv.Error as e:
        sys.exit(f"CSV error: {e}")
    except UnicodeDecodeError:
        sys.exit("File decoding error: Check the file encoding")

# Write a new csv file with "first", "last" and "house" columns.
def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        
        for record in data:
            name = record['name']
            first_name = name.split(',')[1].strip()
            last_name = name.split(',')[0].strip()
            house = record['house']
            writer.writerow({'first': first_name, 'last': last_name, 'house': house})
            #print(f" Hello {first_name} {last_name}, {house}")       
        
  
if __name__ == "__main__":
    main()