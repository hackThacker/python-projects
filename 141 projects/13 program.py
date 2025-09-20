# write a program to check leap year

year = int(input("Enter a year: "))

"""
divided by 100 meands centrury year ( ending with 00)
century year divide by 400 is leap year 
"""

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year ".format(year))
elif (year % 4 == 0 ) and (year % 100 != 0):
        print(f"{year} is a leap year ".format(year))
else:
    print(f"{year} is a not leap year ".format(year))