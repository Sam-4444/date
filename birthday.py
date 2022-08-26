import datetime


import calendar
y=int(input("input the year :"))
x=int(input("input the month :"))
print(calendar.month(y,x))


age=int(input("enter your age (in years):"))
now=datetime.datetime.now().year
print(f"birthday(year) :{now-age}")