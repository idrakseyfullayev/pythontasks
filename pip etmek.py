# import calendar
# import datetime
# import os # operating system - emeliyyat sistemi bagli meseleler
# import sys  # system - python ile bagli meseleler
# import platform # komputerle bagli meseleler
# import socket  # sebeke ile bagli meseleler
# import datetime # vaxt ve zamanla bagli meseleler
# import calendar # teqvimle bagli meseleler

# now = datetime.datetime.now() # cari vaxti qaytarir
# print(calendar.month(now.year, now.month)) # cari vaxtin teqvimini qaytarir
# print(now.year) # cari ili qaytarir
# print(now.month) # cari ayi qaytarir
# print(now)


# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=VtwR3Di1D6M")
# print(yt.title.title())
# print(yt.thumbnail_url)
# print(yt.captions.get_by_language_code('en'))
# print(yt.streams.first().download())

import pywhatkit

pywhatkit.sendwhatmsg_instantly(
    phone_no="", 
    message="bu mesaj size Idrak terefinden python proqramlasdirma dilinin komeyi ile automatic qaydada gonderildi"
)


# pywhatkit.sendwhatmsg(
#     phone_no="+994556532437", 
#     message="This is a scheduled message.",
#     time_min=2
# )


# a = 5
# print(a)



