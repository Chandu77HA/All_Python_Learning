import time

# Time in secounds starts from 1970
ball = time.time()
print("Epoch timestamp value :", ball)
# Output: Epoch timestamp value : 1664418993.7937267

bat = time.localtime(ball)
print("Local Time :", bat)
# Output: Local Time : time.struct_time(tm_year=2022, tm_mon=9, tm_mday=29, tm_hour=8, tm_min=6, tm_sec=33, tm_wday=3, tm_yday=272, tm_isdst=0)

wicket = time.ctime(ball)
print("Normal time format as in OS :", wicket)
# Output: Normal time format as in OS : Thu Sep 29 08:06:33 2022
run = time.asctime(bat)
print("ASCI format : ", run)
# Output: ASCI format :  Thu Sep 29 08:06:33 2022

import datetime

out = datetime.datetime.now()
print("Current time", out)
print("Current year : ", out.year)
print("Current month : ", out.month)
print("Current day : ", out.day)
print("Current date : ", out.date())
print("Current hour : ", out.hour)
print("Current minute : ", out.minute)
print("Current second : ", out.second)
print("Current microsecond : ", out.microsecond)

# Output:
# Current time 2023-09-19 15:55:28.023934
# Current year :  2023
# Current month :  9
# Current day :  19
# Current date :  2023-09-19
# Current hour :  15
# Current minute :  55
# Current second :  28
# Current microsecond :  23934

score1 = datetime.datetime(2022, 9, 23, 12, 10, 42, 333657)
print("Required date", score1)
score2 = datetime.datetime(2022, 10, 10, 12, 10, 42, 333657)
print("Required date", score2)

# Output:
# Required date 2022-09-23 12:10:42.333657
# Required date 2022-10-10 12:10:42.333657

difference1 = score1 - out
print("Difference of D1: ", difference1)
difference2 = score2 - out
print("Difference of D2: ", difference2)
difference3 = difference2 - difference1
print("Difference D2 - D1: ", difference3)

# Output:
# Difference of D1:  -6 days, 4:00:14.239364
# Difference of D2:  11 days, 4:00:14.239364
# Difference D2 - D1:  17 days, 0:00:00


print((out.day)+ 7)
# Output:
# 36


# Week day short version
print("Week day short version -",out.strftime("%a"))

# Week day full version
print("Week day full version -",out.strftime("%A"))

# Week day as number # 0 as Sunday
print("Week day as number # 0 as Sunday -",out.strftime("%w"))

# Day of month
print("Day of month -",out.strftime("%d"))

# Month Name short version
print("Month Name short version -",out.strftime("%b"))

# Month Name full version
print("Month Name full version -",out.strftime("%B"))

# Month as a number
print("Month as a number -",out.strftime("%m"))

# Year Short version
print("Year Short version -",out.strftime("%y"))

# Year Full version
print("Year Full version -",out.strftime("%Y"))

# Minute
print("Minute -",out.strftime("%M"))

# Second
print("Second -",out.strftime("%S"))

# Hour - 24-Hour Format
print("Hour - 24-Hour Format -",out.strftime("%H"))

# Hour - 12-Hour Format
print("Hour - 12-Hour Format -",out.strftime("%I"))

# Represent Dates in numerical format
print("dd-mm-yy HH:MM:SS : -", out.strftime("%d-%m-%y %H:%M:%S"))
print("dd-mm-yy HH:MM:SS : -", out.strftime("%d/%B/%Y %H:%M:%S"))

# Output:
# Week day short version - Thu
# Week day full version - Thursday
# Week day as number # 0 as Sunday - 4
# Day of month - 29
# Month Name short version - Sep
# Month Name full version - September
# Month as a number - 09
# Year Short version - 22
# Year Full version - 2022
# Minute - 19
# Second - 38
# Hour - 24-Hour Format - 08
# Hour - 12-Hour Format - 08
# dd-mm-yy HH:MM:SS : - 29-09-22 08:19:38
# dd-mm-yy HH:MM:SS : - 29/September/2022 08:19:38


import calendar
print(calendar.month(2021, 8))
print(calendar.firstweekday())

# Output:
#     August 2021
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31

print(calendar.firstweekday())
# Output: 0