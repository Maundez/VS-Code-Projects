
    except FileNotFoundError:
        sys.exit("File not found")
    except PermissionError:
        sys.exit("Permission denied: Unable to access the file")
    except csv.Error as e:
        sys.exit(f"CSV error: {e}")
    except UnicodeDecodeError:
        sys.exit("File decoding error: Check the file encoding")
