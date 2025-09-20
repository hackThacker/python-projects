# write a program to find te sum of natural number

num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    total += i

print(f"The sum of natural numbers up to {num} is: {total}")

