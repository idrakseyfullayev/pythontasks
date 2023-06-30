#                                 programiz.com-files-16       

# 1. Python Program to Merge Mails

# Poçtları Birləşdirmək üçün Python Proqramı
# Bu proqramda siz məktubları birinə birləşdirməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# String üsulları
# Python Fayl I/OPython Fayl Əməliyyatı
# Eyni dəvətləri bir çox insana göndərmək istədikdə poçtun mətni dəyişmir. Yalnız adı (və bəlkə də ünvanı)
# dəyişdirmək lazımdır.

# Poçt birləşməsi bunu etmək üçün bir prosesdir. Hər bir məktubu ayrıca yazmaq əvəzinə, məktubun mətni üçün
# şablonumuz və bütün məktubları yaratmaq üçün birləşdirdiyimiz adların siyahısı var.

# Poçtları Birləşdirmək üçün Mənbə Kodu



# Python program to mail merger
# Names are in the file names.txt
# Body of the mail is in body.txt

# open names.txt for reading
with open("names.txt", 'r', encoding='utf-8') as names_file:

    # open body.txt for reading
    with open("body.txt", 'r', encoding='utf-8') as body_file:

        # read entire content of the body
        body = body_file.read()

        # iterate over names
        for name in names_file:
            mail = "Hello " + name.strip() + "\n" + body

            # write the mails to individual files
            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)


# 2.Python Program to Find the Size (Resolution) of a Image

# Şəklin Ölçüsünü (Qətiyyətini) Tapmaq üçün Python Proqramı
# Xarici kitabxanalardan istifadə etmədən bu nümunədə jpeg şəklinin həllini tapmağı öyrənəcəksiniz

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Funksiyaları
# Python İstifadəçi tərəfindən təyin olunan funksiyalar
# Python Fayl I/OPython Fayl Əməliyyatı
# JPEG ("jay-peg" kimi oxunur) Birgə Fotoqrafiya Ekspertlər Qrupu deməkdir. Bu, təsvirin sıxılması üçün
# ən çox istifadə edilən sıxılma üsullarından biridir.

# Fayl formatlarının əksəriyyətində fayl haqqında faydalı məlumatları ehtiva edən başlıqlar 
# (ilkin bir neçə bayt) var.

# Məsələn, jpeg başlıqlarında hündürlük, genişlik, rəng sayı (boz və ya RGB) və s.

# JPEG Şəklin Tapılma Qətiyyətinin Mənbə Kodu


def jpeg_res(filename):
   """This function prints the resolution of the jpeg image file passed into it"""
   """Bu funksiya ona ötürülən jpeg şəkil faylının həllini çap edir"""
   

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

       # height of image (in 2 bytes) is at 164th position
       img_file.seek(163)

       # read the 2 bytes
       a = img_file.read(2)

       # calculate height
       height = (a[0] << 8) + a[1]

       # next 2 bytes is width
       a = img_file.read(2)

       # calculate width
       width = (a[0] << 8) + a[1]

   print("The resolution of the image is",width,"x",height)

# jpeg_res("img1.jpg")


# Bu proqramda görüntünü binar rejimdə açdıq. Qeyri-mətn faylları bu rejimdə açıq olmalıdır. Şəklin
# hündürlüyü 164-cü mövqedədir, sonra şəklin eni. Hər ikisi 2 bayt uzunluğundadır.

# Qeyd edək ki, bu yalnız JPEG Fayl Mübadilə Formatına (JFIF) aiddir. Şəkliniz digər standart
# (məsələn, EXIF) ilə kodlaşdırılıbsa, kod işləməyəcək.

# Biz << bit istiqamətində dəyişdirmə operatorundan istifadə edərək 2 baytı ədədə çeviririk. Nəhayət, 
# qətnamə göstərilir.




# 3. Python Program to Find Hash of File

# Fayl Hash tapmaq üçün Python proqramı
# Bu yazıda siz faylın hashini tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Funksiyaları
# Python İstifadəçi tərəfindən təyin olunan funksiyalar
# Python Fayl I/OPython Fayl Əməliyyatı
# Hash funksiyaları ixtiyari miqdarda məlumat alır və sabit uzunluqlu bit sətrini qaytarır. Funksiyanın çıxışı
# həzm mesajı adlanır.

# Onlardan autentifikasiya məqsədləri üçün kriptoqrafiyada geniş istifadə olunur. MD5, SHA-1 və s. kimi bir
#  çox heşinq funksiyaları var. Kriptoqrafiyada hash funksiyaları haqqında daha çox bilmək üçün bu səhifəyə baxın.

# Bu nümunədə bir faylı necə hash etmək lazım olduğunu göstərəcəyik. SHA-1 hashing alqoritmindən istifadə 
# edəcəyik. SHA-1 həzminin uzunluğu 160 bitdir.

# Biz fayldakı məlumatları birdən-birə qidalandırmırıq, çünki bəzi fayllar bir anda yaddaşa sığmaq üçün
#  çox böyükdür. Faylın kiçik hissələrə bölünməsi proses yaddaşını səmərəli edəcək.

# Hash tapmaq üçün mənbə kodu


# Python program to find the SHA-1 message digest of a file

# importing the hashlib module
# import hashlib

# def hash_file(filename):
#    """"This function returns the SHA-1 hash
#    of the file passed into it"""

#    # make a hash object
#    h = hashlib.sha1()



# #    open file for reading in binary mode
#    with open(filename,'rb') as file:

#        # loop till the end of the file
#        chunk = 0
#        while chunk != b'':
#            # read only 1024 bytes at a time
#            chunk = file.read(1024)
#            h.update(chunk)

#    # return the hex representation of digest
#    return h.hexdigest()

# message = hash_file("track1.mp3")
# print(message)

# Bu proqramda faylı binar rejimdə açırıq. Hash funksiyaları hashlib modulunda mövcuddur. Bir müddət döngəsindən
#  istifadə edərək faylın sonuna qədər dövrə vururuq. Sona çatdıqda boş bayt obyekti alırıq.

# Hər iterasiyada biz fayldan yalnız 1024 bayt oxuyuruq (bu dəyər bizim istəyimizə uyğun olaraq dəyişdirilə bilər)
#  və hashing funksiyasını yeniləyirik.

# Nəhayət, hexdigest() metodundan istifadə edərək həzm mesajını onaltılıq təmsildə qaytarırıq.


# 4 ?????????????????????????????????????????????????????????????????????????????????


# 5. Python Program to Catch Multiple Exceptions in One Line

# Bir sətirdə çoxlu istisnaları tutmaq üçün Python proqramı
# Bu nümunədə bir sətirdə çoxlu Python istisnalarını tutmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Əsas Giriş və Çıxış
# Python İstisnaları
# Python İstisna İdarəetmə
# Bir dəstdən istifadə edərək bir çox istisnalar tutula bilər. Səhvlər aşağıdakı nümunədə göstərildiyi kim
# bir dəstdən keçirilə bilər.

# Mötərizəli dəst kimi çoxsaylı istisnalar


# string = input()

# try:
#     num = int(input())
#     print(string+num)
# except (TypeError, ValueError) as b:
#     print(b)


# 6. Python Program to Copy a File   

# Faylı Kopyalamaq üçün Python Proqramı
# Bu nümunədə siz Python istifadə edərək faylın məzmununu başqa fayla köçürməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı

# Shutil modulundan istifadə

# from shutil import copyfile
# copyfile("Python\\body.txt", "Python\\names.txt") # ???????????  \b gore problem yaranir??????



# copyfile() funksiyasının birinci parametri mənbə faylın yolu, ikinci parametr isə təyinat faylının yoludur. 
# Təyinat faylının məzmunu mənbə faylın məzmunu ilə əvəz olunur.

# Bəzi metadata dəyişiklikləri ilə eyni məqsədə xidmət edən copy(), cop2() və copyfileobj() başqa üsulları 
# da var.





# 7.Python Program Read a File Line by Line Into a List
# Python Proqramı Fayl Sətirini Siyahıya Oxuyun
# Bu nümunədə siz faylı sətir-sətir siyahıda oxumağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı
# Misal 1: Readlines() istifadə
# data_file.txt faylının məzmunu olsun

# honda 1948
# mercedes 1926
# ford 1903
# Mənbə kodu


# with open("Python\car.txt") as file:
#    list1 = file.readlines()
# print(list1)



# list2 =[]
# for i in list1:
#    if "\n" in i:
#       i = i[0:-2]
#    list2.append(i)
# print(list2)

# for i in list2:
#    print(i)


# with open("Python\car.txt") as file:
#    list1 = file.readlines()

# print(list1)

# list2 = list(map(lambda x: x[0:-2], list1))
# print(list2)
# print("\n".join(list2))


# with open("Python\car.txt") as file:
#    list1 = file.readlines()
# print(list1)
# list2 = "".join(list1).split("\n")
# print(list2)
# print("\n".join(list2))



# with open("Python\car.txt") as f:
#     content_list = f.readlines()

# # print the list
# print(content_list)

# # remove new line characters
# content_list = [x.strip() for x in content_list]  # burda \n yazmadan \n-i legv edib nece?????????/
# print(content_list)

# readlines() fayldan sətirlərin siyahısını qaytarır.
# Əvvəlcə faylı açın və readlines() istifadə edərək faylı oxuyun.
# Yeni sətirləri ('\n') silmək istəyirsinizsə, strip() funksiyasından istifadə edə bilərsiniz.



# with open('Python\car.txt') as f:
#     content_list = [line for line in f]

# print(content_list)

# # removing the characters
# with open('Python\car.txt') as f:
#     content_list = [line.rstrip() for line in f]

# print(content_list)





# 8.Python Program to Append to a File
# Fayla əlavə etmək üçün Python proqramı
# Bu nümunədə siz fayla əlavə etməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı
# Faylı əlavə rejimində açın və ona yazın
# my_file.txt faylının məzmunu belədir

# honda 1948
# mercedes 1926
# ford 1903

# with open("Python\car.txt", "a") as t:
#     x = t.write("\ntoyota 2023")
# print(x)    

# with open("Python\car.txt", "r") as f:
#     list1 = f.readlines()
# print(list1)    
# list2 = list(map(lambda x: x.removesuffix("\n"), list1))    
# print(list2)    


# with open("Python\car.txt", "a") as f:
#    f.write("new text")





# 9. Python Program to Extract Extension From the File Name
# Fayl adından genişlənmə çıxarmaq üçün Python proqramı
# Bu nümunədə siz fayl adından uzantı çıxarmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Kataloq və Faylların İdarə Edilməsi
# Python Fayl I/OPython Fayl Əməliyyatı
# Misal 1: Os modulundan splitext() metodundan istifadə

# import os

# file_details = os.path.splitext("Python\car.txt")      # path nedir ki burda class-a oxsamir????
# print(file_details)  # ('Python\\car', '.txt') bele niye cap olunur 2 eded slash??
# print(file_details[1])

# os.path.splitext() faylın adı kimi bir elementi yol ilə birlikdə, digəri isə faylın uzantısıdır.
# Yalnız fayl uzantısını istəyirsinizsə, onu yuxarıda göstərildiyi kimi çap edə bilərsiniz file_details[1].




# Example 2: Using pathlib module
# import pathlib
# print(pathlib.Path('/path/file.ext').suffix)


# pathlib modulundan şəkilçi atributundan istifadə etməklə biz faylın genişləndirilməsini əldə edə bilərik.
# Yuxarıdakı misalda .ext fayl.ext faylının uzantısıdır.




# 10. Python Program to Get the File Name From the File Path

# Fayl yolundan fayl adını almaq üçün Python proqramı
# Bu nümunədə siz fayl yolundan fayl adını almağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı
# Python sətirləri
# Misal 1: Os modulundan istifadə


# import os
# name_file = os.path.basename("Python\car.txt")
# print(name_file)
# print((os.path.splitext(name_file)[0]))



# import os

# # file name with extension
# file_name = os.path.basename('Python\car.txt')
# print(file_name)

# # file name without extension
# print(os.path.splitext(file_name)[0])

# basename() yolun son fayl/qovluğunun adını verir, splitext() isə fayl adını fayl adına və uzantıya bölür.



# import os
# file_name = os.path.basename('Python\car.txt')
# print(file_name)
# print(os.path.splitext(file_name))




# Example 2: Using Path module

# from pathlib import Path

# print(Path('Python\car.txt').stem)

# Path modulunun kök atributundan istifadə etməklə fayl adı yuxarıda göstərildiyi kimi çıxarıla bilər.
# Python 3.4 və daha yuxarı versiyalar üçün işləyir.




# 11.Python Program to Get Line Count of a File
# Faylın sətir sayını əldə etmək üçün Python proqramı
# Bu nümunədə siz faylın sətir sayını almağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python enumerate()
# Python Fayl I/OPython Fayl Əməliyyatı
# Döngü üçün Python
# Misal 1: for loopundan istifadə
# my_file.txt faylının məzmunu belədir

# honda 1948
# mercedes 1926
# ford 1903
# Mənbə kodu


# with open("Python\car.txt","r") as file:
#    text = file.readlines()
# print(text)

# len_text = 0
# for i in text:
#    pass
#    len_text += 1
# print(len_text)   


# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1

# print(file_len("Python\car.txt"))

# For döngəsindən istifadə edərək faylın sətirlərinin sayını hesablamaq olar.
# Faylı yalnız oxumaq rejimində açın.
# For döngəsindən istifadə edərək f obyektini təkrarlayın.
# Hər iterasiyada bir sətir oxunur; buna görə də hər iterasiyadan sonra döngə dəyişəninin dəyərini artırın.


# Example 2: Using list comprehension

# num_of_lines = sum(1  for l in open('Python\car.txt'))

# print(num_of_lines)

# Faylı yalnız oxumaq rejimində açın.
# For döngəsindən istifadə edərək open('my_file.txt') vasitəsilə təkrarlayın.
# Hər iterasiyadan sonra 1-i qaytarın.
# Qaytarılan dəyərlərin cəmini tapın.





# 12.Python Program to Find All File with .txt Extension Present Inside a Directory
# Kataloqda mövcud olan .txt genişlənməsi ilə bütün faylları tapmaq üçün Python proqramı
# Bu nümunədə siz qovluqda mövcud olan .txt uzantılı bütün faylları tapmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı
# Python Kataloq və Faylların İdarə Edilməsi
# Döngü üçün Python
# Nümunə 1: Qlobdan istifadə

# Example 1: Using glob
# import glob, os

# os.chdir("Python")

# for file in glob.glob("*.txt"):
#     print(file)

# Glob modulundan istifadə edərək müəyyən uzantıları olan faylları axtara bilərsiniz.
# os.chdir("my_dir") cari iş qovluğunu /my_dir olaraq təyin edir.
# for loopundan istifadə edərək glob() istifadə edərək .txt uzantılı faylları axtara bilərsiniz.
# * verilmiş uzantılı bütün faylları bildirir.


# Example 2: Using os
# import os

# for file in os.listdir("Python"):
#     if file.endswith(".txt"):
      #   print(file)

# Bu nümunədə .txt uzantısını yoxlamaq üçün endswith() metodundan istifadə edirik.
# For döngəsindən istifadə edərək, /my_dir qovluğunun hər bir faylını təkrarlayın.
# Enswith() istifadə edərək faylın .txt uzantısına malik olub olmadığını yoxlayın.


# Example 3: Using os.walk

# import os

# for root, dirs, files in os.walk("Python"):
#     for file in files:
#         if file.endswith(".txt"):
#             print(file)

# Bu nümunə os modulunun walk() metodundan istifadə edir.
# for loopundan istifadə edərək my_dir-in hər bir faylını təkrarlayın.
# Enswith() istifadə edərək faylın .txt uzantısına malik olub olmadığını yoxlayın.




# 13.Python Program to Get File Creation and Modification Date

# Fayl Yaratma və Dəyişiklik Tarixini Almaq üçün Python Proqramı
# Bu nümunədə siz faylın yaradılması və dəyişdirilmə tarixini öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı



# Example 1: Using os module

# import os.path, time
# import pathlib

# file = pathlib.Path('Python\car.txt')
# print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
# print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))

# getmtime() son modifikasiya vaxtını, getctime() isə Linux/Unix-də son metadata dəyişmə vaxtını və Windows-da
# yol yaratma vaxtını verir.

# Example 2: Using stat() method
# import datetime
# import pathlib

# fname = pathlib.Path('Python\car.txt')
# print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
# print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))

# Nümunə 1-ə bənzər, st_mtime son dəyişiklik vaxtına aiddir; halbuki, st_ctime Linux/Unix-də son metaməlumat
# dəyişikliyi vaxtına və Windows-da yaradılma vaxtına aiddir.



# 14. Python Program to Get the Full Path of the Current Working Directory
# Cari İş Kataloqunun Tam Yolunu əldə etmək üçün Python Proqramı
# Bu nümunədə siz cari iş qovluğunun tam yolunu əldə etməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Fayl I/OPython Fayl Əməliyyatı
# Python Kataloq və Faylların İdarə Edilməsi


# Example 1: Using pathlib module

# import pathlib

# # path of the given file
# print(pathlib.Path('Python\car.txt').parent.absolute())

# # current working directory
# print(pathlib.Path().absolute())

# pathlib modulundan istifadə edərək cari iş qovluğunu əldə edə bilərsiniz.
# Faylın adını Path() metodunda ötürün.
# valideyn yolun məntiqi valideynini, mütləq() isə faylın mütləq yolunu verir.
# pathlib.Path().absolute() cari iş kataloqunu verir.


# Example 2: Using os module

# import os

# # path of the given file
# print(os.path.dirname(os.path.abspath('Python\car.txt')))

# # current working directory
# print(os.path.abspath(os.getcwd()))

# Eyni şeyi OS modulu ilə edə bilərsiniz.
# Mütləq yolu əldə etmək üçün abspath() metodundan istifadə edin.
# getcwd() cari iş qovluğunu verir.



# 15.Python Program to Check the File Size

# Fayl ölçüsünü yoxlamaq üçün Python proqramı
# Bu nümunədə siz faylın ölçüsünü yoxlamağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Kataloq və Faylların İdarə Edilməsi


# Example 1: Using os module
# import os

# file_stat = os.stat('Python\car.txt')
# print(file_stat.st_size)

# Os modulundan stat() istifadə edərək, faylın təfərrüatlarını əldə edə bilərsiniz. Fayl ölçüsünü əldə etmək 
# üçün stat() metodunun st_size atributundan istifadə edin.
# Fayl ölçüsünün vahidi baytdır.


# Example 2: Using pathlib module

# from pathlib import Path

# file = Path('Python\car.txt')
# print(file.stat().st_size)

# pathlib modulundan istifadə edərək, yuxarıda göstərildiyi kimi eyni şeyi edə bilərsiniz.
# Fayl ölçüsünün vahidi baytdır.






