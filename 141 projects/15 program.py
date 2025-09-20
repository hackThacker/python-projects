# write a program all prime numbers in an inteval of 1-100

low = 1
upper = 100

print("Prime numbers between", low, "&", upper, "are:")

for num in range(low, upper + 1):
    if num > 1:
        # Check if num is divisible by any number between 2 and num-1
        for i in range(2, int(num ** 0.5) + 1):  # Using square root for efficiency
            if (num % i) == 0:
                break
        else:
            # This else is associated with the for loop, not the if statement.
            print(num)
