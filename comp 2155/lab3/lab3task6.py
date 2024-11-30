from lab3task5 import Apartment  # Import the Apartment class

# Create an Apartment object and pass 5 arguments
apartment = Apartment("123 Main St", 200000, 1500, 2, 2)

# Output the two new properties of Apartment class
print("Number of Bedrooms:", apartment._num_bedrooms)
print("Number of Bathrooms:", apartment._num_bathrooms)

# Change the values of the two new properties of Apartment by using the setters
apartment._num_bedrooms = 3
apartment._num_bathrooms = 3

# Output the toString of Apartment to display all five properties
print(apartment)