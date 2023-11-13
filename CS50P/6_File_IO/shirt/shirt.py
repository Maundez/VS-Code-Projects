import sys
from PIL import Image, ImageOps

def main():
    # Command-line arguments validation
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path, output_path = sys.argv[1], sys.argv[2]

    # Check file extensions
    if not (input_path.lower().endswith(('.jpg', '.jpeg', '.png')) and output_path.lower().endswith(('.jpg', '.jpeg', '.png'))):
        # sys.exit("Input and output files must be .jpg, .jpeg, or .png")        
        sys.exit("Invalid output")

    # Check if input and output have the same file extension
    if input_path.split('.')[-1].lower() != output_path.split('.')[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        # Open, resize, and crop the input image
        with Image.open(input_path) as input_image:
            shirt_image = Image.open("shirt.png")
            resized_input = ImageOps.fit(input_image, shirt_image.size)

            # Overlay the shirt on the resized input image
            resized_input.paste(shirt_image, (0, 0), shirt_image)

            # Save the output image
            resized_input.save(output_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()

