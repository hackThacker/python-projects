# write a program to find ascii value of character 
import string

character = str(input("Enter the character: "))
print("The ASCII value of '", character, "' is", ord(character))


# Combine lowercase (a-z), uppercase(A-Z), digits(0-9), and symbols(~-+)
all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Print ASCII values for each character in the combined set
for char in all_characters:
    print(f"The ASCII value of '{char}' is {ord(char)}")
