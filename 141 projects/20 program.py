# write a program to find armstrong number between interval 

low = int(input("Enter the starting number (e.g., 1): "))
upper = int(input("Enter the highest number: "))

print(f"Armstrong numbers between {low} and {upper} are:")

for num in range(low, upper + 1):
    order = len(str(num))  # Number of digits
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # ✅ This must be inside the for-loop
    if num == sum:
        print(num)
