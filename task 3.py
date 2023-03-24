# a = input()

# b = input()

# c = input()

# print(a + b +c)

# a, b, c =input().split(" ")

#a = input()
#b = input()
#c = input()

# print(a, b, c)

# print("{} {} {}".format(a, b, c))

# print("{}+{}+{}".format(a, b, c))

# print("{2}+{0}+{1}".format(a, b, c))


# print("%s %s" % (a, b, c))



# k = int(input())

# l = int(input())

# print("%d%d" % (k, l))

# k, l = int(input()), int(input())

# print("%d%d" % (k, l))

# print("%d %d" % (k, l))



# k, l = input().split()

# k, l = int(k), int(l)

# print("%d %d" % (k, l))

# print("%d9%d" % (k, l))




# a = int(input())

# print("Menim  %d yasim var." % (a))



# f  = float(input())

# print("%f" % (f))

# print("%.2f" % (f))

# print("%.4f" % (f))


# print("{}".format(f))


# ad = "Idrak"

# soyad = "Seyfullayev"

# yas = 35


# print("{1} {0}in {2} yasi var.".format(ad, soyad, yas))

# ad = input()

# soyad = input()

# yas = int(input())


# print("{1} {0}in {2} yasi var.".format( ad.capitalize(), soyad.capitalize(), yas))

# print("%s %sin %d yasi var" % (soyad, ad, yas))

# print(f"{soyad} {ad}in {yas} yasi var.")


# print(ad, soyad, yas, end=".", sep=",")

# print(ad, end=" ")
# print(soyad, end=" ")
# print(yas, end=" ")









#### Input/Output ####

# input() ==> Konsoldan (terminaldan) qiymet almaq ucun istifade edilir
# input() funksiyasinin qiymeti str tipinde olur.
# meselen

# a1 = input()

# print(a1)


# print() ==> Konsola (terminala) qiymet capa vermek ucun istifade edilir.
# print() funksiyasinda stringler 3 formada formatlanir.
# 1. format() funksiyasindan istifade ederek:
# meselen

# ad = input()
# soyad = input()

# ve ya

# ad, soyad = input().split(" ")

# print("{} {}".format(ad, soyad)) # ve ya
# print("{0} {1}".format(ad, soyad))

# 2. % simvolundan istifade ederek
# meselen

# print("%s %s" % (ad, soyad)) 

# print("%d %d" % (ad, soyad)) 

# print("%f %f" % (ad, soyad)) 

# 3. f simvolundan istifade ederek
# meselen

# print(f"{ad} {soyad}")

# print funksiyasinin end ve sep parametrleri var.
# meselen

# print(ad, end=" ") # sonda bosluq qoyur
# print(soyad, end=",") # sonda vergul qoyur

# print(ad, soyad, sep=", ") # deyisenler arasinda vergul ve bosluq qoyur



# a1 = input()

# print(a1)


# ad = input()

# soyad = input()

# ad, soyad = input().split(" ")

# print("{} {}".format(ad, soyad))

# print('{}{}'.format(ad, soyad))

# print("{1} {0}in dersleri".format(ad, soyad))


# ad = input()

# soyad = input()

# gtr ="%s %s" % (ad, soyad)

# print(gtr)

# print("%s %s" % (ad, soyad)) 



# reqem = 56

# reqem1 = 78

# print(reqem, reqem1)

# print("%d%d" % (reqem, reqem1))        #bu ne demekdir?



# reqem = int(input())

# reqem1 = int(input())

# print(reqem, reqem1)

# print("%d3%d" % (reqem, reqem1))


# j5 = float(input())

# j6 = float(input())

# print("%d %d" % (j5, j6))     #yoxladim integer verdi?????



# j5 = float(input())

# j6 = float(input())

# print("%f#%f" % (j5, j6))   #bu sekilde niye verdi?



# y1 = input()

# y2  = input()

# print(f"{y1, y2}")        #bu ne demekdir?


# y1 = input()

# y2  = input()

# print(f"{y1}in {y2}u")



# y1 = int(input())

# y2  = int(input())

# print(f"{y1}in {y2}u")



# y1 = float(input())

# y2  = float(input())

# print(f"{y1}in {y2}u")


# y1, y2 = input().split()

# y1, y2 = float(y1), float(y2)      #  bunu anlamadim?


# print(f"{y1}{y2}")



# k, l = input().split()

# k, l = int(k), int(l)

# print("%d %d" % (k, l))      #  bunu anlamadim?



# ad1 = "Idrak"

# soyad1 = "Seyfullayev"

# yas1 = "35"


# print(ad1, soyad1, yas1)   

# print(ad1 + " " + soyad1 + " " + yas1)   # bunlar eyni seydi?

# print(ad1, soyad1, yas1, sep=" ")          # bunlar eyni seydi?

# print(ad1, soyad1, yas1, end="")      #bu niye bele olur?

# print(ad1, soyad1, yas1, end=".")        #bu niye bele olur?

# print(ad1, soyad1, yas1, end="$")        #bu niye bele olur?



# print(ad1, soyad1, yas1, sep="")

# # print(ad1 + soyad1 + yas1)              # bunlar eyni seydi?

# print(ad1, soyad1, yas1, sep="u")


# print(ad1, soyad1, yas1, sep="u", end="u")



ad4 = "Idrak"

soyad4 = "Seyfullayev"

yas4 = "35"

print(ad4, end="\n.")     #  noqte qoysun amma yuxari qaldirmasin?
print(soyad4)
# print(soyad4)

# print(yas4) 







                               #Ev tapşırıqları  Dərs 3. Input/Output. 

# 1. Konsoldan (terminaldan) 2 str tipli dəyişən daxil edin. Bu dəyişənlərin ilk simvolunu böyük
# hərflə format() funksiyasından istifadə edərək arasında boşluq qoyaraq çapa verin.



a1 = input()

b1 = input()

a1, b1 = input().split()

print("{} {}".format(a1.capitalize(), b1.capitalize()))



# 2. Konsoldan 3 str tipli dəyişən daxil edin. Bu dəyişənləri format() funksiyasından istifadə edərək
# tərs sıra ilə böyük hərflərlə çapa verin.

a2= input()

b2= input()

c2= input()

a2, b2 , c2 = input().split()

print("{2}{1}{0}".format(a2.capitalize(), b2.capitalize(), c2.capitalize()))




# 3. Konsolda yanaşı 2 qiymət daxil edin və bu qiymətləri int tipinə çevirərək cəmini, fərqini,
# hasilini, nisbətini, tam nisbətini aşağıdakı kimi çapa verin:
# Meselen, daxil edilsin: 5 3
# Çapa verilsin:
# Cem : 5 + 3 = 8
# Ferq : 5 – 3 = 2
# Hasil : 5 * 3 = 15
# Nisbet : 5 / 3 = 1.777
# Tam nisbet : 5 // 3 = 1

a3, b3 = input().split()

a3, b3 = int(a3), int(b3)


print((f"{a3} + {b3} = {a3+b3}"))  

print((f"{a3} - {b3} ="), (a3-b3))  

print((f"{a3} * {b3} ="), (a3*b3))  

print((f"{a3} / {b3} ="), (a3/b3))  

print((f"{a3} // {b3} ="), (a3//b3)) 





# 4. Konsoldan 1 str tipli qiymət daxil edin və % simvolundan istifadə edərək bu dəyişəni böyük
# hərflərlə, kiçik hərflərlə çapa verin.


a4 = input()



print("%s" % (a4.swapcase()))





# 5. Konsolda 2 str tipli qiymət daxil edin və % simvolundan istifadə edərək 1-ci dəyişənin ilk iki, 2-
# ci dəyişənin son 2 simvolunu və bu simvolları birləşdirərərək çapa verin.



a5 = input()

b5 = input()

a5, b5 = input().split()

print("%s%s" % (a5[0:2], b5[-2:]))





# 6. Konsoldan 1 str tipli qiymət daxil edin və f simvolundan istifadə edərək bu dəyişəni boşluq
# simvoluna görə parçalayaraq çapa verin.



a6 = input().split()

print(f"{a6}")




# 7. Konsoldan kitabın adı, müəllifin adı və kitabın səhifə sayını daxil edin və onları f simvolundan
# istifadə edərək aşağıdakı kimi çapa verin:
# Daxil edilsin:
# Oyunbaz
# Vulf Dorn
# 452
# Çap edilsin:
# Mağazada Vulf Dornun 452 səhifəlik Oyunbaz kitabı mövcuddur.


kitabin_adi7= input()

muellifin_adi7= input()

kitabin_sehife_sayi= int(input())

print(f"Magazada {muellifin_adi7}un {kitabin_sehife_sayi} sehifelik {kitabin_adi7} kitabi movcuddur.")




# 8. Konsoldan yanaşı 3 str tipli dəyişən daxil edin və onları hər 3 formatlama üsulundan istifadə
# edərək aşağıdakı kimi daxil edin:
# Daxil edilsin:
# Bakı Sumqayıt Gəncə
# Çap edilsin:
# Bakı, Sumqayıt, Gəncə Azərbaycanın ən böyük şəhərləridir.


a8, b8, c8 = input().split()


print("{}, {}, {} Azerbaycanin en boyuk seherleridir.".format(a8, b8, c8))


print("%s, %s, %s Azerbaycanin en boyuk seherleridir." % (a8, b8, c8))


print(f"{a8}, {b8}, {c8} Azerbaycanin en boyuk seherleridir.")





# 9. Konsoldan yanaşı 3 int tipli dəyişən daxil edin və end parametrindən istifadə edərək onları
# yanaşı çapa verin.



a9, b9, c9 = input().split()

a9, b9, c9 = int(a9), int(b9), int(c9)

print(a9, end=" ")                             # /n    ne idi?????

print(b9, end=" ")

print(c9)





# 10. Konsoldan yanaşı 3 float tipli dəyişən daxil edin və sep parametrindən istifadə edərək onları
# vergüllə ayıraraq çapa verin.




a10, b10, c10 = input().split()

a10, b10, c10 = float(a10), float(b10), float(c10)

print(a10, b10, c10, sep=",")









