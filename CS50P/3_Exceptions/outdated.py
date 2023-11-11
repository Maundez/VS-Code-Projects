#  prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
#  [checked the date was valid by using a regex]
#  wherein the month in the latter might be any of the values in the months list 
#  Then output that same date in YYYY-MM-DD format. 
#  If the user’s input is not a valid date in either format, prompt the user again. [Used a While True: loop]
#  Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

import re
from datetime import datetime
# List of month names for reference
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Regular expression pattern for the MM/DD/YYYY format
slash_date_pattern = r'^(\d{1,2})/(\d{1,2})/(\d{4})$'

# Regular expression pattern for the MMMM DD, YYYY format
full_date_pattern = r'^(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})$'

# This (while True:) starts an infinite loop (True is always True - it's just logic at work here
# and will keep repeating the block of code until a match is found. 
# It exits when a break is reached in an if match statement

while True: 
    try:
        date_input = input("Date: ").strip()

        # Attempt to match the MM/DD/YYYY format first
        match = re.match(slash_date_pattern, date_input)
        if match:
            # Extract date components from the matched groups as we know the exact format
            month, day, year = match.groups()
            
            # Convert date to YYYY-MM-DD format and validate its correctness using datetime
            formatted_date = datetime.strptime(f"{month}/{day}/{year}", "%m/%d/%Y").strftime("%Y-%m-%d")
            print(formatted_date)
            break
        
        # Attempt to match the MMMM DD, YYYY format (if we have gotten this far it means that the MM/DD/YYYY format didn't work)
        match = re.match(full_date_pattern, date_input)
        if match:
            # Extract date components from the matched groups
            month_name, day, year = match.groups()
            month_num = months.index(month_name) + 1
            formatted_date = datetime.strptime(f"{month_num}/{day}/{year}", "%m/%d/%Y").strftime("%Y-%m-%d")
            print(formatted_date)
            break

        #If we get this far then the user is prompted for the date again")

    except KeyboardInterrupt:   # Handle the case where the user wants to exit
        print("User exited.")
        print("User exited.")
        break
    except ValueError:  # Handle incorrect date values (e.g., February 30)
        pass            # Pass statement is just a placeholder that does nothing but where syntactically some code is required,
                        # but you don't want any action to take place. 
                        # In the above case, the pass statement simply allows the loop to continue to the next iteration, 
                        # effectively sending the user back to the input prompt.