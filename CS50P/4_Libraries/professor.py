import random

def main():
    # Get the desired difficuilty level - number of digits
    level = get_level()
    
    # Initialize variables for various counting requirements
    correct_answer_count = 0
    incorrect_answer_count = 0
    quiz_count = 0
    
    # User gets 10 questions generated at random
    while quiz_count < 10:
        # Generate two random integers based on the chosen level
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        
        # Reset incorrect answers count for each new question
        incorrect_answer_count = 0
        
        while True:                
            try:
                # Prompt the user for their answer
                user_answer = int(input(f"{x} + {y} = "))
            except ValueError:
                continue
            # Check if the users answer is correct
            if user_answer == correct_answer:
                correct_answer_count += 1
                break
            else:
                incorrect_answer_count += 1
                if incorrect_answer_count == 3:
                    # Provide the correct answer after 3 incorrect attempts
                    print(f"{x} + {y} = {correct_answer}")
                    break
                else:
                    # Notify the user of an incorrect answer
                    print("EEE")
        
        quiz_count += 1
    
    # Print out the user's score
    print(f"Score: {correct_answer_count}")

    
def get_level():
    # Continuously prompt the user for a level until a valid input is provided
    while True:
        try:
            n = int(input("Level: "))
            # Check if the provided level is valid
            if n in [1, 2, 3]:
                break

        except ValueError:
            # Handle non-integer inputs
            continue
    return n

            
def generate_integer(level):
    # Determine the range of integers based on the chosen level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)      
     

# Run the main function if the script is executed as a standalone program    
if __name__ == "__main__":
    main()   