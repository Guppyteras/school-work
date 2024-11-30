# Step 1: Create a list of the following numbers
numbers = [73, 18, 64, 60, 26, 33, 66, 74, 59, 69, 60, 95, 53, 45, 57, 1, 48, 88, 13, 62]

# Step 2: Iterate through the list of numbers and determine if the number is between 1-50 or between 51-100
file_50_and_under = open("50_and_under.txt", "a")
file_over_50 = open("over_50.txt", "a")

for number in numbers:
    if 1 <= number <= 50:
        # i) Append the number to a file named 50_and_under.txt
        file_50_and_under.write(str(number) + "\n")
    elif 51 <= number <= 100:
        # b) If the number is between 51-100
        # i) Append the number to a file named over_50.txt
        file_over_50.write(str(number) + "\n")

# Close the files
file_50_and_under.close()
file_over_50.close()