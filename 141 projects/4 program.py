#write program to swap two variable

#input two variables
a = input("enter the value of first variable: ")
b = input("enter tha value of the seconf variable: ")

#display the orginal value
print(f"orginal values: a ={a}, b ={b}")

#swap the values using tempary variables 
temp = a
a = b
b = temp

# shoiwng the swapped values

print(f"swapping values : a = {a}, b = {b}")
