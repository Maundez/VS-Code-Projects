def get_calories(fruit):
    
    # Define a dictionary containing the calorie counts for various fruits
    fruit_calories_dict = {
        'Lemon': 15,
        'Lime': 20,
        'Avocado': 50,
        'Cantaloupe': 50,
        'Honeydew': 50,
        'Pineapple': 50,
        'Strawberries': 50,
        'Tangerine': 50,
        'Grapefruit': 60,
        'Nectarine': 60,
        'Peach': 60,
        'Plums': 70,
        'Orange': 80,
        'Watermelon': 80,
        'Grapes': 90,
        'Kiwifruit': 90,
        'Pear': 100,
        'Sweet Cherries': 100,
        'Banana': 110,
        'Apple': 130,
    }

    # Get the calorie count for the given fruit from the dictionary. 
    # If the fruit isn't found, it defaults to None.
    fruit_calories = fruit_calories_dict.get(fruit, None)
    if fruit_calories is not None:
        print(f"Output: {fruit_calories}")

def main():
    fruit = input("Item: ")
    get_calories(fruit)

main()