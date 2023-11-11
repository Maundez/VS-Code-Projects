# Code adds up menu items as entered by a diner
# Declare the total cost variable
total_cost = 0.00

# Declare a dictionary to hold the menu items and their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00    
}
 
# Start an infinite loop to keep taking orders until some exit condition is met.
while True:
    try:
        # Take user input for the item and convert it to title case.
        # This will make it case-insensitive when matching with menu items.
        order = input("Item: ").title()
    except EOFError:
        # Catch the End-Of-File error, usually triggered by pressing Ctrl+D (or Ctrl+Z on Windows).
        # Break the loop and exit when this error is caught.
        break
    # Check if the entered item is in the menu
    if order in menu:
        # Add the cost of the item to the menu
        total_cost = total_cost + menu[order]
        # Retun the updated cost to two decimal places
        print(f"${total_cost:.2f}")
    else:
        # If the order is not on the menu, skip the rest of the loop and go back to the start
        continue
    

    