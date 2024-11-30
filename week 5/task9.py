# Count up from 1 to 20 by ones, skipping the numbers 6 and 13
number = 1
while number <= 20:
    if number != 6 and number != 13:
        print(number, end=" ")
    number += 1