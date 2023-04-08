# text = "salam"

# a = text[0]

# print(a)


text = "siyfunlayev"

# r = text[4]

# print(r)


# v = text[-5]

# print(v)



# h = text[0:4]

# print(h)

# u = text[1:-1]

# print(u)



# t = text[:1]

# print(t)


# g = text[:-10]

# print(g)


# n = text[3::3]         #musbet yazanda soldan saga gedir

# print(n)


# l = text[0::5]           #siyfunlayev



# print(l)


#l = text[-5:-8]                #   :    bu isare o demekdir funksiya hemise soldan saga oxunur?????



# print(l)



# x = text[::-1]  #eksine cixardir          #   :    bu isare o demekdir funksiya hemise sagdan sola oxunur?????

# print(x)


# h = text[10::-1]


# print(h)






# print(text.capitalize())            #siyfunlayev

# print(text[0].capitalize())

# a = True

# b = False

# print(a + b)

# c = ""                                    # bu ne demekdir

# c = " "                                      #bu ne demekdir

# a = c + c
# print(a)




# print(bool(c))




# a = 12

# b = 13

# c = a > b

# print(c)

# c = a < b


# print(c)

# print(c)


# c = a >= b

# print(c)


# a = 12

# b = 12

# c = a == b             # menasini bir aciqlansin


# print(c)

# c = a != b             # menasini bir aciqlansin

# print(c)


a = True

b = ""


c = bool(b) - a         #  -1  olanda True verir????????

print(bool(c))


a = True

b = 35

c = "Salam"

d = a + bool(b) + bool(c)

print(bool(c))



print(d)

d = str(a + bool(b) + bool(c))


print(d)




#### String elementleri ve metodlari ####

# 1. capitalize()       Birinci simvolu böyük hərflərə çevirir
# 2. casefold()         Sətri kiçik hərflərə çevirir
# 3. count()            Müəyyən edilmiş dəyərin sətirdə neçə dəfə baş verdiyini qaytarır
# 4. endswith()         Sətir müəyyən edilmiş dəyərlə bitərsə, doğru qaytarır
# 5. format()           Sətirdə müəyyən edilmiş dəyərləri formatlayır
# 6. index()            Müəyyən edilmiş dəyər üçün sətirdə axtarış aparır və onun tapıldığı yeri qaytarır
# 7. join()             Təkrarlanan elementləri sətirə çevirir
# 8. lower()            Sətri kiçik hərflərə çevirir
# 9. replace()          Müəyyən edilmiş dəyərin müəyyən edilmiş dəyərlə əvəz edildiyi sətri qaytarır
# 10. split()           Göstərilən ayırıcıda sətri bölür və siyahını qaytarır
# 11. startswith()      Sətir müəyyən edilmiş dəyərlə başlayırsa, doğru qaytarır
# 12. strip()           Sətin kəsilmiş versiyasını qaytarır
# 13. swapcase()        Rəqəmləri dəyişdirir, kiçik hərf böyük hərf olur və əksinə
# 14. title()           Hər sözün ilk simvolunu böyük hərfə çevirir
# 15. upper()           Sətri böyük hərflərə çevirir

#### Bool deyisenler ####

# True (1), False (0)


h = "kirmanoldu irmanoldu"

p = h.capitalize()

print(p)

print(h[2].capitalize())

print(h.casefold())

print(h.casefold())



print(h.center(20, "+"))




print(h.count("kirmanoldu"))      #basa dusmedim nedir bu?


print(h.endswith("kirmanoldu irmanoldu"))

# h = "kirmanoldu {price: .2f} irmanoldu"       #anlamadim?
# print(h.format(price = 9))

print(h.index("irmanoldu"))    #hansi qaydada axtaris aparir 



                # Ev tapşırıqları Dərs 2. Stringlər, String metodları. Bool dəyişənlər

# 1. İki str tipli dəyişən götürün. Birinci dəyişənin 3-cü elementi ilə 2-ci dəyişənin sonuncu
# elementini toplayıb çapa verin.


t = "universitet"

d = "shoping"

w = t[3] + d[6]

print(w)




# 2. Str tipli dəyişənin sonuncu elementindən 2-ci elementinə kimi olan hissəsini bir
# dəyişənə yazıb çapa verin.


j = "Nerimanov"

print(j[-1:-8:-1])

z = j[-2:-7:-1]          #  onami cixmasi ucun nece etmeliyem?

print(z)



# 3. Bütün simvolları kiçik hərflə olan str tipli bir dəyişən götürün və onun tərsini (ilk
# simvolu böyük hərflə) çapa verin.


pl = "karvansaray"

ok = pl[::-1].capitalize()  

print(ok)





# 4. Str tipli dəyişəndə ilk simvolunun sayını tapın.

er = "MasalliM"

print(er.count("M"))

print(er.count(er[0]))




# 5. Str tipli bir dəyişən götürün və onun son 2 simvolunu “12” ilə əvəzləyib yeni dəyişənə
# yazın. Yeni dəyişənin başlanğıcdan 5-ci elementə kimi olan hissəsini çapa verin.


vip = "Bineqedi"

pk = vip.replace("di", "12")

print(pk)

print(pk[0:5])





# 6. “Men proqramlasdirma oyrenirem.” cümləsini bir dəyişənə yazın və bu dəyişəni “ “
# (boşluq) simvoluna görə parçalayın.

uu = "Men proqramlasdirma oyrenirem."

print(uu.split())

print(uu.split("p"))   # yoxladim gorum ne bas verir?



# 7. Bütün simvolları kiçik hərflə olan str tipli bir dəyişən götürün və bu dəyişənin
# başlanğıcdan sona kimi elementlərini 1 simvol ötürərək böyük hərflərlə çapa verin.
# (məs: “salam” – “SLM”)


ff = "kondisioner"

print(ff[0::2].swapcase())        # reqemleri nece deyisdirir?

print(ff[0::2].upper())





# 8. Str tipli iki dəyişən götürün. 1-ci dəyişənin ilk 2 simvolu ilə 2-ci dəyişən son 2
# simvolunu birləşdirib yeni bir dəyişənə yazın. Yeni dəyişənin bütün simvollarını kiçik
# hərflə çapa verin.


ty = "ALQORITM"

gg = "GIMNASTIKA"

hh = ty[0:2] + gg[8:]


print(hh.casefold())
 

print((ty[0:2] + gg[8:]).swapcase())    




# 9. Str tipli bir dəyişən götürün və onun 3-cü elementindən 15-ci elementinə kimi olan
# hissəsini 2 simvol ötürərək yeni bir dəyişənə yazın. Yeni dəyişənin “a” simvolu ilə
# başlayıb-başlamamasını və “z” simvolu ilə bitib-bitməməsini yoxlayın.


td = "Qafqaz Universiteti"

ju = td[3:15:3]


print(ju.startswith("a"))



print(ju.endswith("z"))




# 00 elave test

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)       #bu ne demekdir? 5-dən 11-ə qədər mövqenin "mənim dünyam" ifadəsi ilə bitdiyini yoxlayın.

print(x)




# 10. İki int tipli dəyişən götürün və onların bütün müqayisələrini (kiçikdir, böyükdür,
# bərabərdir, bərabər deyildir) yeni bir dəyişənə yazıb,` bu dəyişənləri çapa verin.


df = 78

qe = 78.001

jjj = df < qe

print(jjj)


ttt = df > qe

print(ttt)


yyy = df == qe // 1  #  tam hissesini goturur


print(yyy)



rrr = df != qe

print(rrr)


aaa = df <= qe

print(aaa)



lll = df >= qe

print(lll)






j = "Nerimanov"

yyyy = j[-2:2:-1]          #  onami cixmasi ucun nece etmeliyem?

print(yyyy)



rtrt = "youtbe"

nnnnn = rtrt[-5:-1:-1]

print(nnnnn)



