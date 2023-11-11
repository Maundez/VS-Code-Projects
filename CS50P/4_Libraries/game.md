FUNCTION get_level():
    REPEAT UNTIL valid input:
        PROMPT user for level
        VALIDATE input
    RETURN level

FUNCTION generate_random(level):
    RETURN random number between 1 and level

FUNCTION get_guess():
    REPEAT UNTIL valid input:
        PROMPT user for guess
        VALIDATE input
    RETURN guess

FUNCTION evaluate_guess(target, guess):
    IF guess is less than target:
        RETURN "Too small!"
    ELSE IF guess is greater than target:
        RETURN "Too large!"
    ELSE:
        RETURN "Just right!"

MAIN FUNCTION:
    level = get_level()
    target = generate_random(level)
    REPEAT:
        guess = get_guess()
        feedback = evaluate_guess(target, guess)
        PRINT feedback
        IF feedback is "Just right!":
            EXIT
