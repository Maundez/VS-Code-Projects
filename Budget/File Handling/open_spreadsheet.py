import openpyxl

# Open the Excel file
wb = openpyxl.load_workbook("example.xlsx")

# Get the first sheet
sheet = wb.active

# Print the sheet name
print(sheet.title)

# Read the cell values
for row in sheet.rows:
  for cell in row:
    print(cell.value)

# Iterate through the rows
for row in sheet.rows:
  # Get the value of the first cell
  cell_value = row[0].value

  # If the cell value is "hello" or "goodbye", write "greeting" in the next column
  if cell_value in ["hello", "goodbye"]:
    row[1].value = "greeting"

  # If the cell value is "cat", "dog", or "elephant", write "animal" in the next column
  elif cell_value in ["cat", "dog", "elephant"]:
    row[1].value = "animal"

# Save the Excel file
wb.save("example.xlsx")    