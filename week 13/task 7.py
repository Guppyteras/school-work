import sys

def main():
    try:
        number = int(input("Please enter an odd number: "))
        if number % 2 == 0:
            raise ValueError("Error: The number must be odd.")
        print("You entered the odd number:", number)
    except ValueError as e:
        print(e, file=sys.stderr)
    finally:
        print("Thank you for using the program!")

if __name__ == "__main__":
    main()