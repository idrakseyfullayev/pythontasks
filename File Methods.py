# #                                           Python File Methods

file = open("Python\Program\myfile.txt", "r")

with open("Python\Program\myfile.txt", "w") as file:
    data = file.write("dunya")

with open("Python\Program\myfile.txt", "a") as file:
    data = file.write("dunya")    

# #Metod                   Təsviri
file.close()         # Açılan faylı bağlayır. Fayl artıq bağlanıbsa, bunun heç bir təsiri yoxdur.
file.detach()        # Əsas binar buferi TextIOBase-dən ayırır və onu qaytarır.
file.fileno()        # Faylın tam ədədini (fayl deskriptoru) qaytarır.
file.flush()         # Fayl axınının yazma buferini təmizləyir.
file.isatty()        # Əgər fayl axını interaktivdirsə True qaytarır.
file.read()          # Fayldan ən çoxu n simvolu oxuyur. Mənfi və ya Yoxdursa, faylın sonuna qədər oxuyur.
file.readable()      # Əgər fayl axını ondan oxuna bilirsə, True qaytarır.
file.readline(n=-1)  # Fayldan bir sətir oxuyur və qaytarır. Müəyyən edilərsə, ən çox n baytda oxuyur.
file.readlines(n=-1) # Fayldan sətirlərin siyahısını oxuyur və qaytarır. Göstərildiyi təqdirdə ən çox n bayt/simvol oxuyur.
file.seek()          # Fayl mövqeyini (başlanğıc, cari, son) ilə əlaqədar olaraq ofset baytına dəyişir.
file.seekable()      # Əgər fayl axını təsadüfi girişi dəstəkləyirsə True qaytarır.
file.tell()          # Fayl obyektinin cari mövqeyini əks etdirən tam ədədi qaytarır.
file.truncate(size=None) # Fayl axınının ölçüsünü bayt ölçüsünə uyğunlaşdırır. Ölçü göstərilməyibsə, ölçüsünü cari yerə dəyişir.
file.writable()      # Əgər fayl axını ona yazıla bilirsə, True qaytarır.
file.write()         # s sətirini fayla yazır və yazılan simvolların sayını qaytarır.
file.writelines()    # Fayla sətirlərin siyahısını yazır.

from shutil import copyfile
copyfile("Python\Program\myfile.txt", "Python\g.txt")
# copyfile() funksiyasının birinci parametri mənbə faylın yolu, ikinci parametr isə təyinat faylının yoludur. 
# Təyinat faylının məzmunu mənbə faylın məzmunu ilə əvəz olunur.

