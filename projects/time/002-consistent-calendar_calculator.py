# calendar calculator; automatic or manual #

import datetime
import math


x = input("ENTER or \"m\"")
if x != "m":
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
elif x == "m":
    year = input("What year? ")
    month = input("What month? ")
    day = input("What day in the month? ")

day_of_year = datetime.datetime(int(year), int(month), int(day)).timetuple().tm_yday

if int(year) % 4 == 0:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            day_of_year -= 1
            if day_of_year % 73 == 0:
                day_of_month = 73
                month_number = math.floor(day_of_year / 73)
            else:
                day_of_month = day_of_year % 73
                month_number = math.floor((day_of_year / 73) + 1)
        else:
            day_of_year = day_of_year
            if day_of_year % 73 == 0:
                day_of_month = 73
                month_number = math.floor(day_of_year / 73)
            else:
                day_of_month = day_of_year % 73
                month_number = math.floor((day_of_year / 73) + 1)
    else:
        day_of_year -= 1
        if day_of_year % 73 == 0:
            day_of_month = 73
            month_number = math.floor(day_of_year / 73)
        else:
            day_of_month = day_of_year % 73
            month_number = math.floor((day_of_year / 73) + 1)
else:
    day_of_year = day_of_year
    if day_of_year % 73 == 0:
        day_of_month = 73
        month_number = math.floor(day_of_year / 73)
    else:
        day_of_month = day_of_year % 73
        month_number = math.floor((day_of_year / 73) + 1)

print("")

weekday = day_of_year % 5
if weekday == 0:
    print("Friday")
elif weekday == 1:
    print("Monday")
elif weekday == 2:
    print("Tuesday")
elif weekday == 3:
    print("Wendsday")
elif weekday == 4:
    print("Thursday")
print(str(year) + " / " + str(month_number) + " / " + str(day_of_month))
