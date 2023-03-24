# # a = 5
# # print(a)

# # a="salam"
# # b="dunya"
# # c= a + "  " + b*3

# # print(a + "  " + b*3) 

# # a = 5

# # c = float(a)

# # print(type(c))

# # print(c)


# # tet = "534"

# # print(int(tet))
# # a = "223"
# # b="448"

# # c = int(float(a) + int(b))

# # print(c)

# # a = 34,5
# # b = 


# k = "15"

# b = 20.4


# print(type(k))


# c = int(k) +b
# c = float(k) + b

# a = 5.1

# b = 10

# a = a + b

# a += b

# print(a)

# a = a*b



# a *= b



# a /= b


# print(a)



# m = 253

# l = 15

# v = m %l

# print(v)

# m %= l
# print(m)



# a, b , c  = 18, 25, "24"

#print(a + b, c)




#### Operatorlar ####

# 1. Menimsetme (Assignment) operatoru
# =

# 2. Arifmetik operatorlar
# +, -, *, /, //, %, **

# 3. Artirma, Azaltma (Increment, Decrement) operatorlari
# +=, -=, *=, /=, //=, %=, **=

# 4. Muqayise (Comparison) operatorlari
# <, >, <=, >=, ==, !=

#### Variable Convertion ###

# 1. to int ==> int()
# 2. to float ==> float()
# 3. to str ==> str()
# 4. Deyisenin tipini qaytarir ==> type()

# a3 = 5

# print(a3)

# ay = 5; bp = 8

# c = ay + bp

# print(c)

# print(type(c))

# k = "Cemil"

# o = "Ehmedov"

# h = k + " " + o 

# print(h)


# print(type(h))



# l = 45

# kim = 34.0

# c = l - kim

# print(c)

# print(l - kim)


# print(type(l - kim))


# print(type(c))



# j = 12

# v = 10

# l = 14 + j*v


# vb = "Ahmed"

# # vb = vb + " " + "5"  +","

# vb += " " + "5" + ","

# vb = (vb + " ")*10



# print(vb)


# print(l)

# yt = 64

# rt = 5

# oi = yt / rt

# print(oi)

# print(type(oi))



# ol = 72

# lo = 5

# oll = ol // lo

# print(oll)





# hyu = 7

# lki = 4

# uuu = hyu % lki

# print(uuu)

# yt = 2

# hj = 6

# kk = yt ** hj

# print(kk)


# rr = 8

# rr += 10

# print(rr)



# tt = 12

# tt -= 80

# print(tt)



# ii = 10

# ii *= 1273

# print(ii)



# ui = 67

# ui **= 4

# ui += 3


# print(ui)


# ty = 45    muzakire olunmali

# kl = 15

# ll = ty + kl

# ty = str(ty)

# print(ll)



# ty = 45   

# kl = "15"

# ty = str(ty)

# ll = ty + kl

# print(ll)

# ll = int(ty) + int(kl)

# print(ll)




# Tapsiriqlar

# 1. İki int tipli a və b dəyişənlərinin cəminin fərqinə bölünməsindən alınan qalığı
# hesablayan proqram tərtib edin.

# a = 19

# b = 4

# c = (a + b) % (a - b)

# print(c)



# 2. İki str tipli ad və soyadı və bir int tipli yaşı özündə saxlayan dəyişən götürün və bu
# dəyişənlərdən istifadə edərək tam adı və yaşı çapa verin. Məs: “İbrahimli Valeh 23
# yaş”

# k = "Seyfullayev"

# l = 'Idrak'

# y = 35

# u = "yas"

# print(k + " " + l + " "+ str(y) + " " + u)


# 3. İki int tipli a və b dəyişəni götürün və a dəyişənini əvvəlcə b qədər, daha sonra b dəfə
# artırın. Nəticəni çapa verin.



# a = True

# b = 35

# c = "Salam"

# d = a + bool(b) + bool(c)

# print((d))




# d = str(a + bool(b) + bool(c))


# print(d)



# j = "Nerimanov"

# print(j[-2:-8:-1])




# pl = "karvansaray"

# ok = pl[::-1].capitalize()  

# print(ok)


# pl = "karvansaray"

# ok = pl[-1:-12:-1].capitalize()  

# print(ok)



# er = "MasalliM"

# print(er.count("M"))

# print(er.count(er[0]))


# vip = "Bineqedi"

# pk = vip.replace("di", "12")

# print(pk)

# print(pk[0:5])





# j = "Nerimanov"

# yyyy = j[-2:2:-1]          #  onami cixmasi ucun nece etmeliyem?

# print(yyyy)



# rtrt = "youtube"

# nnnnn = rtrt[-1:0:-1]   #oxunus duzduse oxuyacaq????

# print(nnnnn)




# df = 78

# qe = 78.001




# yyy = df == qe // 1  #  tam hissesini goturur




# print(yyy)






# a1 = input()

# print(a1)


# ad = input()

# soyad = input()


# print("{} {}".format(ad, soayd))

# print('{}{}'.format(ad, soyad))

# print("{}")



# k, l = input().split()

# k, l = int(k), int(l)

# print("%d %d" % (k, l))






# list1 = list("sa")

# print(list1)




# binom = [[1], [1,1] ]

# n = int(input())

# for i in range(2, n+1):
#     binom.append([])
#     binom[i].append(1)
#     for j in range(1,i):
#         binom[i].append(binom[i-1][j-1] + binom[i-1][j])
#     binom[i].append(1)
      

# for i in binom:
#     if len(i) <=len(binom)-1:
#         print(" ",end="")
#     for k in range(len(binom)-len(i)):
#         print(" ", end=" ")
#     for j in i:
#         print(j , end="   ")
#     print()    











# a = 123456

# print(str(a)[::-1])


# b = [1, 2, 3]

# x = reversed(b)

# for i in x:
#     print(i)


# print(sum([7, 8]))








# def check_number_given_range(n, x, y):
#     for i in range(x, y+1):
#         if n == i:
#             return f"{n} is in range{x,y}"  
#     else:
#         return f"{n} isnt in range({x}, {y})"

# num = int(input())
# beginning_interval = int(input())
# end_of_interval = int(input())
# print(check_number_given_range(num, beginning_interval, end_of_interval))





# def count_upper_lower_letter(text):
#     uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lowers = "abcdefghijklmnopqrstuvwxyz"
#     c = 0
#     t = 0
#     for i in text:
#         if i in uppers:
#             c += 1
#         elif i in lowers:
#             t += 1    
#     return (f"In '{text}' text have {c} upper letter and {t} lower letter")
#     # print(f" No. of Upper case characters : {c}")
#     # print(f" No. of lower case characters : {t}")

# string1 = 'The quick Brown Fox'
# print(count_upper_lower_letter(string1))




# a = "ket ulutek"
# b = a.split(" ")
# c = "".join(b)
# print(c)



# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXVZ"
# string = "The quick brown fox jumps over the lazy dog"
# string1 = string.upper()
# string2 = string1.split()
# string3 = "".join(string2)
# string4 = set(string3)
# string5 = list(string4)
# string5.sort()
# string6 = "".join(string5)
# print(type(string6))
# print(type(alphabet))

# if string6 == alphabet:
#     print("salam")
    


# a = "salam"


# def yoxla(x):
#     a = "salam"
#     if x == a:
#         return 5

# k = "salam"
# print(yoxla(k))









# class Woker:
#     cambinzon_in_year = 2
#     helmet_in_year = 1
#     helmet_color = "blue"
#     safety_glass_in_year = 1
#     boot_in_year = 2
#     jacet_in_year = 1
#     canteen_entrance = "junior"
#     vacation = "own expence"

#     def __init__(self, name, surname, position, salary):
#         self.name = name
#         self.surname = surname 
#         self.position = position
#         self.salary = salary

#     def get_full_name(self):
#         return f"{self.name.capitalize()} {self.surname.capitalize()}"

#     def get_vacation_days(self):
#         for i in range(1,11):
#             if i == self.period_work:   # bu funksiyanin deyiseni child class-da olsada isleyir niye???????? 
#                 return 22 + i*2

# class ITW(Woker):
#     vacation = "Company's expense"
#     canteen_entrance = "Senior"
#     helmet_color =  "White"

#     def __init__(self, name, surname, position, salary, period_work):
#         super().__init__(name, surname, position, salary)
#         self.period_work = period_work

#     def get_general_info_salary(self):
#         return f"{self.name} {self.surname} : {self.position}, {self.salary}"


# class Bonus_salary(ITW):
    
#     # def __init__(self, name, surname, position, salary, vacation_days):
#     #     super().__init__(name, surname, position, salary, vacation_days)

#     # days = int(input())   Men burda niye input vere bilmirem????????????????
#     def salary_with_bonus(self, days):
#         bonus = days*30
#         return f"{self.get_full_name()}: Salary with bonus:{self.salary + bonus}"   

#     # Men asagida printde ancaq idrak.salary_with_bonus funksyasini cagiranda mentiqi olaraq anladim ki
#     # salary_with_bonus funksiyasinin return-nine get_full_name() funksiyasini yazsam Idrak seyfullayev:
#     # salary with bonus: mebleg cap oluncaq.amma proqram bunu hansi aloritme esasen edir bax bunu anlamadim.??????    

#     # salary_bonus(days)  Burda niye funksiya cagira bilmirem????????/                      



# alik = Woker("Alik", "Yolcuyev", "Usta", 500)
# zulfuqar = Woker("Zulfuqar", "Aliyev", "Fehle", 450)
# nurlan = Woker("Nurlan", "Kazimov", "Bagban", 600)
# idrak = Bonus_salary("Idrak", "Seyfullayev", "Foreman", 800, 5) # burda int(input) vere bilmedim?????????
# sahbaz = Bonus_salary("Sahbaz", "Xelilov", "Engineer", 1200, 8)
# nebi = Bonus_salary("Nebi", "Seyfullayev","Junior Engineer", 700, 4)


# print(f"{alik.get_full_name()} - Helmet color:{alik.helmet_color} - Boot in year:{alik.boot_in_year} - Canteen_entrance:{alik.canteen_entrance} - Vacation:{alik.vacation}")
# print(f"{nebi.get_full_name()} - Cambinzon_in_year:{nebi.cambinzon_in_year} - Jacet_in_year:{nebi.jacet_in_year} - Helmet_color:{nebi.helmet_color} - Canteen_entrance:{nebi.canteen_entrance} - Vacation:{nebi.vacation}")

# print(nebi.get_general_info_salary())
# print(f"{nebi.get_full_name()} - Vacation_days:{nebi.get_vacation_days()}")


# # print(f"{idrak.get_full_name()} - Vacation_days:{idrak.vacation_days}")

# print(f"{idrak.get_full_name()} - Vacation_days:{idrak.get_vacation_days()}")

# print(idrak.salary_with_bonus(int(input())))



# def cap(a,b,c):
#     return f"{a}, {c}, {b}"
# a ="salam"
# b = "axiret"

# print(cap(a,b,"\n"))



# print(list(enumerate([5, 9, 3, 7, 2])))








# class Math:
#     pi = 3.14
#     e = 2.71

#     def __init__(self, name, n):
#         self.name = name
#         self.n = n

#     def topla(self, m):
#         return self.n + m

#     def bolenlerin_sayi(self):
#         count = 0
#         for i in range(1, self.n +1):
#             if not self.n % i:
#                 count += 1
#         return count

#     def ebob(self):
#         return None

#     def __str__(self):
#         return self.name


# y = Math("y", 10)

# a = y.topla(15)  # 25
# b = y.bolenlerin_sayi()
# print(a)
# print(b)
# print(y)
# print(y.n)









# def pyramid(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end=" ")
#         print("\r")        

# n = 10
# pyramid(n)





# def check_perfect_number(n):
#     sum_divisor = 0
#     for i in range(1, n):
#         if not n % i:
#             sum_divisor+=i           
#     if sum_divisor == n:
#         return "a perfect number"
#     else:
#         return "isn't a perfect number"


# num = 495
# print(check_perfect_number(num))           





# def check_square_number(n):
#     if n**0.5 == int(n**0.5):
#         return "a square number"
#     else:
#         return "isnt' a square number"



# num = 4
# print(check_square_number(num))        



# print("""{}
# {}{}""".format(1,(" ")*5,2))


# n = 5
# for i in range(1,n+1):
#     print("{}{}{}".format((" ")*(n-i),"*"*i,("*")*(i-1)))

# n = 5    
# for i in range(1,n+1):
#     print(f"{(' ')*(n-i)}{'*'*i}{'*'*(i-1)}")





# class Math:
#     pi = 3.14
#     e = 2.71

#     def __init__(self, name, n):
#         self.name = name
#         self.n = n

#     def __str__(self):
#         return self.name
    
#     def topla(self, m):
#         return self.n + m

#     def bolenlerin_sayi(self):
#         count = 0
#         for i in range(1, self.n +1):
#             if not self.n % i:
#                 count += 1
#         return count

#     def bolenleri_(self):
#         str1 = ""
#         for i in range(1, self.n+1):
#             if not self.n % i:
#                 str1 += str(i) + ", "
#         return (str1)       # burda print(i,end= " ")  verende qarisdi printe verdiyim netice
                
        
#     # def ebob(self, m):
#     #     while self.n != m:
#     #         if self.n > m:
#     #             self.n = self.n - m
#     #         else:
#     #             m = m - self.n
#     #     return self.n             #  return self.n verende  asagida print(eded_10.n) = 5 olur eslinde 10 olmalidi idi??? 


#     def ebob(self, m):
#         x = self.n  #   burda deyisene yazdim duzeldi
#         while x != m:
#             if x > m:
#                 x = x - m
#             else:
#                 m = m - x
#         return x

#     def ekob(self, t, ebob):
#         return (self.n * t) / ebob    # retunn-de nece ebob-u funksiya kimi yaza bilerem?
#         # return (self.n * t) / self.ebob(t) 2-ci forma 
        

#     def factorial(self):
#         fact = 1
#         for i in range(2, self.n+1):
#             fact *= i
#         return fact    

#     def check_prime_composite_number(self):
#         if self.n <= 0:
#             return "isn't natural number"
#         elif self.n ==1:
#             return "neither a prime nor a composite number"    
#         for i in range(2, self.n):
#             if not self.n % i:
#                 return "a composite number"
#         else:
#             return "a prime number"        


#     def check_perfect_number(self):
#         sum_divisor = 0
#         for i in range(1, self.n):
#             if not self.n % i:
#                 sum_divisor += i           
#         if sum_divisor == self.n:
#             return "a perfect number"
#         else:
#             return "isn't a perfect number"            


#     def check_square_number(self):
#         if self.n**0.5 == int(self.n**0.5):
#             return "a square number"
#         else:
#             return "isnt' a square number"  


#     def calculate_circle_area_by_radius(self):
#         return self.pi * self.n**2 
    
#     def calculate_radius_by_circle_area(self):
#         return (self.n / self.pi)**0.5   


#     def calculate_arranged(self, z):
#         arranged = 1
#         for i in range(self.n-z+1, self.n+1):
#             arranged *= i
#         return arranged    

# eded_10 = Math("10", 10)

# print(f"""Eded_{eded_10} - 
# Bolenlerin_sayi:{eded_10.bolenlerin_sayi()},
# Bolenleri:{eded_10.bolenleri_()}
# EBOB({eded_10.n},{35})={eded_10.ebob(35)}, 
# EKOB({eded_10.name},{45})={eded_10.ekob(45, eded_10.ebob(45))}, 
# Factorial_{eded_10}={eded_10.factorial()},
# Eded_{eded_10}:{eded_10.check_prime_composite_number()}, 
# Eded_{eded_10}:{eded_10.check_perfect_number()},
# Eded_{eded_10}:{eded_10.check_square_number()}, 
# Arranged({eded_10},{5})={eded_10.calculate_arranged(5)}""",)    




# class Math:
#     pi = 3.14
#     e = 2.71

#     def __init__(self, name, n):
#         self.name = name
#         self.n = n

#     def __str__(self):
#         return self.name
    

#     def ekob(self, t):
#         return (self.n * t) / Mathchild.ebob(eded_2, t) #  mentiqi basa dusdum amma yazilis sadece bir az qaranliq qaldi?
#         # return (self.n * t) / self.ebob(t) 2-ci forma

# class Mathchild(Math):

#     def __init__(self, ad, z):
#         self.name = ad
#         self.z = z

#     def ebob(self, m):
#         x = self.z 
#         while x != m:
#             if x > m:
#                 x = x - m
#             else:
#                 m = m - x
#         return x

# eded_10 = Math("10", 10)
# eded_1 = Mathchild("18", 5)
# eded_2 = Mathchild("9", 15)

# print(f"EKOB({eded_10.name},{45})={eded_10.ekob(45)}")





# print("%d %a" %(5, "b"))

# a = 5
# b = 2
# c = a + b
# print(c)

# Y = "salam"
# X = "dunya"
# t = Y + X
# print(t)



# print(list(filter(lambda n: n > 5, range(10))))

# n = int(input())
# print((lambda x:(not x % 2 and "cut eded" or "tek eded"))(n)))
# x = 5

# y = lambda x: not x % 2 and "cut eded" or "tek eded"
# x = int(input())
# print(y(x))


# y = lambda x: x*5
# x = int(input())
# print(y(x))




# list1 = [1, 2, 4 , 6]
# list2 = [2, 4, 5]
# x = int(input())
# list3 = [(lambda x: x)(range(x))]

# print(list3)


# import datetime
# cur_time = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
# print(cur_time)









# class Math:

#     def __init__(self, name, n):
#         self.name = name
#         self.n = n

#     def __str__(self):
#         return self.name

#     def bolenlerin_sayi(self):
#         count = 0
#         for i in range(1, self.n +1):
#             if not self.n % i:
#                 count += 1
#         return count
        

# # eded_10 = Math("eded_10", 10)
# # print(Math.bolenlerin_sayi(eded_10))
# print(Math("eded_100", 100).bolenlerin_sayi())



# class Math:

#     def __init__(self, name, n):
#         self.name = name
#         self.n = n

#     def __str__(self):
#         return self.name

#     def bolenleri(self):
#         sum = 0
#         for i in range(1, self.n):
#             if not self.n % i:
#                 sum += i
#                 print(i)
#         return sum

# class Math_1(Math):

#     def __init__(self, name, n):
#         super().__init__(name, n)

#     def perfect_num(self):
#         if self.n == super().bolenleri(): 
#             return "perfect number"
#         else:
#             return "is'nt perfect number"


# # eded_6 = Math_1("eded_6", 6)
# # print(eded_6.perfect_num())
# print(Math_1("eded_50", 50).perfect_num())
# # print(Math_1.perfect_num(eded_19)) #  bunu niye goturmur??



# print(datetime.date(1, 1, year=1))








# a,b,c = input().split()
# print(a)
# print(b)
# print(c)
# print(int(a)+int(b)+int(c))


# a = int(input())
# b = int(input())
# c = int(input())

# print(f'{a}, '
# f'{b}, '
# f'{c}')





# def fib(n):
#     n1 = 0
#     n2 = 1
#     for i in range(3,n+1):
#         n1, n2 = n2, n1 + n2
        
#         print(n2)

# fib(10)    




# list1 = list(map(lambda x: x,range(5) ))
# print(list1)



# from functools import reduce
 
# fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
#                                 range(n-2), [0, 1])
 
# print("Fibonacci series upto 2:")
# print(fib_series(2))
# print("\nFibonacci series upto 5:")
# print(fib_series(5))
# print("\nFibonacci series upto 6:")
# print(fib_series(6))
# print("\nFibonacci series upto 9:")
# print(fib_series(9))




# print(reduce(lambda x, y: x+y, [1, 6, 3, 4, 5]))

# ((((1+2)+3)+4)+5)


# org_list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# org_list_2 = [1, 2, 4, 8, 9]
# set_intersection = lambda x,y: set(x).intersection(set(y))
# list_intersection = list(set_intersection(org_list_1, org_list_2))
# list_intersection.sort()
# print(list_intersection)


# org_list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# org_list_2 = [1, 2, 4, 8, 9]

# list_intersection = list(filter(lambda x: x in org_list_1, org_list_2))    
# print(list_intersection)

# a = [1,2,3,4,5]
# y = lambda x: x if x in a else "yoxdur" 
# print(y(6))



# a = [1,2,3,4,5]
# b = [1,2]
# y = list(filter(lambda x: x in b, a)) 
# print(y)




# list1 = [-1, 2, -3, 5, 7, 8, 9, -10]

# list1.sort()
# print(list1)




# import datetime

# y = datetime.date.today()
# print(y)
# x = datetime.datetime(y.year, y.month, y.day, hour=15, minute=45) + datetime.timedelta(days = 1, hours=1) 
# print(x.strftime("%d-" "%m-" "%Y " "%H:" "%M"))




# Python program to shuffle a deck of card

# # importing modules
# import itertools, random

# # make a deck of cards
# deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# # shuffle the cards
# random.shuffle(deck)

# # draw five cards
# print("You got:")
# for i in range(5):
#    print(deck[i][0], "of", deck[i][1])




# import calendar

# print(calendar.month(2014, 11))


# # Program to display calendar of the given month and year

# # importing calendar module
# import calendar

# yy = 2014  # year
# mm = 11    # month

# # To take month and year input from the user
# # yy = int(input("Enter year: "))
# # mm = int(input("Enter month: "))

# # display the calendar
# print(calendar.month(yy, mm))



# my_list = [[1], [2, 3], [4, 5, 6, 7]]

# flat_list = [x for y in my_list for x in y]
# print(flat_list)



# list_1 = [int(input()) for x in range(int(input()))]
# print(list_1)

# list_1 = []
# x = int(input())
# for i in range(x):  
#     y = int(input())
#     list_1.append(y)

# print(list_1)    




# matrix = []

# for i in range(int(input())):
#     list_1 = [int(input()) for i in range(int(input()))]
#     matrix.append(list_1)

# print(matrix)    




# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# list1 = [i for j in my_list for i in j]
# print(list1)

# list2 = []
# for i in my_list:
#     for j in i:
#         list2.append(j)

# print(list2)


def a(x):
    try:
        return x[1]
    except TypeError:
        return x
        

   


tuple1 = [["b",12],["a",1],2,1]

tuple2 = sorted(tuple1, key=a)
print(tuple2)
# list4 =[(1,2,3,4,5),(12,3)]
# list4.sort(key=a)
# print(list4)





# result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)