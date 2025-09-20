# write a program to check armstrong number

num = int(input("Enter the number: "))

# Number of digits in num
num_str = str(num)
num_digit = len(num_str)

# Initialize variables
power = 0
temp = num

# Calculate the sum of digits raised to the power of num_digit
while temp > 0:
    digit = temp % 10
    power += digit ** num_digit
    temp //= 10

# Check if it is an Armstrong number (outside the loop!)
if power == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")