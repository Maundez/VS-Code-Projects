def main():
    while True:
        try:
            fraction = input("Enter a fraction (e.g. 3/4): ")
            percentage = convert(fraction)
            gauge_reading = gauge(percentage)
            print(gauge_reading)
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    parts = fraction.split('/')
    if len(parts) != 2:
        raise ValueError("Invalid format")

    numerator, denominator = map(int, parts)
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if numerator > denominator:
        raise ValueError("Numerator cannot be greater than the denominator")
 

    result = numerator / denominator
    return round(result * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
