import datetime
import calendar



# printing the calendar
y=int(input("input the year :"))
x=int(input("input the month :"))
print(calendar.month(y,x))

# printing the year of birth
age=int(input("enter your age (in years):"))
now=datetime.datetime.now().year
print(f"birthday(year) :{now-age}")


# age by seconds
age=input("enter your age and press enter ! ")
print("your age  is (by seconds ): "+str(int((3.156)*(10**7)*int(age))))
