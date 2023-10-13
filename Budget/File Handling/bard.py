import re

# Open the Excel file
wb = openpyxl.load_workbook("example.xlsx")

# Get the active sheet
sheet = wb.active

# Iterate over all cells in the sheet
for row in sheet.iter_rows():
  for cell in row:
    # Match the cell value to the patterns
    match = re.match(r"hello|goodbye", str(cell.value).lower())
    if match:
      # Write 'greeting' in the next column
      sheet.cell(row=cell.row, column=cell.column+1).value = 'greeting'

    match = re.match(r"cat|dog|elephant", str(cell.value).lower())
    if match:
      # Write 'animal' in the next column
      sheet.cell(row=cell.row, column=cell.column+1).value = 'animal'

# Save the Excel file
wb.save("example.xlsx")