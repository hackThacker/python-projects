# write a program to find factorail of number using recursion

def rec(n):
    if n == 1:
        return n 
    else:
        return n*rec(n-1)
num  = int(input("Enter the number : "))

if num < 0:
    print("factorial doesnot exit on negative integer")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("the factorial of 0",num, "is",rec(num))
    