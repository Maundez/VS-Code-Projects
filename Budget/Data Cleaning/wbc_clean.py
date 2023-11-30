import pandas as pd
from datetime import datetime
# Uncomment the following lines if you are running the code outside of this environment
from tkinter import filedialog
from tkinter import Tk
import os

# Function to transform the source data and add the 'Account' column
# Function to transform the source data and add the 'Account' column
def transform_data_with_account(df):
    # Drop the unwanted columns
    df.drop(['Bank Account', 'Balance', 'Categories', 'Serial'], axis=1, inplace=True)
    
    # Rename columns
    df.rename(columns={'Date': 'Date', 'Narrative': 'Description'}, inplace=True)
    
    # Combine 'Debit Amount' and 'Credit Amount' into a single 'Amount' column
    df['Amount'] = df['Credit Amount'].fillna(0) - df['Debit Amount'].fillna(0)
    
    # Drop the now unnecessary 'Debit Amount' and 'Credit Amount' columns
    df.drop(['Debit Amount', 'Credit Amount'], axis=1, inplace=True)
    
    # Add the 'Account' column with the value 'WBC-DS'
    df['Account'] = 'WBC-DS'
    
    # Drop any rows with NaN values in 'Amount' column
    df.dropna(subset=['Amount'], inplace=True)

    # Reorder columns
    df = df[['Date', 'Amount', 'Description', 'Account']]
    
    return df


# Uncomment the following lines to use the file dialog in your local environment
# Hide the main tkinter window
root = Tk()
root.withdraw()

# Open file dialog to select the source CSV file
title = "Select the source CSV file"
filetypes = [("CSV files", "*.csv")]
file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)

# For the purpose of this environment, we'll use the hardcoded path of the uploaded file
#file_path = '/mnt/data/wbc_source_format.csv' # Replace this with the above filedialog code

# Load the source CSV file
source_df = pd.read_csv(file_path)

# Transform the data
transformed_df = transform_data_with_account(source_df)

# Generate a timestamp for the output filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Get the directory of the source file to save the new file in the same location
directory = os.path.dirname(file_path)

# Define the path for the output Excel file with the timestamp
# output_file_path = os.path.join(directory, f'transformed_with_account_{timestamp}.xlsx')
output_file_path = os.path.join(directory, f'{timestamp} transformed_WBC Data_export.csv')

# Save the transformed data to an Excel file
transformed_df.to_csv(output_file_path, index=False)

# The Excel file is saved in the same directory as the source file with a timestamp to ensure it's unique
print(f"Transformed file saved as: {output_file_path}")
