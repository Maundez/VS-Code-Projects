import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import re

# Function to load CSV file
def load_csv_file(title, filetypes, sheet_name='Sheet1'):
    root = tk.Tk()
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Clean the DataFrame
def clean_dataframe(df):
    # Convert all string data to uppercase
    df = df.map(lambda x: x.upper() if isinstance(x, str) else x)
    
    # Remove all non-alphanumeric characters except spaces
    df['Description'] = df['Description'].astype(str).apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
    
    # Remove all numeric characters
    df['Description'] = df['Description'].astype(str).apply(lambda x: re.sub(r'[0-9]', '', x))
    
    # Replace multiple spaces with a single space
    df['Description'] = df['Description'].astype(str).str.replace(r'\s+', ' ', regex=True)
    
    return df

# Add financial year based on Australian financial year
def add_financial_year(df, date_column='Date'):
    def financial_year(date):
        if date.month > 6:
            return f"FY{date.year}/{date.year + 1}"
        else:
            return f"FY{date.year - 1}/{date.year}"
    
    df[date_column] = pd.to_datetime(df[date_column])  # Ensure the date column is in datetime format
    df['Financial Year'] = df[date_column].apply(financial_year)
    return df

# Split and assign columns
def split_and_assign_columns(df, categories_df):
    df['Credits'] = df['Amount'].apply(lambda x: x if x > 0 else None)
    df['Debits'] = df['Amount'].apply(lambda x: abs(x) if x < 0 else None)
    df['Categories'] = df['Description'].apply(lambda x: assign_category(x, categories_df))
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df.drop(columns=['Amount', 'Date'], inplace=True)
    return df

# Assign category
def assign_category(description, categories_df):
    # Iterate through each column in the categories DataFrame, where each column represents a category
    for category in categories_df.columns:
        # Get all the keywords for the current category, removing any NaN values
        keywords = categories_df[category].dropna()
        
        # Check if any of the keywords appear in the description
        if any(keyword in description for keyword in keywords):
            # If a keyword is found, return the name of the category
            return category
    
    # If no keywords are found in the description, return 'Other'
    return 'Other'

# Clean descriptions
def clean_descriptions(main_df, cleanup_df):
    for idx, row in cleanup_df.iterrows():
        dirty_desc = row['dirty_description']
        clean_desc = row['clean_description']
        category = row['category_passthrough']
        
        mask = main_df['Description'].str.contains(dirty_desc, case=False, na=False)
        main_df.loc[mask, 'Description'] = clean_desc
        
        #main_df.loc[mask, 'Categories'] = category  # Optional: Update Categories based on cleanup
    return main_df

# Load multiple CSV sheets (if your CSV has different sections, otherwise this might need to be removed)
def load_multiple_sheets(title, filetypes, sheet_names):
    # Open file dialog to let the user select the Excel file
    root = tk.Tk()
    excel_file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()

    # Read specified sheets into separate DataFrames and store them in a dictionary
    dfs = {}
    for sheet in sheet_names:
        dfs[sheet] = pd.read_excel(excel_file_path, sheet_name=sheet)
        
    return dfs

# Save the DataFrame as CSV
def save_dataframe(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    # Load main financial data
    main_df = load_csv_file("Select the financial data file", [("CSV files", "*.csv")])

    # Clean the main DataFrame
    main_df = clean_dataframe(main_df)
    
    # Assuming categories and cleanup information is in the same CSV
    # Adjust the code if they are in separate files
    categories_df = main_df['Categories'].dropna().unique()
    cleanup_df = main_df['Cleanup'].dropna().unique()

    # Clean descriptions based on the Cleanup DataFrame
    main_df = clean_descriptions(main_df, cleanup_df)

    # Assign categories and split columns
    main_df = split_and_assign_columns(main_df, categories_df)

    # Add financial year column
    main_df = add_financial_year(main_df)

    # Reorganize columns to put 'Financial Year' at the end
    column_order = ['Year', 'Month', 'Day', 'Debits', 'Credits', 'Description', 'Categories', 'Account', 'Financial Year']
    main_df = main_df[column_order]

    # Save the DataFrame with a timestamp in the filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_path = f'categorized_data_{timestamp}.csv'
    save_dataframe(main_df, save_path)

if __name__ == "__main__":
    main()