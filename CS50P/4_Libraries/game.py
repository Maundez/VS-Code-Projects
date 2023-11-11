# In a file called game.py, implement a program that:
# Prompts the user for a level, 
# If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
# Hints
# Note that the random module comes with quite a few functions, per 
# docs.python.org/3/library/random.html.

import random

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n >= 1:
                return n
            else:
                continue
        except ValueError:
            continue

def generate_random(level):
    target = random.randint(1, level)
    return target

def get_guess():   
    while True:    
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
            else:
                continue
        except ValueError:
            continue
        
    
def evaluate_guess(target, guess):        
        if guess > target:
            return "Too large!"
        elif guess < target:
            return "Too small!"
        elif guess == target:
            return "Just right!"

        
def main():
    level = get_level()
    target = generate_random(level)
    
    while True:
        guess = get_guess()
#        print(f"Target is: {target}")
        result = evaluate_guess(target, guess)
        print(result)
        if result == "Just right!":
            break
    
if __name__ == "__main__":
    main()
    
    
    
    
    


