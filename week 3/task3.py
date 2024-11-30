userInput = input("Please input a word: ")

character = input("Please input a character: ")

for char in userInput:
    if character in char:
        print("True!")
    else:
        print("False!")