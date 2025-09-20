# write program to solve quadratic quation

"""
The standar form of quadratic quation is ax^2 + bx + c = 0
    where a, b and c are real numbers and a != 0

The solution of quadratic quation is given by the formula:
    x = (-b ± √(b^2 - 4ac)) / 2

"""

import math
#input conefficients

a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b:"))
c = float(input("enter coefficient c:"))

#calculate the discrimainat

d = b**2 - 4*a*c

#check if the discriminant is positive, negative or zero

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The roots are real and different.\nRoot 1: {root1}\nRoot 2: {root2}")   
elif d == 0:
    root = -b / (2*a)
    print(f"The roots are real and same.\nRoot: {root}")    
else:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-d) / (2*a)
    print(f"The roots are complex and different.\nRoot 1: {realPart} + {imagPart}i\nRoot 2: {realPart} - {imagPart}i")