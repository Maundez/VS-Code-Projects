import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog


# Create a file dialog to allow the user to select a file.
root = tk.Tk()
file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx",)])

# Close the file dialog.
root.destroy()

# Read the Excel file into a DataFrame
df_raw = pd.read_excel(file_path)

# Convert all the data to uppercase
df = df_raw.map(lambda x: x.upper() if isinstance(x, str) else x)

print(df.head())

# Remove all multiple spaces and replace them with a single space in the 'Description' column
df['Description'] = df['Description'].str.replace(r'\s+', ' ', regex=True)

# Create 'Credits' and 'Debits' columns
df['Credits'] = df['Amount'].apply(lambda x: x if x > 0 else None)
df['Debits'] = df['Amount'].apply(lambda x: abs(x) if x < 0 else None)

# Show the first few rows of the modified DataFrame
print(df.head())
