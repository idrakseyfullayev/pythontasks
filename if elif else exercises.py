# a = 10
# b = 8
# c = 7

# if a == 10:
#     x = a + b
#     print(x)
#     if b == 9:
#         print(9)
#     else:
#         print(8)



# 01. string daxil olunsun ,  stringin ilk simvolu a -dirsa a silinsin   esk halda ilk simvol stringin sonuna elave olunsun

a1= input() 

if a1[0] == "a":
    a1 = a1[1:]
else:
    a1 = a1 + a1[0]

print(a1)





# 02. iki str daxil olunsun    yoxlayiram ki ikinci str birinci str-in ilk sozudrse, onda birinci str-den ikinci 

# str-i sil, eks halda str ozu cap olunsun birinci str yani

a = input()
b = input()

if a[:len(b)] == b:
    a = a[len(b):]

print(a)




# 03. list olsun    lsitin elementlerinin sayi   listin birinci elementine bereberdirse onda listin elentlerimin

 #sayi ile onun birinci elementinin cemi cap olunsn   eks halda onlarin ferqini cap etsin

list1 = [2, 1, 0,]

if list1[0] == len(list1):
    print(len(list1) + list1[0])
else:
    print(len(list1) - list1[0])    





# 04. bir eded str daxil olunsun    eger str de bosluq simvolu varsa bu bosluqa gore parcalansin eks halda,
# bu str tersine capa versin

a = input()

if ' ' in a:
    b = a.split()
else:
    b = a[::-1]    

print(b)


#                       # Dərs 7. Şərt operatorları(if/elif/else). Ev tapşırıqları #

# 1. İki str tipli dəyişən götürün. Əgər birinci dəyişənin ilk elementi ikinci dəyişənin ilk
# elementinə bərabərdirsə, onları “*” simvolu ilə əvəzləyin, əks halda birinci dəyişənin
# ilk elementini ikinci dəyişənin ilk elementi ilə əvəzləyin.

a1 = input()
b1 = input()

if a1[0] == b1[0]:
    a1 = "*"
    b1 = "*"
    print(a1)
    print(b1)
else:
    a1 = b1[0] + a1[1:]
    print(a1)
    a1 = a1.replace(a1[0], b1[0] )   # alma yazanda her iki a herfi b1[0] ile evez olundu??????
    print(a1)


# 2. Bir str tipli dəyişən götürün. Əgər bu dəyişəndə boşluqlar varsa, onu başlıq(title)
# formasında çap edin, əks halda onun uzunluğunu çap edin.

a21 = input()

if " " in a21:
    print(a21.title())
else:
    print(len(a21))    


# 3. Bir str tipli dəyişən götürün. Əgər bu dəyişən böyük hərflə başlayıb, böyük hərflə
# bitirsə, onun bütün simvollarını böyük hərflə çap edin, əgər böyük hərflə başlayıb
# kiçik hərflə bitirsə, bütün simvolları swapcase formada çap edin, əgər kiçik hərflə
# başlayıb böyük hərflə bitirsə, olduğu kimi çap edin, əks halda bütün simvolları kiçik
# hərflə çap edin.

a31 = input()

if a31.startswith(a31[0].capitalize()) and a31.endswith(a31[-1].capitalize()):
    print(a31.upper()) 
elif a31.startswith(a31[0].capitalize()) and a31.endswith(a31[-1].casefold()):
    print(a31.swapcase())
elif a31.startswith(a31[0].casefold()) and a31.endswith(a31[-1].capitalize()):
    print(a31)
else:
    print(a31.casefold())    


# Basqa metodla hell #

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"

if a31[0] in uppers and a31[-1] in uppers:
    print(a31.upper()) 
elif a31[0] in uppers and a31[-1] in lowers:
    print(a31.swapcase())
elif a31[0] in lowers and a31[-1] in uppers:
    print(a31)
else:
    print(a31.casefold())        


# 4. Bir list dəyişəni götürün. Əgər bu listdə 5 element varsa, listə yeni 3 element, 6
# element varsa 2 element, 7 element varsa 1 element əlavə edin. Elementlərin sayı 8-
# dən çoxdursa, 1 element silin.

list41 = [1000, 6, 56, 78, 1089, 90, "ups", 12, 90]

if len(list41) == 5:
    list41.extend("543")
    print(list41)
elif len(list41) == 6:
    list41.append(78)
    list41.append(101)
    print(list41)
elif len(list41) == 7:
    list41.insert(2, 0)   
    print(list41)
elif len(list41) > 8:
    list41.pop(2)
    print(list41)    


# 5. İki list dəyişəni götürün. Birinci listin ilk elementi, ikinci listin son elementinə
# bərabərdirsə, bu listləri tərs sıra ilə, böyükdürsə, birinci listi tərs, ikinci listi düz sıra ilə,
# əks halda, hər iki listi bu listləri düz sıra ilə nizamlayıb çap edin.

list51 = int(input())
list52 = int(input())

list51 = [9, 4, 6, 7]
list52 = [0, 3, 5, 8]

if list51[0] == list52[-1]:
    list51.sort(reverse=True)
    list52.sort(reverse=True)
    print(list51)
    print(list52)
elif list51[0] > list52[-1]:
    list51.sort(reverse=True)
    list52.sort()
    print(list51)
    print(list52)
else:
    list51.sort()
    list52.sort()
    print(list51)
    print(list52)    


# 6. İki set dəyişəni götürün. Birinci setin elementlərinin sayı ikinci listin elementlərinin
# sayına bərabərdirsə, onların birləşməsini, böyükdürsə, kəsişməsini, əks halda fərqini
# çap edin.

set61 = {3, 45, 89, 9, "salam"}
set62 = {'Kim Cen In', 23, 56, 78}

if len(set61) == len(set62):
    print(set61.union(set62))
elif len(set61) > len(set62):
    print(set61.intersection(set62))
else:
    print(set61.difference(set62))


# 7. a, b, c, d int tipli dəyişənləri götürün. Əgər a b-yə və c d-yə tam bölünürsə, a+b+c+d
# cəmini çap edin, a b-yə tam bölünür, c d-yə tam bölünmürsə, a+b+c-d çap edin, a b-
# yə tam bölünmür, c d-yə tam bölünürsə, a-b+c+d çap edin, əks halda, bu dəyişənləri
# çap edin.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % b == 0 and c % d == 0:
    print(a + b + c + d)
elif a % b == 0 and c % d != 0:
    print(a + b + c - d)
elif a % b != 0 and c % d == 0:
    print(a - b + c + d)
else:
    print(a)
    print(b)
    print(c)
    print(d)        


# a = 10     
# b = 5

# if not a:
#     print(a)
# if a % b:
#     print(a+b)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not a % b and not c % d:
    print(a + b + c + d)
elif not a % b and c % d:
    print(a + b + c - d) 
elif a % b and not c % d:
    print( a - b + c + d)
else:
    print(a , b, c, d)



# 8. İki str tipli dəyişən götürün. Əgər ikinci dəyişənin bütün simvolları birinci dəyişəndə
# varsa, bu dəyişənlərin birləşməsini, əks halda hər iki dəyişəni tərsinə birləşdirib çap
# edin.

a81 = input()
b82 = input()

if b82 in a81:
    print(a81 + b82)
else:
    print(a81[::-1] + b82[::-1])
      

# 9. a, b, c int tipli dəyişənlərin ən böyüyünü çap edin.

a = int(input())
b = int(input())
c = int(input())


if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)


# 10. a, b, c parametrləri verilmiş kvadrat tənliyin ən böyük kökünü çap edin.
 
a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b*22 + D**0.5) / (2*a)
    x2 = (-b*2 - D**0.5) / (2*a)
    if x1 > x2:
        print(x1)
    else:
        print(x2)
elif D == 0:
    x = -b/(2*a)
    print(x)
else:
    print("tenliyin heqiqi koku yoxdur")                




 