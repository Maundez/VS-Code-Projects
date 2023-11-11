import mimetypes
file_name =  input("Filename? ")
file_type = mimetypes.guess_type(file_name)

print(f"MIME filetype = {file_type}")