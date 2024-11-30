# Count down from 60 to 12 by 3s, skipping the odd numbers
number = 60
while number >= 12:
    if number % 2 == 0:
        print(number, end=" ")
    number -= 3
