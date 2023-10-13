import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def load_excel_file(title, filetypes, sheet_name='Sheet1'):
    root = tk.Tk()
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()
    return pd.read_excel(file_path, sheet_name=sheet_name)


import re

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


def split_and_assign_columns(df, categories_df):
    df['Credits'] = df['Amount'].apply(lambda x: x if x > 0 else None)
    df['Debits'] = df['Amount'].apply(lambda x: abs(x) if x < 0 else None)
    df['Categories'] = df['Description'].apply(lambda x: assign_category(x, categories_df))
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df.drop(columns=['Amount', 'Date'], inplace=True)
    return df

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

def clean_descriptions(main_df, cleanup_df):
    for idx, row in cleanup_df.iterrows():
        dirty_desc = row['dirty_description']
        clean_desc = row['clean_description']
        category = row['category_passthrough']
        
        mask = main_df['Description'].str.contains(dirty_desc, case=False, na=False)
        main_df.loc[mask, 'Description'] = clean_desc
        
        #main_df.loc[mask, 'Categories'] = category  # Optional: Update Categories based on cleanup
    return main_df

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


def save_dataframe(df, timestamp):
    df.to_excel(f'cleaned_and_updated_financial_data_{timestamp}.xlsx', index=False, sheet_name='Sheet1')

if __name__ == "__main__":
    # Load main financial data
    main_df = load_excel_file("Select the financial data file", [("Excel files", "*.xlsx")])
    
    # Clean the main DataFrame
    main_df = clean_dataframe(main_df)

    # Load both 'Categories' and 'Cleanup' sheets from the same Excel file
    title = "Select the Excel file containing Categories and Cleanup sheets"
    filetypes = [("Excel files", "*.xlsx")]
    sheet_names = ['Categories', 'Cleanup']
    dfs = load_multiple_sheets(title, filetypes, sheet_names)
    
    # Assign loaded DataFrames to individual variables
    categories_df = dfs['Categories']
    cleanup_df = dfs['Cleanup']

    # Clean descriptions based on the Cleanup DataFrame
    main_df = clean_descriptions(main_df, cleanup_df)

    # Assign categories and split columns
    main_df = split_and_assign_columns(main_df, categories_df)

    # Reorganize columns
    column_order = ['Year', 'Month', 'Day', 'Debits', 'Credits', 'Description', 'Categories', 'Account']
    main_df = main_df[column_order]
    
    print(main_df.head())

    # Save DataFrame
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # save_dataframe(main_df, timestamp)
    
    # Create the full path with timestamp
    path = f'C:\\Users\\smaun\\OneDrive\\Documents\\Data Analysis\\Budget\\Output\\categorized_data_{timestamp}.xlsx'
    
    # Save the DataFrame to an Excel file in a specific directory
    
    main_df.to_excel(path, index=False, sheet_name='Sheet1')


