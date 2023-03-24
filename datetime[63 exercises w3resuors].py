#                             w3resource.  Python datetime [ 52 Exercises with Solution ]

# 1. Write a Python script to display the various Date Time formats - Go to the editor
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week


# 1. Müxtəlif Tarix Saat formatlarını göstərmək üçün Python skripti yazın - Redaktora keçin
# a) Cari tarix və vaxt
# b) Cari il
# c) İlin ayı
# d) İlin həftə nömrəsi
# e) Həftənin iş günü
# f) İlin günü
# g) Ayın günü
# h) Həftənin günü

# import calendar
# import time
# import datetime
# print(f"Current date and time: {datetime.datetime.now()}")
# print(f"Current year :{datetime.datetime.now().year}")
# print(f"Current yearr: {datetime.date.today().strftime('%Y')}")
# print(f"Month of year: {datetime.date.today().strftime('%B')}")
# print(datetime.date.today().strftime("%W"))
# print(datetime.date.today().strftime("%w"))
# print(datetime.date.today().strftime("%j"))
# print(datetime.date.today().strftime("%d"))
# print(datetime.date.today().strftime('%A'))


# 2. Write a Python program to determine whether a given year is a leap year. Go to the editor

# 2. Verilən ilin sıçrayış ili olub-olmadığını müəyyən etmək üçün Python proqramı yazın. Redaktora gedin

# import calendar
# import datetime
# import time

# class Leap_year:
#     def __init__(self, name,year):
#         self.year = year
#         self.name = name

#     def __str__(self):
#         return self.name


#     def leap_year_calendar(self):
#         if calendar.isleap(self.year):
#             return " is leap year"
#         else:
#             return " isn't leap year" 

          
        
# car_1 = Leap_year("Mercedes", 2000)
# car_2 = Leap_year("Toyota", 2020)
# car_3 = Leap_year("Prius", 2023)      

# print(f"""{car_1}:{car_1.leap_year_calendar()}
# {car_2}:{car_2.leap_year_calendar()}""")


# def leap_year(y):
#     if y % 400 == 0:
#         return True
#     if y % 100 == 0:
#         return False
#     if y % 4 == 0:
#         return True
#     else:
#         return False
# print(leap_year(1900))
# print(leap_year(2004))





# 3. Write a Python program to convert a string to datetime. Go to the editor
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00

# 3. Simli tarixə çevirmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə sətri: 1 yanvar 2014-cü il saat 14:43
# Gözlənilən nəticə : 2014-07-01 14:43:00


# import datetime

# current_time = datetime.datetime(2014, 1, 7, 14, 43) 
# print(type(current_time))

# cur_time = current_time.strftime("%Y-%d-%m %H:%M:%S")
# print(cur_time)


# 4. Write a Python program to get the current time in Python. Go to the editor
# Sample Format :  13:19:49.078205

# 4. Python-da cari vaxtı əldə etmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə Format: 13:19:49.078205

# import datetime
# current_time_1 = datetime.datetime.now().strftime("%H:""%M:""%S:""%f")
# print(current_time_1)

# current_time_2 = datetime.datetime.now().time()
# print(current_time_2)

# istediyim saatin capi
# import datetime
# current_time_3 = datetime.time(16, 49, 28, 272332)
# print(current_time_3)



# 5. Write a Python program to subtract five days from the current date. Go to the editor
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17

# 5. Cari tarixdən beş günü çıxmaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə Tarixi:
# Hazırkı Tarix: 22-06-2015
# Cari Tarixdən 5 gün əvvəl: 2015-06-17

# import datetime
# def subtract_days_cur_time(d):
#     current_time = datetime.date.today()
#     sub_cur_time = current_time - datetime.timedelta(d)
#     return sub_cur_time

# day = int(input())
# print(subtract_days_cur_time(day))



# import datetime
# def subtract_days_cur_time(d):
#     current_time = datetime.datetime.now().time()
#     sub_cur_time = current_time - datetime.timedelta(hours=d)
#     return sub_cur_time

# day = 5
# print(subtract_days_cur_time(day))


# import datetime
# print((datetime.datetime.now() - datetime.timedelta(hours= 5,minutes=5)).strftime("%H:" "%M:" "%S"))





# 6. Write a Python program to convert a Unix timestamp string to a readable date. Go to the editor
# Sample Unix timestamp string : 1284105682
# Expected Output : 2010-09-10 13:31:22

# 6. Unix vaxt damğası sətirini oxunaqlı tarixə çevirmək üçün Python proqramı yazın. Redaktora gedin
# Unix vaxt damğası sətirinin nümunəsi: 1284105682
# Gözlənilən Nəticə : 2010-09-10 13:31:22


# import datetime
# ts = 1284105682

# print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))



##  ????????????????????????????????
# import datetime
# print(
#     datetime.datetime.fromtimestamp(
#         int("1284105682")
#     ).strftime('%Y-%m-%d %H:%M:%S')
# )





# 7. Write a Python program to print yesterday, today, tomorrow. Go to the editor

# 7. Dünən, bu gün, sabah çap etmək üçün Python proqramı yazın. Redaktora gedin


# class Pyt_prog_date:

#     def __init__(self, name, n):
#         self.name = name
#         self.n = n

#     def __str__(self) -> str:
#         return self.name

#     def prog_date(self):
#         import datetime
#         return (datetime.date.today() + datetime.timedelta(self.n)).strftime("%d-" "%m-" "%Y")    

# yesterday = Pyt_prog_date("Yesterday", -1)
# today = Pyt_prog_date("Today", 0)
# tomorrow = Pyt_prog_date("Tomorrow", 1)
# print(f"""{yesterday} : {yesterday.prog_date()}
# {today} : {today.prog_date()}
# {tomorrow} : {tomorrow.prog_date()}""")

        
# import datetime 
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days = 1)
# tomorrow = today + datetime.timedelta(days = 1) 
# print('Yesterday : ',yesterday)
# print('Today : ',today)
# print('Tomorrow : ',tomorrow)



# 8. Write a Python program to convert the date to datetime (midnight of the date) in Python. Go to the editor
# Sample Output : 2015-06-22 00:00:00

# 8. Python-da tarixi tarixə (tarixin gecə yarısı) çevirmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə çıxışı : 2015-06-22 00:00:00


# import datetime

# today_ = datetime.date.today()
# print(today_)
# print(datetime.datetime(today_.year, today_.month, today_.day))

# from datetime import date
# from datetime import datetime
# dt = date.today()
# print(datetime.combine(dt, datetime.min.time()))


# 9. Write a Python program to print the next 5 days starting today

# 9. Bu gündən başlayaraq növbəti 5 günü çap etmək üçün Python proqramı yazın

# import datetime

# def  next_5_days_star_today(n):
#     cur_time = datetime.datetime.today()
#     for i in range(n):
#         film_time = datetime.datetime(cur_time.year, cur_time.month, cur_time.day, hour= 19, minute=0) + datetime.timedelta(days=i, hours=i)
#         print(film_time.strftime("%d-" "%m-" "%Y " "Time_%H:" "%M"))

# num = 5
# next_5_days_star_today(num)


# 10. Write a Python program to add 5 seconds to the current time. Go to the editor
# Sample Data :
# 13:28:32.953088
# 13:28:37.953088

# 10. Cari vaxta 5 saniyə əlavə etmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə Məlumat:
# 13:28:32.953088
# 13:28:37.953088


# import datetime

# cur_time = datetime.datetime.now()
# print(cur_time.time().strftime("%H:" "%M:" "%S"))
# cur_time_5sec = cur_time + datetime.timedelta(0, 5)
# print(cur_time_5sec.time().strftime("%H:" "%M:" "%S"))



# import datetime
# x= datetime.datetime.now()
# y = x + datetime.timedelta(0,5)
# print(x.time())
# print(y.time())

# import datetime
# given_time = datetime.datetime(1,1,1,13,28,32, 953088)
# print(given_time.strftime("%H:" "%M:" "%S:" "%f"))
# result = (given_time +datetime.timedelta(0,5)).strftime("%H:" "%M:" "%S:" "%f")
# print(result)
    

# 11. Write a Python program to convert Year/Month/Day to Day of Year in Python.

# 11. Python-da İl/Ay/Günü İlin Gününə çevirmək üçün Python proqramı yazın

# import datetime
# import calendar

# cur_time = datetime.datetime(2023, 2, 19).strftime("%j")
# print(cur_time)


# import datetime
# today = datetime.datetime.now()
# day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
# print(day_of_year)




# # import datetime
# import datetime
# # create two dates with year, month, day, hour, minute, and second
# date1 = datetime.date(2017, 6, 21)
# date2 = datetime.date(2017, 5, 16)

# # Difference between two dates
# diff = (date1-date2)
# print("Difference: ", diff)
# print("Difference: ", diff.days, "days")



# 12. Write a Python program to get the current time in milliseconds in Python

# 12. Python dilində cari vaxtı millisaniyələrlə almaq üçün Python proqramı yazın

# import time

# def current_milli_time():
#     return round(time.time() * 1000)

# print(current_milli_time())


# import time
# milli_sec = int(round(time.time() * 1000))
# print(milli_sec)




# 13. Write a Python program to get the week number. Go to the editor
# Sample Date : 2015, 6, 16
# Expected Output : 25

# 13. Həftə nömrəsini almaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə Tarixi : 2015, 6, 16
# Gözlənilən Nəti


# import datetime

# date_ = datetime.datetime(2015, 6, 16)
# date_week_num = date_.isocalendar().week
# print(date_week_num)
# date_week_num = date_.strftime("%W") #?????????????????????????????????????????????
# print(date_week_num)
# date_week_num = date_.isocalendar()[1] #?????????????????????????????????????????????
# print(date_week_num)
# #?????????????????????????????????????????????

import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])






# 14. Write a Python program to find the date of the first Monday of a given week. Go to the editor
# Sample Year and week : 2015, 50
# Expected Output : Mon Dec 14 00:00:00 2015

# 14. Verilən həftənin ilk bazar ertəsinin tarixini tapmaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə İl və həftə : 2015, 50
# Gözlənilən Nəticə : Bazar ertəsi 14 dekabr 00:00:00 2015






