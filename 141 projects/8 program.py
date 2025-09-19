#write program to display calendar , month date, year, time

import calendar
import datetime

year = int(input("enter the year: "))
MONTH = int(input("enter the month: "))

cal = calendar.month(year, MONTH)
print(cal)


now =datetime.datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")