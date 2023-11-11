import random

# Constants
NUM_QUESTIONS = 10
MAX_INCORRECT_ATTEMPTS = 3

def prompt_for_level():
    """Prompt the user for a difficulty level and return the selected level."""
    while True:
        try:
            level = int(input("Level (1/2/3): "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Silently handle the error and prompt again

def generate_random_integer(level):
    """Generate and return a random integer based on the chosen difficulty level."""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

def prompt_for_guess(question):
    """Prompt the user for their guess and return it."""
    while True:
        try:
            return int(input(question))
        except ValueError:
            pass  # Silently handle the error and prompt again

def main():
    level = prompt_for_level()
    correct_answers = 0
    
    for _ in range(NUM_QUESTIONS):
        x = generate_random_integer(level)
        y = generate_random_integer(level)
        correct_answer = x + y
        
        incorrect_attempts = 0
        while incorrect_attempts < MAX_INCORRECT_ATTEMPTS:
            guess = prompt_for_guess(f"{x} + {y} = ")
            
            if guess == correct_answer:
                correct_answers += 1
                break
            else:
                print("EEE")
                incorrect_attempts += 1
        
        if incorrect_attempts == MAX_INCORRECT_ATTEMPTS:
            print(f"The correct answer was: {correct_answer}")
    
    print(f"Score: {correct_answers}")

if __name__ == "__main__":
    main()
