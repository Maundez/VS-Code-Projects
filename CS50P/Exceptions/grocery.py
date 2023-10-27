grocery_dict = {}  # Initialize an empty dictionary

while True:
    try:
        item = input("Grocery item: ").strip().lower()  # Read input and convert to lowercase
    except EOFError:
        break  # Exit the loop on EOFError

    # Update the item count in the dictionary
    if item in grocery_dict:
        grocery_dict[item] += 1
    else:
        grocery_dict[item] = 1
sorted_grocery = dict(sorted(grocery_dict.items(), key=lambda x: x[0].lower()))

# iterate through the sorted dictionary and print the items with their counts in uppercase.
for item, count in sorted_grocery.items():
    print(f"{count} {item.upper()}")

