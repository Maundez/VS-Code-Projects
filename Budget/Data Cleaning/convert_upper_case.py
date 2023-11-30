import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog


# The file is in the same directory as the script
# file_path = 'categories.xlsx'

# Create a file dialog to allow the user to select a file.
root = tk.Tk()
file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx",)])

# Close the file dialog.
root.destroy()

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name='categories')

# Convert all the data to uppercase
df_upper = df.map(lambda x: x.upper() if isinstance(x, str) else x)

# Remove all multiple spaces and replace them with a single space in the 'Description' column
df['Description'] = df['Description'].str.replace(r'\s+', ' ', regex=True)

# Show the first few rows of the modified DataFrame
print(df_upper.head())

# Get the original filename
original_file_name = file_path.split('/')[-1]

# Create a new filename
modified_file_name = 'modified_' + original_file_name

# Save the modified DataFrame to a new Excel file
df_upper.to_excel(modified_file_name, index=False)

