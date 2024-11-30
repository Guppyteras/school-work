import os

def main():
    try:
        file_name = input("Please enter the name of a text file to open in the current working directory: ")
        if not file_name.endswith(".txt"):
            raise NameError("Error: The file name must end with '.txt'.")
        file_path = os.path.join(os.getcwd(), file_name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Error: The file was not found.")
        with open(file_path, 'r') as f:
            print(f.read())
    except (NameError, FileNotFoundError) as e:
        print(e, file=sys.stderr)
    finally:
        print("Thank you for using the program!")

if __name__ == "__main__":
    main()