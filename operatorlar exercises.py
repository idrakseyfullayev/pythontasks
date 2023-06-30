# a = 5
# print(a)

# a="salam"
# b="dunya"
# c= a + "  " + b*3

# print(a + "  " + b*3) 

# a = 5

# c = float(a)

# print(type(c))

# print(c)


# tet = "534"

# print(int(tet))
# a = "223"
# b="448"

# c = int(float(a) + int(b))

# print(c)

# a = 34,5
# b = 


k = "15"

b = 20.4


print(type(k))


c = int(k) +b
c = float(k) + b

a = 5.1

b = 10

a = a + b

a += b

print(a)

a = a*b



a *= b



a /= b


print(a)



m = 253

l = 15

v = m %l

print(v)

m %= l
print(m)



a, b , c  = 18, 25, "24"

print(a + b, c)




### Operatorlar ####

# 1. Menimsetme (Assignment) operatoru
# =

# 2. Arifmetik operatorlar
# +, -, *, /, //, %, **

# 3. Artirma, Azaltma (Increment, Decrement) operatorlari
# +=, -=, *=, /=, //=, %=, **=

# 4. Muqayise (Comparison) operatorlari
# <, >, <=, >=, ==, !=

# ### Variable Convertion ###

# 1. to int ==> int()
# 2. to float ==> float()
# 3. to str ==> str()
# 4. Deyisenin tipini qaytarir ==> type()

a3 = 5

print(a3)

ay = 5; bp = 8

c = ay + bp

print(c)

print(type(c))

k = "Cemil"

o = "Ehmedov"

h = k + " " + o 

print(h)


print(type(h))



l = 45

kim = 34.0

c = l - kim

print(c)

print(l - kim)


print(type(l - kim))


print(type(c))



j = 12

v = 10

l = 14 + j*v


vb = "Ahmed"

# vb = vb + " " + "5"  +","

vb += " " + "5" + ","

vb = (vb + " ")*10



print(vb)


print(l)

yt = 64

rt = 5

oi = yt / rt

print(oi)

print(type(oi))



ol = 72

lo = 5

oll = ol // lo

print(oll)





hyu = 7

lki = 4

uuu = hyu % lki

print(uuu)

yt = 2

hj = 6

kk = yt ** hj

print(kk)


rr = 8

rr += 10

print(rr)



tt = 12

tt -= 80

print(tt)



ii = 10

ii *= 1273

print(ii)



ui = 67

ui **= 4

ui += 3


print(ui)


ty = 45   # muzakire olunmali

kl = 15

ll = ty + kl

ty = str(ty)

print(ll)



# ty = 45   

# kl = "15"

# ty = str(ty)

# ll = ty + kl

# print(ll)

# ll = int(ty) + int(kl)

# print(ll)




                             # Ev tapşırıqları Dərs 1. Dəyişənlər, Operatorlar. 

# 1. İki int tipli a və b dəyişənlərinin cəminin fərqinə bölünməsindən alınan qalığı
# hesablayan proqram tərtib edin.

a = 19

b = 4

c = (a + b) % (a - b)

print(c)



# 2. İki str tipli ad və soyadı və bir int tipli yaşı özündə saxlayan dəyişən götürün və bu
# dəyişənlərdən istifadə edərək tam adı və yaşı çapa verin. Məs: “İbrahimli Valeh 23
# yaş”

k = "Seyfullayev"

l = 'Idrak'

y = 35

print(k + " " + l + " "+ str(y) + " " + "yas")


# 3. İki int tipli a və b dəyişəni götürün və a dəyişənini əvvəlcə b qədər, daha sonra b dəfə
# artırın. Nəticəni çapa verin.


a = 70

b = 23

a += b

a *= b

print(a)

# ve ya

# a = a + b

# a = a*b

# print(a)

# ve ya

# a = 70

# b = 23

# a = (a + b) * b

# print(a)


# 4. Üç müxtəlif tipli dəyişən götürün (int, float, str) və onların tipini alt-alta çapa verin.

kitablarin_sayi = 99      # kitablarin sayi niye yazmaq olmur

print(type(kitablarin_sayi))

derman_qr = 3.2           #derman(qr) niye yazmaq olmur

print(type(derman_qr))

ad_soyad = 'Idrak Seyfullayev'

print(type(ad_soyad))


# 5. a = “Ders” və b = 1; “Ders1Ders1Ders1” çapa verin.

a = "Ders"

b = 1

c = (a + str(b))*3

print(c)



# 6. İnt tipli a və b dəyişənlərinin nisbəti (/) ilə tam nisbətinin (//) hasilini çapa verin.

a = 48

b = 44

c = (a / b) * (a // b)

print(c)



# 7. Str tipli a və b dəyişənlərini int tipinə çevirərək cəmini, fərqini, hasilini, nisbətini, tam
# nisbətini, qalığını (a%b) və qüvvətini (a^b) çapa verin: a = “48”, b = “3”.


a = "48"

b = "3"

# c = int(a)  bilmirem hansi sekilde daha duzgun hesab olunur bu yoxsa davam etdiyim qayda

# d = int(b)

# print(c + d)

print(int(a) + int(b))

print(int(a) - int(b))

print(int(a) * int(b))

print(int(a) / int(b))

print(int(a) // int(b))

print(int(a) % int(b))

print(int(a) ** int(b))


# 8. İki int tipli a və b dəyişəni götürün və onların cəmi ilə fərqinin 2-ci dərəcədən
# qüvvətlərini toplayıb çapa verin.

a = 7

b = 8

c = (a + b)**2 + (a - b)**2

print(c)



# 9. Float tipli iki dəyişənin tam hissələrinin cəmini çapa verin.

w = 47.8

r = 12.5

print(int(w) + int(r))




# 10. “Men”, “proqramlasdirma”, “oyrenirem” sözlərinin hərəsini bir dəyişənə yazın və bu
# dəyişənlərdən istifadə edərək “Men proqramlasdirma oyrenirem.” cümləsini çapa
# verin.

g = "Men"

x = "proqramlasdirma"

z = "oyrenirem"

print(g + " " + x + " " + z + ".")

print('"' + g + " " + x + " " + z + "." + '"')



# # python testleri


# a = 7; b =4   #izaha ehtiyac var

# a, b = b, a

# print(a - b)    



# ty = 45    

# kl = 15

# ll = ty + kl

# ty = str(ty)

# print(ll)

# print(ty + kl)















