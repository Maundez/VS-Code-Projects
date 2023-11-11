def main():
    while True:
        try:
            fraction = input("Enter a fraction (e.g. 3/4): ")
            percentage = convert(fraction)
            gauge_reading = gauge(percentage)
            print(f"{gauge_reading}")
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    numerator, denominator = map(int, fraction.split('/'))
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
