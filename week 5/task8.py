# Continually ask the user for a number until they input a value between 50-75
while True:
    user_number = int(input("Enter a number between 50 and 75: "))
    if 50 <= user_number <= 75:
        print("Congratulations! You entered a number within the range of 50-75.")
        break

print("Congratulations! You have successfully escaped the loop.")
