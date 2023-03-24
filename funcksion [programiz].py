# a = 5
# b = 10

# def topla(a, b):
#     c = a + b
#     return c

# x = topla(a, b)
# print(x)



# a = 5
# b = 10

# def topla(a, b):
#     c = a - b
#     return c

# x = topla(b, a)
# print(x)



# a = 5
# b = 10

# def topla(a, b):
#     c = a - b
#     return c

# x = topla(a, b)
# print(x)



# a = 5
# b = 10

# def topla(a,b):
#     a += 1
#     c = a + b
#     print(c)

# x = topla(a, b)    
# print(x)



# a = 5
# b = 10

# def topla(a,b):
#     a += 1
#     c = a + b
#     return a, b, c

# x = topla(a, b)
# print(x)



# a = int(input())
# b = int(input())
# c = int(input())

# def kvadrat_tenlik(a, b, c):
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"

# print(kvadrat_tenlik(a, b, c))






# def kvadrat_tenlik(a=1, b=1, c=1):
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"

# print(kvadrat_tenlik())




# c =5

# def kvadrat_tenlik(c, a=1, b=1):
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"

# print(kvadrat_tenlik(c))






# a = int(input())
# b = int(input())
# c = int(input())

# def kvadrat_tenlik(a=1, c, b=1,):
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"

# print(kvadrat_tenlik(a, c, b))








# def kvadrat_tenlik(c, a=1, b=1):
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"


# print(kvadrat_tenlik(3,5))




# c = float(input())

# def kvadrat_tenlik(c, a=1, b=1,):
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"

# print(kvadrat_tenlik(c))



# def topla(*args):
#     a = 0
#     for i in args:
#         a += i
#     return(a)  
       
# print(topla(3, 5, 8, 9))


# def topla(*args):
#     a = 0
#     for i in args:
#         a += i
#         return(a)  # burda niye 3 cap olundu
       
# print(topla(3, 5, 8, 9))


# def topla(*args):
#     a = 0
#     for i in args:
#         a += i
#         print(a)
       
# print(topla(3, 5, 8, 9))


# def topla(*args):
#     a = 0
#     for i in args:
#         a += i
#     print(a)
       
# print(topla(3, 5, 8, 9))



# def topla(**kwargs):
#     a = 0
#     for i in kwargs:
#         a += kwargs[i] 
#     return a    

# print(topla(a=3, b=5, c=8,))


# def topla(**kwargs):
#     a = 0
#     for i in kwargs:
#         a += kwargs[i] 
#         return a    

# print(topla(a=3, b=5, c=8,))


# def topla(**kwargs):
#     a = 0
#     for i in kwargs:
#         a += kwargs[i] 
#         print(a)   

# print(topla(a=3, b=5, c=8,))


# def topla(**kwargs):
#     a = 0
#     for i in kwargs:
#         a += kwargs[i] 
#     print(a)   

# print(topla(a=3, b=5, c=8,))




# def topla():
# positional:
#      required
#      optional
# none-positional
#      *args
#      **kwargs         



# matrix= []
# n = int(input())

# for i in range(n):
#     m = int(input())
#     List1 = []
#     for j in range(m):
#         c = int(input())
#         List1.append(c)
#     matrix.append(List1)

# print(matrix)



# matrix= []
# n = int(input())

# for i in range(n):
#     m = int(input())
#     List1 = []
#     for j in range(m):
#         List1.append(int(input()))
#     matrix.append(List1)

# print(matrix)





#                               # Ders.Proqramiz Function-15 Ev tapsiriqlari #

# 1.Python Program to Display Powers of 2 Using Anonymous Function

# Bu proqramda siz Python anonim funksiyasından istifadə edərək tam 2-nin səlahiyyətlərini göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Döngü üçün Python
# Python Lambda/Anonim Funksiya
# Aşağıdakı proqramda 2-nin səlahiyyətlərini tapmaq üçün map() daxili funksiyası daxilində anonim (lambda) 
# funksiyasından istifadə etdik.

# Mənbə kodu
# Anonim funksiyadan istifadə edərək 2-nin səlahiyyətlərini göstərin

# şərtlər = 10

# İstifadəçidən daxil olmaq üçün aşağıdakı kodu şərhdən çıxarın
# şərtlər = int(input("Neçə termin? "))

# anonim funksiyadan istifadə edin

n = int(input())
list1 = list(map(lambda n: 2**n, range(n)))

for i in list1:
    print(f"{2} ^ {n} = {i}")
    


# ########################################
def pow_2(n):
    for i in range(n):
        print(f"{2}^{n} = {2** i}")

n = int(input())
pow_2(n)
# ########################################



# # Display the powers of 2 using anonymous function
terms = 10

# Uncomment code below to take input from the user
terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])   



# 2. Python Program to Find Numbers Divisible by Another Number

# Bu proqramda siz başqa ədədə bölünən ədədləri tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Lambda/Anonim Funksiya
# Python siyahısı
# Aşağıdakı proqramda biz siyahıda 13-ə bölünən bütün ədədləri tapmaq üçün filter() daxili funksiyası daxilində anonim 
# (lambda) funksiyasından istifadə etdik.

# Mənbə kodu
# # Nömrələrin siyahısını götürün

my_list = [12, 65, 54, 39, 102, 339, 221,]
List1 = []

for i in my_list:
    if not i % 13:
        List1.append(i)

for i in range(len(List1)-1):
    print(List1[i], end=", ")

print(f"{List1[-1]} ededleri 13-e bolunur")
print("Idrak", end=". ")
print("Seyfullayev")



my_list = [12, 65, 54, 39, 102, 339, 221,]

def my_function(my_list, n2):
    for i in my_list:
        if not i % n2:
            print(i, end=", ")
           
n2 = int(input())
my_function(my_list,n2)



my_list = [12, 65, 54, 39, 102, 339, 221,]

print(f"{list(filter(lambda n: not n % 13, my_list))} ededleri 13-e bolunur")



# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)



# 3. Python Program to Convert Decimal to Binary, Octal and Hexadecimal

# Ondalığı Binary, Octal və Hexadecima çevirmək üçün Python proqramı
# Bu proqramda siz ondalığı ikilik, səkkizlik və onaltılığa çevirməyi və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Proqramlaşdırma Quraşdırılmış Funksiyaları
# Onluq sistem ən çox istifadə olunan say sistemidir. Bununla belə, kompüterlər yalnız ikili sistemi başa düşürlər.
# İkilik, səkkizlik və onaltılıq say sistemləri bir-biri ilə sıx bağlıdır və biz ondalığı bu sistemlərə çevirməyi tələb
# edə bilərik. Onluq sistem 10 əsasdır (ədədi təmsil etmək üçün on simvol, 0-9 istifadə olunur) və buna bənzər şəkildə,
# ikilik baza 2, səkkizlik baza 8 və onaltılıq sistem 16 əsasdır.

# 0b prefiksi olan ədəd ikilik, 0o səkkizlik, 0x isə onaltılıq sayılır. Misal üçün:

# 60 = 0b11100 = 0o74 = 0x3c
# Mənbə kodu
# Onluğu digər say sistemlərinə çevirmək üçün Python proqramı
# dec = 344


x = int(input())
print("{0:b}".format(x))


# binary-      0:b  -  ikilik
# decimal-     0:d  -  onluq
# octal-       0:o  -  sekkizlik
# hexadecimal- 0:x  -  on altiliq
# integer -    0:i  -  tam eded


dec = 344

print("{0:b}".format(dec))
print("{0:d}".format(dec))
print("{0:o}".format(dec))
print("{0:x}".format(dec))
print("%i" %(dec))    



# Python program to convert decimal into other number systems
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")



# 4.Python Program to Find ASCII Value of Character

# Bu proqramda siz simvolun ASCII dəyərini tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Əsas Giriş və Çıxış
# Python Proqramlaşdırma Quraşdırılmış Funksiyaları
# ASCII, Məlumat Mübadiləsi üçün Amerika Standart Kodunu ifadə edir.

# Bu, kompüterlərin saxlaması və manipulyasiyası üçün müxtəlif simvol və simvollara verilən rəqəmli dəyərdir.
#  Məsələn, 'A' hərfinin ASCII dəyəri 65-dir.

# Mənbə kodu
# Verilmiş simvolun ASCII qiymətini tapmaq üçün proqram

c = 'p'
print(f"'p' herfinin ASCII deyeri {ord('p')}")


# Program to find the ASCII value of the given character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c)) 



# 5. Python Program to Find HCF or GCD

# HCF və ya GCD tapmaq üçün Python proqramı
# Bu nümunədə siz iki fərqli metoddan istifadə edərək iki ədədin GCD-ni tapmağı öyrənəcəksiniz: 
# funksiya və döngələr və Evklid alqoritmi

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Funksiyaları
# Python rekursiyası
# Python Funksiya Arqumentləri

# İki ədədin ən yüksək ümumi əmsalı (H.C.F)(Highest Common Factor) və ya ən böyük ortaq bölən (G.C.D)
# (Greatest Common Divisor) verilmiş iki ədədi mükəmməl şəkildə  bölən ən böyük müsbət tam ədəddir. 
# Məsələn, 12 və 14-ün H.C.F 2-dir.

def H_C_F(a1,b1):
    if a1 < b1:
        smaller = a1
    else:
        smaller = b1
    for i in range(smaller,0, -1):
        if not a1 % i and not b1 % i:
            c1 = i
            break           
    return c1            

a1 = int(input())
b1 = int(input())
print(H_C_F(a1, b1))                



def h_c_f(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a            

a = int(input())
b = int(input())
print(h_c_f(a, b))



# Python program to find H.C.F of two numbers
# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:   
        smaller = y
    else:
        smaller = x
    for i in range(smaller, 0, -1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            break 
    return hcf

x = int(input())
y = int(input())

print("The H.C.F. is", compute_hcf(x, y))



# 6. Python Program to Find LCM

# Bu proqramda siz iki ədədin LCM-ni tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python while Loop
# Python Funksiyaları
# Python Funksiya Arqumentləri
# Python İstifadəçi tərəfindən təyin olunan funksiyalar

# İki ədədin ən kiçik ümumi çoxluğu (L.C.M.)( least common multiple) verilmiş iki ədədə mükəmməl bölünən ən kiçik 
# müsbət tam ədəddir. Məsələn, L.C.M. 12 və 14-ün sayı 84-dür.

def H_C_F(a,b ):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = int(input())
b = int(input())    
H_C_F(a, b)

L_C_M = (a*b) / (H_C_F(a, b))
print(int(L_C_M))



# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
    if x > y:
       greater = x
    else:
       greater = y
    i = 1
    while(True):
        lcm = greater * i
        if((lcm % x == 0) and (lcm % y == 0)):
            break
        i += 1
    return lcm

x = int(input())
y = int(input())
print("The L.C.M. is", compute_lcm(x, y))



# 7. Python Program to Find the Factors of a Number    

# Bu proqramda siz for loopundan istifadə edərək ədədin amillərini tapmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python if...else Bəyanat
# Döngü üçün Python
# Python İstifadəçi tərəfindən təyin olunan funksiyalar
# Mənbə kodu
# Ədədin amillərini tapmaq üçün # Python proqramı

# Bu funksiya ötürülən arqumentin faktorunu hesablayır        


def ededin_bolenleri(a):
    for i in range(1, a+1):
        if not a % i:
            print(i)

n = int(input())
ededin_bolenleri(n)



# Python Program to find the factors of a number

# This function computes the factor of the argument passed


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)



def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

x = int(input())
print_factors(x)






# 8. Python Program to Make a Simple Calculator

# Bu nümunədə siz istifadəçinin daxil etdiyi məlumatdan asılı olaraq əlavə edə, çıxa, çoxalda və ya bölməyə qadir olan
#  sadə kalkulyator yaratmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Funksiyaları
# Python Funksiya Arqumentləri
# Python İstifadəçi tərəfindən təyin olunan funksiyalar
# Nümunə: Funksiyalardan istifadə etməklə sadə kalkulyator
# Proqram sadə kalkulyator hazırlayır

# Bu funksiya iki ədəd əlavə edir

def kalkulyator(a8, b8, c8):
    if b8 == "+":
        d8 = a8 + c8
        return d8
    elif b8 == "-":
        d8 = a8 - c8
        return d8
    elif b8 == "*":
        d8 = a8 * c8
        return d8  
    elif b8 == "/":
        d8 = a8 / c8
        return d8       

a8 = int(input())
b8 = input()
c8 = int(input())
print(kalkulyator(a8, b8, c8))




# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")




# 9. Python Program to Shuffle Deck of Cards  ????????????????????????????????? 

# Bu proqramda siz təsadüfi moduldan istifadə edərək kartların göyərtəsini qarışdırmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Döngü üçün Python
# Python Modulları
# Python Təsadüfi Modul
# Python Proqramlaşdırma Quraşdırılmış Funksiyaları
# Mənbə kodu
# Kart destesini qarışdırmaq üçün Python proqramı

# modulların idxalı
# itertools, təsadüfi idxal

# kart göyərtəsi hazırlayın

# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])








# 10. Python Program to Display Calendar   ???????????????????????????????

# Python-da tarixlə bağlı tapşırıqlarla işləmək üçün daxili funksiya, təqvim var. Bu nümunədə verilmiş tarixin təqvimini
#  göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Modulları
# Python Proqramlaşdırma Quraşdırılmış Funksiyaları
# Aşağıdakı proqramda biz təqvim modulunu idxal edirik. Modul daxilində quraşdırılmış month() funksiyası il və ayı 
# götürür və ilin həmin ayı üçün təqvimi göstərir.

# Mənbə kodu
# Verilən ayın və ilin təqvimini göstərmək üçün proqram

# təqvim modulunun idxalı

import calendar

print(calendar.month(2014, 11))



# 11. Python Program to Display Fibonacci Sequence Using Recursion

# Bu proqramda siz rekursiv funksiyadan istifadə edərək Fibonacci ardıcıllığını göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Döngü üçün Python
# Python Funksiyaları
# Python rekursiyası
# Fibonaççi ardıcıllığı 0, 1, 1, 2, 3, 5, 8... tam ədədlər ardıcıllığıdır.

# İlk iki hədd 0 və 1-dir. Bütün digər şərtlər əvvəlki iki şərti əlavə etməklə əldə edilir. Bu o deməkdir ki, n-ci hədd
#  (n-1) və (n-2)-ci hədlərin cəmidir.

# Mənbə kodu
# Fibonacci ardıcıllığını göstərmək üçün # Python proqramı


def fabionacci(n11):
    a11 = 0
    b11 = 1
    print(a11)
    print(b11)
    for i in range(3, n11+1):
        a11, b11 = b11, a11 + b11
        print(b11)

n11= int(input())

fabionacci(n11)


################################
# Factorial meselesi
def recur_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*recur_fact(n-1)    

n = int(input())
print(recur_fact(n))
#################################


def recur_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recur_fib(n-1) + recur_fib(n-2)

a = int(input())
if a < 0:
    print("Plese enter a positive integer")
else:
    for i in range(1, a + 1):
        print(recur_fib(i))




# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))






# 12. Python Program to Find Sum of Natural Numbers Using Recursion

# Bu proqramda siz rekursiv funksiyadan istifadə edərək natural ədədlərin cəmini tapmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python if...else Bəyanat
# Python Funksiyaları
# Python rekursiyası
# Aşağıdakı proqramda verilmiş ədədə cəmini hesablamaq üçün recur_sum() rekursiv funksiyasından istifadə etdik.

# Mənbə kodu
# Rekursiv funksiyadan istifadə edərək təbii cəmini tapmaq üçün # Python proqramı


def recur_sum(n):
    if n <= 1:
        return n
    else:
        return recur_sum(n-1) + n    

number = int(input("enter number:"))
print(recur_sum(number))



# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))





# 13. Python Program to Find Factorial of Number Using Recursion


# Bu proqramda siz rekursiv funksiyadan istifadə edərək ədədin faktorialını tapmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python if...else Bəyanatı
# Python Funksiyaları
# Python Rekursiyası
# Ədədin faktorialı 1-dən həmin ədədə qədər olan bütün tam ədədlərin hasilidir.

# Məsələn, 6-nın faktorialı 1*2*3*4*5*6 = 720-dir. Mənfi ədədlər üçün faktorial müəyyən edilmir və
# sıfırın faktorialı birdir, 0! = 1.

# Mənbə Kodu
# Rekursiyadan istifadə edən ədədin faktorialı


def recur_fac(n):
    if n <= 1:
        return 1
    else:
        return n*recur_fac(n-1)

number = int(input("enter number:"))
if number < 0:
    print("There is no factorial of negative numbers")
else:
    print(recur_fac(number))




# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))




# 14. Python Program to Convert Decimal to Binary Using Recursion

# Bu proqramda siz rekursiv funksiyadan istifadə edərək onluq ədədi ikiliyə çevirməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python if...else Bəyanat
# Python Funksiyaları
# Python rekursiyası
# Ondalıq ədəd, ədədi ardıcıl olaraq 2-yə bölmək və qalanı tərs qaydada çap etməklə ikiliyə çevrilir.


def binary_2(n) -> str:
    str1 = ""
    while n > 0:
        str1 += str(n % 2)
        n //= 2
    return str1[::-1]

number = int(input("enter number:"))
print(binary_2(number))

for i in binary_2(number):
    print(i)
        

def binary_2(n):
    str1 = ""
    k = n
    for i in range(n, 0, -1):
        str1 += str(k % 2)
        k //= 2
        if k ==0:
            break
    return str1[::-1]

number = int(input())
print(binary_2(number))



def binary_2(n):
    str1 = ""
    for i in range(n, 0, -1):
        str1 += str(n % 2)
        n //= 2
        if n == 0:
            break
    return str1[::-1]

number = int(input())
print(binary_2(number))



def binary_recur(n):
    if n <=1:
        return "1"
    else:
        return binary_recur(n // 2)  +  str(n % 2) 


n = int(input())
print(binary_recur(n))



# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input())

convertToBinary(dec)
print()



# 15. Python Program to Return Multiple Values From a Function

# Bu nümunədə siz bir funksiyadan çoxlu qiymət qaytarmağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:
# Python Funksiyaları
# Misal 1: Vergüldən istifadə edərək dəyərləri qaytarın



def name():
    return "John","Armin"

# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)
print(name_1)



################################################
def func(a, b):
    if a ==b:
        raise KeyError("acar sehvi")
    else:
        raise NameError(" ad sehv daxil edilib")    

a = 2
b = 2
func(a, b)
#################################################































































