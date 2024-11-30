number = float(input ("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number provided is neutral.")
    else:
        print("The number provided is positive.")
else:
    print("The number provided is negative.")