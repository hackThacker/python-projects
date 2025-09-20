# write a program to find the factorial of a number

num = int(input("enter the number : "))
factorial = 1
if num < 0:
    print("doesnot exit for negative number")
elif num == 0:
    print("factorial 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
        print(f'the factorial of {num} is {factorial}')
