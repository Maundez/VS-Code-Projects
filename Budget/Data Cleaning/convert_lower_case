import pandas as pd


# The file is in the same directory as the script
file_path = 'categories.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Your code to manipulate the DataFrame goes here
# Convert all the data to lowercase
df_lower = df.map(lambda x: x.lower() if isinstance(x, str) else x)

# Show the first few rows of the modified DataFrame
print(df_lower.head())

# Save the modified DataFrame to a new Excel file
df_lower.to_excel('modified_categories.xlsx', index=False)

