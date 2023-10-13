
def main():
    filename = input("File name: ").strip().lower()
    mime_type = get_file_extension(filename)
    print_mime_type(mime_type)

# Function to get the file extension
def get_file_extension(filename):
    extension = filename.split('.')
    return extension[-1]

# Function to print the MIME Type
def print_mime_type(mime_type): 
    if mime_type == "jpg":
        mime_type = mime_type.replace("jpg", "jpeg")

    match mime_type:
        case "gif" | "jpg" | "jpeg" | "png":
            print(f"image/{mime_type}")
        case "pdf" | "zip":
            print(f"application/{mime_type}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
 

    
# Call the main function
main()
