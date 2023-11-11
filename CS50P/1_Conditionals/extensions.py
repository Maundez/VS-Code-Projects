# Main function
def main():
    filename = input("File name: ").strip().lower() # asks the user for the filename, removes spaces and converts to lower case
    mime_type = get_file_extension(filename) #calls the get_file_extension function to return the extension part only
    print_mime_type(mime_type)

# Function to get the file extension
def get_file_extension(filename):
    extension = filename.split('.') # splits the filename at the period
    return extension[-1] #returns to the right of the period, i.e. the file extension

# Function to print the MIME Type
def print_mime_type(mime_type):
    if mime_type == "jpg":
        mime_type = mime_type.replace("jpg", "jpeg") #replaces jpg with jpeg for consistency with the spec

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