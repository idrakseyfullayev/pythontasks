# This module allows you to output calendars like the Unix cal program and provides additional useful functions
# related to the calendar. By default, these calendars have Monday as the first day of the week, and Sunday as
# the last (the European convention). Use setfirstweekday() to set the first day of the week to Sunday (6) or
# to any other weekday. Parameters that specify dates are given as integers. For related functionality, see 
# also the datetime and time modules.

# Bu modul Unix cal proqramı kimi təqvimlər çıxarmağa imkan verir və təqvimlə bağlı əlavə faydalı funksiyaları
# təmin edir. Varsayılan olaraq, bu təqvimlərdə həftənin ilk günü bazar ertəsi, sonuncu isə bazar günü 
# (Avropa konvensiyası) var. Həftənin ilk gününü bazar gününə (6) və ya hər hansı digər iş gününə təyin etmək 
# üçün setfirstweekday() funksiyasından istifadə edin. Tarixləri təyin edən parametrlər tam ədədlər kimi verilir.
# Müvafiq funksionallıq üçün tarix və vaxt modullarına da baxın.


# iterweekdays() method -  Bir həftə ərzində istifadə olunacaq həftə içi nömrələr üçün iteratoru qaytarın.
# import calendar
# #set firstweekday=0
# cal= calendar.Calendar(firstweekday=0)
# for x in cal.iterweekdays():
# 	print(x)

# itermonthdates() method - itermonthdates() metodu ilin ilin ay ayı (1-12) üçün iteratoru qaytarmaq üçün istifadə olunur.
# import calendar
# cal= calendar.Calendar()
# for x in cal.itermonthdates(2016, 5):
# 	print(x)

# itermonthdays2() method - itermonthdays2() metodu itermonthdates() kimi ilin ay ayı üçün iteratoru qaytarmaq üçün
#  istifadə olunur.
# import calendar
# cal= calendar.Calendar()
# for x in cal.itermonthdays2(2016, 5):
# 	print(x)

# itermonthdays() method - itermonthdays() metodu itermonthdates() kimi ilin ay ayı üçün iteratoru qaytarmaq üçün
#  istifadə olunur.
# import calendar
# cal= calendar.Calendar()
# for x in cal.itermonthdays(2016, 5):
#   print(x)

# monthdatescalendar() method - 
# monthdatescalendar() metodu ilin ayındaki həftələrin siyahısını tam həftələr kimi qaytarmaq üçün istifadə olunur
# . Həftələr yeddi datetime.date obyektinin siyahısıdır.
# import calendar
# cal= calendar.Calendar()
# print(cal.monthdatescalendar(2016, 5))

# monthdays2calendar() method - monthdays2calendar() metodu ilin ay ayında həftələrin siyahısını tam həftələr kimi
# qaytarmaq üçün istifadə olunur. Həftələr yeddi gün nömrələrinin və həftə içi nömrələrin siyahısıdır.
# import calendar
# cal= calendar.Calendar()
# print(cal.monthdays2calendar(2016, 5))

# monthdayscalendar() method - monthdayscalendar() metodu ilin ay ayında həftələrin siyahısını tam həftələr kimi
# qaytarmaq üçün istifadə olunur. Həftələr yeddi günlük nömrələrin siyahısıdır
# import calendar
# cal= calendar.Calendar()
# print(cal.monthdayscalendar(2016, 5))

# yeardatescalendar() method - Yeardatescalendar() metodu müəyyən edilmiş il üçün məlumatları formata hazır
# şəkildə qaytarmaq üçün istifadə olunur. Qaytarılan dəyər ay sətirlərinin siyahısıdır
# import calendar
# cal= calendar.Calendar()
# print(cal.yeardatescalendar(2016, 3))

# yeardays2calendar() method - Yeardays2calendar() metodu müəyyən edilmiş il üçün məlumatı formata hazır şəkildə
# qaytarmaq üçün istifadə olunur (yeardatescalendar() ilə oxşar).
# import calendar
# cal= calendar.Calendar()
# print(cal.yeardays2calendar(2016, 5))


# yeardayscalendar() method - Yeardayscalendar() metodu müəyyən edilmiş il üçün məlumatı formata hazır şəkildə 
# qaytarmaq üçün istifadə olunur (yeardatescalendar() ilə oxşar)
# import calendar
# cal= calendar.Calendar()
# print(cal.yeardayscalendar(2016, 5))

# text-calendar-formatmonth() method - Formatmonth() metodu çox sətirli sətirdə bir ayın təqvimini qaytarmaq üçün
# istifadə olunur.
# import calendar
# tc= calendar.TextCalendar(firstweekday=0)
# print(tc.formatmonth(2016, 5))

# text-calendar-prmonth() method - prmonth() metodu formatmonth() tərəfindən qaytarılan bir ayın təqvimini çap etmək
# üçün istifadə olunur.
# import calendar
# tc= calendar.TextCalendar(firstweekday=0)
# print(tc.prmonth(2016, 5))

# text-calendar-formatyear() method - Formatyear() metodu m-sütunlu təqvimi çox sətirli sətir kimi bütün il üçün 
# qaytarmaq üçün istifadə olunur.
# import calendar
# tc= calendar.TextCalendar(firstweekday=0)
# print(tc.formatyear(2016, 5))

# text-calendar-pryear() method - Pryear() metodu formatyear() tərəfindən qaytarıldığı kimi bütün il üçün təqvimi 
# çap etmək üçün istifadə olunur.
# import calendar
# tc= calendar.TextCalendar(firstweekday=0)
# print(tc.pryear(2016, 5))

# html-calendar-formatmonth() method - formatmonth() metodu bir ayın təqvimini HTML cədvəli kimi qaytarmaq üçün
# istifadə olunur.
# import calendar
# tc= calendar.HTMLCalendar(firstweekday=0)
# print(tc.formatmonth(2016, 5))

# html-calendar-formatyear()method - Formyear() metodu bir ilin təqvimini HTML cədvəli kimi qaytarmaq üçün
# istifadə olunur.
# import calendar
# tc= calendar.HTMLCalendar(firstweekday=0)
# print(tc.formatyear(2016, 3))

# html-calendar-formatyearpage() method - Formatyearpage() metodu bir ilin təqvimini tam HTML səhifəsi kimi
# qaytarmaq üçün istifadə olunur
# import calendar
# tc= calendar.HTMLCalendar(firstweekday=0)
# print(tc.formatyear(2016, 3))

# setfirstweekday() method - Hər həftənin başlaması üçün iş gününü təyin edir (0 bazar ertəsi, 6 bazar günü).
# import calendar
# x = calendar.setfirstweekday(calendar.SUNDAY)
# print(x)

# isleap() method - isleap() metodu əgər il sıçrayış ilidirsə True, əks halda isə False qaytarmaq üçün
# istifadə olunur.
# import calendar
# print(calendar.isleap(2016))

# leapdays() method - leapdays() metodu y1 və y2-nin illər olduğu y1-dən y2 (eksklüziv) diapazonunda sıçrayış
# illərinin sayını qaytarmaq üçün istifadə olunur.
# import calendar
# print(calendar.leapdays(2015, 2018))


# weekday() method - Weekday() metodu il (1970–...), ay (1–12), gün (1–31) üçün həftənin gününü (0 Bazar ertəsi)
# qaytarmaq üçün istifadə olunur.
# import calendar
# print(calendar.weekday(2016, 5, 15))

# weekheader() method - Weekheader() metodu qısaldılmış iş günləri adlarını ehtiva edən başlığı qaytarmaq üçün
# istifadə olunur. n bir iş günü üçün simvollarla genişliyi təyin edir.
# import calendar
# print(calendar.weekheader(3))

# monthrange() method - monthrange() metodu müəyyən il və ay üçün ayın ilk gününün iş gününü və ayda günlərin
# sayını qaytarmaq üçün istifadə olunur.
# import calendar
# print(calendar.monthrange(2016,5))

# monthcalendar() method - monthrange() metodu bir ayın təqvimini təmsil edən matrisi qaytarmaq üçün istifadə olunur.
# import calendar
# print(calendar.monthcalendar(2016,5))

# prmonth() method - prmonth() metodu, month() tərəfindən qaytarılan bir ayın təqvimini çap etmək üçün
# istifadə olunur.
# import calendar
# print(calendar.prmonth(2016,5))

# month() method - month() metodu TextCalendar sinifinin formatmonth() funksiyasından istifadə edərək çoxsətirli
# sətirdə bir ayın təqvimini qaytarmaq üçün istifadə olunur.
# import calendar
# print(calendar.month(2016,5))

# prcal() method - prcal() metodu təqvimi təqvim() tərəfindən qaytarıldığı kimi bütün il üçün çap etmək üçün
# istifadə olunur.
# import calendar
# print(calendar.prcal(2016))

# calendar() method - Calendar() metodu TextCalendar sinfinin formatyear() funksiyasından istifadə edərək bütün 
# il üçün 3 sütunlu təqvimi çoxsətirli sətir kimi qaytarmaq üçün istifadə olunur.
# import calendar
# print(calendar.calendar(2016))



























































