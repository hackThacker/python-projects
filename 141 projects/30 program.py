# wrute a python program to caluclatte the natural logarithm of any number 

import math

num = float(input("Enter the number :"))
if num <= 0:
    print(" enter the postive number")
else:
    result = math.log(num)
    print(f"the natural logarithm of {num} is: {result}")