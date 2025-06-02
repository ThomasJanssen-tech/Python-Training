cars = input("Provide a list of car brands separated by commas: ")

list_cars = cars.split(",")  # Split the string into a list using comma as the delimiter
list_cars.sort()  # Sort the list in ascending order

print("The last car in the alphabet is:", list_cars[-1])  # Print the last car in the sorted list
