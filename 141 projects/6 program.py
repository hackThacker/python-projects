# write program to convert kilometers to miles, inches, feet and centimeters

kilometers = float(input("Enter distance  in kilometers: "))

#converting to miles 1kilometers = 0.621371 miles

copnverted_miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {copnverted_miles} miles")

# converting to kilometers to inches 1 kilometer = 39370.1 inches
convert_inches = kilometers * 39370.1
print(f"{kilometers}kilometers is equal to {convert_inches} inches")

# converting to kilometers to feet 1 kilometer = 3280.84 feet
convert_feet = kilometers * 3280.84         
print(f"{kilometers} kilometers is equal to {convert_feet} feet")

# converting to kilometers to centimeters 1 kilometer = 100000 centimeters
convert_centimeters = kilometers * 100000
print(f"{kilometers} kilometers is equal to {convert_centimeters} centimeters")

