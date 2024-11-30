import sys

def main():
    try:
        number = int(input("Please enter a number: "))
        print("You entered the number:", number)
    except ValueError:
        print("Error: Invalid input. Please enter a number.", file=sys.stderr)
    finally:
        print("Thank you for using the program!")

if __name__ == "__main__":
    main()