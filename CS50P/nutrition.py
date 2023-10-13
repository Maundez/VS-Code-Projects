def get_calories(fruit):

    fruit_calories_dict = {
        'Meat': 250,
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

    fruit_calories = fruit_calories_dict.get(fruit, None)
    if fruit_calories is not None:
        print(f"Output: {fruit_calories}")

def main():
    fruit = input("Item: ")
    get_calories(fruit)

main()