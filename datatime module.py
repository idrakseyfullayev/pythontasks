#                                "datetime" — Basic date and time types¶(Əsas tarix və vaxt növləri¶)
import datetime

#   Constants(Sabitlər)
datetime.MINYEAR  #??????????? contant ne demekdir????
#  The smallest year number allowed in a date or datetime object. MINYEAR is 1.
print(datetime.MINYEAR)

datetime.MAXYEAR
#  The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
print(datetime.MAXYEAR)

datetime.UTC
# Alias for the UTC timezone singleton datetime.timezone.utc.
print(datetime.timezone.utc )
#       New in version 3.11.



### Available Types(Mövcud Növlər) ###
datetime.datetime(year=0, month=0, day=0, hour=0, minute=0, second=0, microsecond=0,tzinfo=0)
print(datetime.datetime(2022,1,23))
# 2022-01-23 00:00:00



datetime.date(year=0, month=0, day=0)
print(datetime.date(2023,1,22)) 
# 2023-01-22

# MINYEAR <= year <= MAXYEAR
# 1 <= month <= 12
# 1 <= day <= number of days in the given month and year

datetime.date.today()
print(datetime.date.today())
# 2023-01-25

datetime.date.fromtimestamp(timestamp=1) # ?????????????????????????

datetime.date.fromordinal(ordinal=1)  # ????????????????????????

datetime.date.fromisoformat(date_string="")
datetime.date.fromisoformat("year-month-day") # - ancaq bu ardicilliqla isleyir
print(datetime.date.fromisoformat("2023-01-25"))
# 2023-01-25

from datetime import date
date.fromisoformat('2019-12-04')
print(date.fromisoformat('2019-12-04'))
# 2019-12-04
date.fromisoformat('20191204')
print(date.fromisoformat('20191204'))
# 2019-12-04
date.fromisoformat('2021-W01-1')
print(date.fromisoformat('2021-W01-1'))
# 2021-01-04
datetime.date(2019, 12, 4)
print(datetime.date(2019, 12, 4))
# 2019-12-04

datetime.date.fromisocalendar(year=0, week=0, day=0)
print(datetime.date.fromisocalendar(year=2023, week=52, day=7)) # day=range[1-7]
# 2023-12-31

datetime.date.min
print(datetime.date.min)
# 0001-01-01
datetime.date(datetime.MINYEAR, 1, 1)
print(datetime.date(datetime.MINYEAR, 1, 1))
# 0001-01-01

datetime.date.max
print(datetime.date.max)
# 9999-12-31
print(datetime.date(datetime.MAXYEAR, 12, 31))
# 9999-12-31

datetime.date.resolution  # ?????????????????????????????????/??
print(datetime.date.resolution) # ??????????????????????????????
# 1 day, 0:00:00

# Instance attributes (read-only):(yalnız oxumaq üçün):
datetime.date.year  # Between MINYEAR and MAXYEAR inclusive.
datetime.date.month # Between 1 and 12 inclusive.
datetime.date.day   # Between 1 and the number of days in the given month of the given year.
# ??????????????????????????????????????????????????



datetime.time(hour=0, minute=0, second=0, microsecond=0,tzinfo=0)
print(datetime.time(20))
# 20:00:00



datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(datetime.timedelta(12))
# 12 days, 0:00:00

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
print(delta)
# 64 days, 8:05:56.000010
print(datetime.timedelta(days=64, seconds=29156, microseconds=10))
# 64 days, 8:05:56.000010

from datetime import timedelta
d = timedelta(microseconds=-1)
print((d.days, d.seconds, d.microseconds))
# (-1, 86399, 999999)

timedelta.min
#  The most negative timedelta object, timedelta(-999999999).
print(datetime.timedelta.min)
# -999999999 days, 0:00:00

timedelta.max
# The most positive timedelta object, timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999).
print(datetime.timedelta.max)
# 999999999 days, 23:59:59.999999

timedelta.resolution # ??????????????????????????

print(datetime.timedelta(days=-1, seconds=68400))
# -1 day, 19:00:00

print(datetime.timedelta(-1,hours=19))
# -1 day, 19:00:00

from datetime import timedelta
delta1 = timedelta(1, seconds=57)
delta2 = timedelta(hours=24, seconds=57)
print(delta2 == delta1)
# True
print(delta2 > delta1)
# False
print(delta2 == 5)
# False
print(delta2 > 5)
# Traceback (most recent call last):
#  File "c:\Users\dell\Desktop\Python Ders 1\Python\task 0.py", line 73, in <module>
#    print(delta2 > 5)
#          ^^^^^^^^^^
#TypeError: '>' not supported between instances of 'datetime.timedelta' and 'int'
print(timedelta(1, seconds=57))
# 1 day, 0:00:57
print(timedelta(hours=24, seconds=57))
# 1 day, 0:00:57

from datetime import timedelta
timedelta.total_seconds()
print(timedelta.total_seconds(timedelta(minutes=1)))
# 60.0

from datetime import timedelta
year = timedelta(days=365)
print(year)
# 365 days, 0:00:00
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
print(another_year)
# 365 days, 0:00:00                         
print(year == another_year)
# True
print(year.total_seconds())
# 31536000.0

from datetime import timedelta
import datetime
year = timedelta(days=365)
print(year)
# 365 days, 0:00:00
ten_years = 10 * year
ten_years
print(ten_years)
# 3650 days, 0:00:00
datetime.timedelta(days=3650)
ten_years.days // 365
print(ten_years.days // 365)
# 10
nine_years = ten_years - year
nine_years
print(nine_years)
# 3285 days, 0:00:00
datetime.timedelta(days=3285)
three_years = nine_years // 3
print(three_years)
# 1095 days, 0:00:00
three_years, three_years.days // 365
print(three_years, three_years.days // 365)
# 1095 days, 0:00:00 3
(datetime.timedelta(days=1095), 3)
print(datetime.timedelta(days=1095), 3)
# 1095 days, 0:00:00 3


datetime.date.min
print(datetime.date.min)
# 0001-01-01
datetime.date(datetime.MINYEAR, 1, 1)
print(datetime.date(datetime.MINYEAR, 1, 1))
# 0001-01-01


datetime.tzinfo  # ???????????????????



datetime.timezone # ???????????????????



# Subclass relationships:(Alt sinif əlaqələri:)
# object
#     timedelta
#     tzinfo
#         timezone
#     time
#     date
#         datetime














































































































































































































