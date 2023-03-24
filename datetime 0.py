# import datetime
# print(datetime.datetime(2022,1,23))
# # 2022-01-23 00:00:00


# print(datetime.timedelta.days)


# print(datetime.timedelta(12))


# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# Only days, seconds, and microseconds remain
# print(delta)


# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# # Only days, seconds, and microseconds remain
# print(delta)
# print(datetime.timedelta(days=64, seconds=29156, microseconds=10))



# print(datetime.timedelta(12))

# from datetime import timedelta
# d = timedelta(microseconds=-1)
# print((d.days, d.seconds, d.microseconds))
# # (-1, 86399, 999999)



# print(datetime.timedelta.min)


# from datetime import timedelta
# print(timedelta.max)

# timedelta(hours=-5)
# datetime.timedelta(days=-1, seconds=68400)
# print(datetime.timedelta(-1,hours=19))







# from datetime import timedelta
# delta1 = timedelta(1, seconds=57)
# delta2 = timedelta(hours=24, seconds=57)
# print(delta2 == delta1)
# print(delta2 > delta1)
# print(delta2 == 5)
# print(delta2 > 5)
# print(timedelta(1, seconds=57))
# print(timedelta(hours=24, seconds=57))

# from datetime import timedelta
# print(timedelta.total_seconds(timedelta(minutes=1)))

# from datetime import timedelta
# year = timedelta(days=365)
# print(year)
# another_year = timedelta(weeks=40, days=84, hours=23,
#                          minutes=50, seconds=600)
# print(another_year)                         
# print(year == another_year)
# print(year.total_seconds())



# from datetime import timedelta
# import datetime
# year = timedelta(days=365)
# print(year)
# # 365 days, 0:00:00
# ten_years = 10 * year
# ten_years
# print(ten_years)
# # 3650 days, 0:00:00
# datetime.timedelta(days=3650)
# ten_years.days // 365
# print(ten_years.days // 365)
# # 10
# nine_years = ten_years - year
# nine_years
# print(nine_years)
# # 3285 days, 0:00:00
# datetime.timedelta(days=3285)
# three_years = nine_years // 3
# print(three_years)
# # 1095 days, 0:00:00
# three_years, three_years.days // 365
# print(three_years, three_years.days // 365)
# # 1095 days, 0:00:00 3
# (datetime.timedelta(days=1095), 3)
# print(datetime.timedelta(days=1095), 3)
# # 1095 days, 0:00:00 3

import datetime
# # print(datetime.date(2023,1,22))
# # print(datetime.datetime.today())


# print(datetime.date.fromordinal(2023, 1, 25))

# print(datetime.date(year=1, month=1, day=1))

# print(datetime.date.today())

# datetime.date.fromisoformat("2023-01-25")



from datetime import date
# date.fromisoformat('2019-12-04')
# datetime.date(2019, 12, 4)
# print(date.fromisoformat('2019-12-04'))
# print(datetime.date(2019, 12, 4))
# # 2019-12-04
# # 2019-12-04

# date.fromisoformat('20191204')
# datetime.date(2019, 12, 4)
# print(date.fromisoformat('20191204'))
# print(datetime.date(2019, 12, 4))
# # 2019-12-04
# # 2019-12-04


# date.fromisoformat('2021-W01-1')
# datetime.date(2021, 1, 4)
# print(date.fromisoformat('2021-W01-1'))
# print(datetime.date(2021, 1, 4).strftime("%Y-%b-%d"))


# day = datetime.datetime.strptime("2023-01-25", "%Y-%m-%d")
# print(day)


# print(datetime.date.fromisocalendar(year=2023, week=52, day=7))


# print(datetime.datetime.now().strftime("%H:%M:%S"))


# datetime.date.min
# print(datetime.date.min)
# print(datetime.date(datetime.MINYEAR, 1, 1))


# datetime.date.max
# print(datetime.date.max)
# # 9999-12-31
# print(datetime.date(datetime.MAXYEAR, 12, 31))
# # 9999-12-31


# datetime.date.resolution
# print(datetime.date.resolution)


print(datetime.date(1, 1, year=1))


