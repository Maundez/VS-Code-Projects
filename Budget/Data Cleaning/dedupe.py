import pandas as pd
from datetime import datetime
from tkinter import filedialog
from tkinter import Tk
import os

def main():
    # Open file dialog to select the source CSV file
    title = "Select the source CSV file to dedupe"
    filetypes = [("CSV files", "*.csv")]
    
    # Set up the root Tkinter window and hide it
    root = Tk()
    root.withdraw()
    
    # Show the file dialog and get the file path
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    
    # Only proceed if a file was selected
    if file_path:
        dedupe(file_path)
    else:
        print("No file selected, exiting program.")
        root.destroy()  # Close the Tkinter window

def dedupe(file_path):
    # Load the source CSV file
    source_df = pd.read_csv(file_path)

    # Identify and remove duplicates based on all columns except 'Account' which might not be unique
    deduped_df = source_df.drop_duplicates(subset=['Date', 'Amount', 'Description'])

    # Generate a timestamp for the output filename
    timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    # Get the directory of the source file to save the new file in the same location
    directory = os.path.dirname(file_path)

    # Define the path for the output CSV file with the timestamp
    output_file_path = os.path.join(directory, f'{timestamp} deduped.csv')

    # Save the de-duplicated DataFrame to a new CSV file
    deduped_df.to_csv(output_file_path, index=False)

    # Print out a success message with the path to the de-duplicated file
    print(f"De-duplicated file saved as: {output_file_path}")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

