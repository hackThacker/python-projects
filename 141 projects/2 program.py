# write a program to do arithemetical operation addition and diviision
#add
num1 = float(input("etner the first number for addition :"))
num2 = float(input("enter the second number for addition :"))
sum = num1 + num2
print (f"add: {num1} + {num2} = {sum}")

#division
num3 = float(input("enter the dividend for divide :"))
num4 = float(input("enter the divisor fo division"))
if num4 == 0:
    print ("Error: Division by zero is not allowed.")
else:
    result = num3 / num4
    print(f"divide: {num3} / {num4} = {result}")
    