# write program to convert celsius to fahrenheit & fahrenheit to celsius

celsius = float(input("enter temperature in celsius: "))

#convert celsius to fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degree celsius is equal to {fahrenheit} degree fahrenheit")

#convert fahrenheit to celsius
fahrenheit = float(input("enter temperature in fahrenheit: "))  
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} degree fahrenheit is equal to {celsius} degree celsius")