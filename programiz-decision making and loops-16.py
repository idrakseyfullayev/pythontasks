#                    ##  Proqramiz-Decision Making and Loops-16.Ev tapsiriqlari ##


# 1. Python Program to Check if a Number is Positive, Negative or 0

# Rəqəmin müsbət, mənfi və ya 0 olduğunu yoxlamaq üçün Python proqramı
# Bu nümunədə istifadəçinin daxil etdiyi rəqəmin müsbət, mənfi və ya sıfır olduğunu yoxlamağı öyrənəcəksiniz. 
# Bu problem if...elif...else və nested if...else ifadəsi ilə həll edilir.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Python Əsas Giriş və Çıxış
# Mənbə kodu: if...elif...else istifadə edərək

def check_number(n):
    if n > 0:      #   burda number yazdim sehv vermedi??????????????????
        return "number is positive"
    elif n < 0:
        return "number is negative"
    else:
        return "you enter zero"     

number = int(input())
print(check_number(number))



num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")



# Burada if...elif...else ifadəsindən istifadə etdik. Eyni şeyi nested if ifadələrindən istifadə edərək aşağıdakı kimi 
# edə bilərik.
# Mənbə kodu: Nested if istifadə

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")




# 2. Python Program to Check if a Number is Odd or Even

# Rəqəmin tək və ya cüt olduğunu yoxlamaq üçün Python proqramı
# Bu nümunədə siz istifadəçinin daxil etdiyi nömrənin cüt və ya tək olduğunu yoxlamağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Operatorları
# Python if...else Bəyanat
# Ədəd 2-yə tam bölünsə belə belədir. Ədəd 2-yə bölündükdə qalığı hesablamaq üçün % qalıq operatorundan istifadə 
# edirik. 
# Qalan sıfır deyilsə, ədəd təkdir.

# Mənbə kodu

# Giriş nömrəsinin tək və ya cüt olduğunu yoxlamaq üçün Python proqramı.
# 2-yə bölmək 0-ın qalığını verərsə, ədəd hətta olar.
# Qalan 1-dirsə, tək ədəddir.


def check_number(n):
    if not n % 2 and n > 0:
        return "number is even"
    elif n % 2:
        return "number is odd"
    else:
        return "0 is neither odd nor even." 

number = int(input("enter number:"))
print(check_number(number))



num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))




# 3. Python Program to Check Leap Year

# Sıçrayış ilini yoxlamaq üçün Python proqramı
# Bu proqramda siz bir ilin artıq il olub olmadığını yoxlamağı öyrənəcəksiniz. Bu problemi həll etmək üçün iç içə
#  if...else istifadə edəcəyik.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Operatorları
# Python if...else Bəyanat
# Əsr illəri (00 ilə bitən illər) istisna olmaqla, sıçrayış ili tam olaraq 4-ə bölünür. Əsr ili yalnız 400-ə tam 
# bölünərsə, sıçrayış ilidir. 
# Məsələn,
# 2017-ci il sıçrayış ili deyil
# 1900-cü il sıçrayış ili deyil
# 2012-ci il sıçrayış ilidir
# 2000-ci il sıçrayış ilidir


def leap_year(n):
    if not n % 400:
        return f"{n} is leap year" 
    elif not n % 4 and n % 100:
        return f"{n} is leap year"  
    else:
        return f"{n} isn't leap year" 

    # return True if (not n % 4 and n % 100) or not n % 400 else False

year = int(input("enter year:"))
print(leap_year(year))



# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))




# 4. Python Program to Find the Largest Among Three Numbers

# Üç ədəd arasında ən böyüyü tapmaq üçün Python proqramı
# Bu proqramda siz if else istifadə edərək üç ədəd arasında ən böyüyü tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Python Əsas Giriş və Çıxış
# Aşağıdakı proqramda üç rəqəm müvafiq olaraq num1, num2 və num3-də saxlanılır. Biz if...elif...else nərdivanından
#  üçü arasında ən böyüyü tapmaq və onu göstərmək üçün istifadə etdik.

# Mənbə kodu
# Üç giriş nömrəsi arasında ən böyük ədədi tapmaq üçün Python proqramı

# num1, num2 və num3 dəyərlərini dəyişdirin
# fərqli nəticə üçün
# 1 = 10
# 2 = 14
# 3 = 12

# istifadəçidən üç rəqəm almaq üçün aşağıdakı sətirləri şərhdən çıxarın
#num1 = float(input("Birinci nömrəni daxil edin:"))
#num2 = float(input("İkinci nömrə daxil edin: "))
#num3 = float(input("Üçüncü nömrə daxil edin: "))


num1 = float(input("enter the first numer:"))
num2 = float(input("enter the second number:"))
num3 = float(input("enter the thrid number:"))

def to_find_the_largest(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return f"{n1} is the largest of these numbers"
    elif n2 >= n1 and n2 >= n3:
        return f"{n2} is the largest of these numbers"
    else:
        return f"{n3} is the largest of these numbers"

print(to_find_the_largest(num1, num2, num3))




# # Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
# num1 = 10
# num2 = 14
# num3 = 12

# # uncomment following lines to take three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)





# 5. Python Program to Check Prime Number

# Baş Nömrəni Yoxlamaq üçün Python Proqramı
# Tam ədədin sadə ədəd olub-olmadığını yoxlamaq üçün misal for loop və if...else ifadəsindən istifadə etmir. 
# Əgər ədəd sadə deyilsə, onun niyə sadə ədəd olmadığı çıxışda izah olunur.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Döngü üçün Python
# Python qırılır və davam edir
# 1-dən və ədədin özündən başqa heç bir faktoru olmayan 1-dən böyük müsbət tam ədədə sadə ədəd deyilir. 2, 3, 5, 7
#  və s. başqa amilləri olmadığı üçün sadə ədədlərdir. Lakin 6 əsas deyil (kompozitdir), çünki 2 x 3 = 6.

# Misal 1: Bayraq dəyişəninin istifadəsi

def check_prime_number(n):
    for i in range(2, n):
        if not n % i:
            return f"{n} is a composite number"
    else:
        if n == 1:
            return f"{n} is neither a prime nor a composite number "
        else:
            return f"{n} is a prime number"

    if n < 1:
        return "Yalnis daxiletme"
    elif n == 1:
        return "Ne sadedir ne murekkeb"
    for i in range(2, n):
        if not n % i:
            return "Murekkebdir"
    else:
        return "Sadedir"

    x = 0
    for i in range(2, n):
        if not n % i:
            x = 1

    return "Sade" if not x else "Murekkeb"
            

#     """
#     n < 1  Sehv
# #     n = 1  Ne sade ne murekkeb
# #     n > 1 
# #     """
                    
# num =  int(input())

# print(check_prime_number(num))




# Program to check if a number is prime or not
# num = 29

# # To take input from the user
# #num = int(input("Enter a number: "))

# # define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
     

# Bu proqramda biz numun əsas olub olmadığını yoxladıq. 1-dən kiçik və ya ona bərabər olan ədədlər sadə ədədlər deyil. 
# Beləliklə, biz yalnız ədəd 1-dən böyük olduqda davam edirik.

# Biz ədədin 2-dən ədədə kimi istənilən ədədə tam bölünüb-bölünmədiyini yoxlayırıq - 1. Əgər həmin diapazonda bir amil
#  tapsaq, ədəd sadə deyil, ona görə də biz bayrağı True olaraq təyin edirik və dövrədən çıxırıq.

# Döngədən kənarda bayrağın True və ya False olduğunu yoxlayırıq.

# Əgər doğrudursa, ədəd sadə ədəd deyil.
# Yanlışdırsa, num sadə ədəddir.
# Qeyd: Faktorları axtardığımız nömrələr diapazonunu azaltmaqla proqramımızı təkmilləşdirə bilərik.

# Yuxarıdakı proqramda axtarış diapazonumuz 2-dən 1-ə qədərdir.

# Biz diapazon, diapazon(2,num//2) və ya diapazondan(2,math.floor(math.sqrt(num)+1)) istifadə edə bilərdik. Sonuncu 
# diapazon, kompozit ədədin həmin ədədin kvadrat kökündən kiçik və ya ona bərabər əmsalı olması faktına əsaslanır. 
# Əks halda, rəqəm əsasdır.

# Ədədin digər tam ədədlər üçün sadə olub-olmadığını yoxlamaq üçün yuxarıdakı mənbə kodundakı num dəyişəninin dəyərini
#  dəyişə bilərsiniz.

# Python-da biz əlavə bayraq dəyişənindən istifadə etmədən bu tapşırığı yerinə yetirmək üçün for...else ifadəsindən də
#  istifadə edə bilərik.


# num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")  #  bu serti niye verib ki burda men ehtiyaci gormedim?????????????


# Burada numun əsas olub-olmadığını yoxlamaq üçün for..else ifadəsindən istifadə etdik.
# Bu məntiq üzərində işləyir ki, for döngəsinin else bəndi yalnız və yalnız for döngəsindən çıxmadığımız halda işləyir.
#  Həmin şərt yalnız heç bir faktor tapılmadıqda yerinə yetirilir, yəni verilmiş ədəd sadədir.
# Beləliklə, else bəndində rəqəmin sadə olduğunu çap edirik.




# 6. Python Program to Print all Prime Numbers in an Interval

# Bütün sadə ədədləri intervalda çap etmək üçün Python proqramı
# Bu proqramda siz for döngələrindən istifadə edərək intervalda bütün sadə ədədləri çap etməyi və onu göstərməyi 
# öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Döngü üçün Python
# Python qırılır və davam edir
# 1-dən və ədədin özündən başqa heç bir faktoru olmayan 1-dən böyük müsbət tam ədədə sadə ədəd deyilir.

# 2, 3, 5, 7 və s. başqa amilləri olmadığı üçün sadə ədədlərdir. Lakin 6 əsas deyil (kompozitdir), çünki 2 x 3 = 6.

# Mənbə kodu

# Python proqramı bütün sadə nömrələri intervalda göstərmək üçün

lower = int(input())
upper = int(input())

def check_prime_numbers(n, z):
    for i in range(n+1, z):
        c1 = 0
        for j in range(2, i):
            if not i % j:
                c1 += 1
                break
        if c1 == 0:
            print(i, end=", ")

check_prime_numbers(lower, upper)
print()  ## ezber yadimda qalib mentiqi olaraq niye alta gonderir setri bilmedim?????????????????


# Muellfifin yazdigina baxanda sonra bildim ki bu cur de yazmaq olardi!!!!!!!!!!!!!!!!!!!!!
##################################
lower = int(input())
upper = int(input())

def check_prime_numbers(n, z):
    for i in range(n+1, z):
        for j in range(2, i):
            if not i % j:
                break
        else:            
            print(i, end=", ")

check_prime_numbers(lower, upper)
print()
###################################


# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)




# 7. Python Program to Find the Factorial of a Number

# Ədədin faktorialını tapmaq üçün Python proqramı
# Bu yazıda siz ədədin faktorialını tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Döngü üçün Python
# Python rekursiyası
# Ədədin faktorialı 1-dən həmin ədədə qədər olan bütün tam ədədlərin hasilidir.

# Məsələn, 6-nın faktorialı 1*2*3*4*5*6 = 720-dir. Mənfi ədədlər üçün faktorial müəyyən edilməyib, sıfırın faktorialı
#  isə birdir, 0! = 1.

# Döngüdən istifadə edərək ədədin faktorialı
# Python proqramı istifadəçi tərəfindən verilən ədədin faktorialını tapmaq üçün.

# fərqli nəticə üçün dəyəri dəyişdirin
# ədəd = 7

# İstifadəçidən məlumat almaq üçün
#num = int(input("Nömrə daxil edin: "))

faktorial = 1


def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    else:    
        c1 = 1
        for i in range(2, n+1):
            c1 *= i
        return f"{n} factorial is {c1}"
        
num = int(input())
print(fact(num))



# Python program to find the factorial of a number provided by the user.

# change the value for a different result
# num = 7

# # # To take input from the user
# # #num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# Qeyd: Proqramı fərqli nömrə üçün yoxlamaq üçün num dəyərini dəyişdirin.

# Burada faktorialı tapılmalı olan ədəd num şəklində saxlanılır və if...elif...else ifadəsindən istifadə edərək
# rəqəmin mənfi, sıfır və ya müsbət olub olmadığını yoxlayırıq. Əgər ədəd müsbət olarsa, faktorialı hesablamaq 
# üçün for loop və range() funksiyasından istifadə edirik.

# iterasiya         faktorial*i (qaytarılmış dəyər)
# i = 1             1 * 1 = 1
# i = 2             1 * 2 = 2
# i = 3             2 * 3 = 6
# i = 4             6 * 4 = 24
# i = 5             24 * 5 = 120
# i = 6             120 * 6 = 720
# i = 7             720 * 7 = 5040



# Rekursiyadan istifadə edən ədədin faktorialı

# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# # change the value for a different result
num = 7

# # to take input from the user
num = int(input("Enter a number: "))


from math import factorial
# # call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


# Muellifin funksiyasi menfi ve sifir ededlerde error verirdi, istedim try except ile duzeldim alinmadi?
# Ancaq bu cur duzelis verdim
###############################################
def factorial(x):
    if x == 1 or x ==0:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input())
if num < 0:
    print("Factorial is not defined for negative numbers")
else:    
    y = factorial(num)
    print(f"{num} factorial is {y}")
#################################################




# 8. Python Program to Display the multiplication Table

# Vurma Cədvəlini göstərmək üçün Python Proqramı
# Bu proqram num dəyişəninin vurma cədvəlini göstərir (1-dən 10-a qədər).

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Döngü üçün Python
# Python Əsas Giriş və Çıxış
# Aşağıdakı proqramda 12-nin vurma cədvəlini göstərmək üçün for döngəsindən istifadə etdik.

# Mənbə kodu
# Python-da vurma cədvəli (1-dən 10-a qədər).

# sayı = 12

# İstifadəçidən məlumat almaq üçün
# num = int(input("Vurma cədvəlini göstərin?"))

# i = 1-dən 10-a qədər 10 dəfə təkrarlayın


# lambda ile yazdim!
###############################################
n = int(input())
list1 = list(map(lambda n: 12*n, range(1, n)))   

c1 = 0
for i in list1:
    c1 +=1
    print(f"12^{c1} = {i}")
###############################################


def multiplication_table_of_12(n):
    for i in range(1, n):
        print(f"12^{i} = {12*i}")

multiply_number = int(input())
multiplication_table_of_12(multiply_number)



# Multiplication table (from 1 to 10) in Python

# num = 12

# # To take input from the user
# # num = int(input("Display multiplication table of? "))

# # Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# Burada 10 dəfə təkrarlamaq üçün interval() funksiyası ilə birlikdə for loopundan istifadə etdik. range() funksiyasının
#  daxilindəki arqumentlər (1, 11)-dir. Mənası, 1-dən böyük və ya bərabər və 11-dən kiçik.
# Num dəyişəninin vurma cədvəlini göstərdik (bizim vəziyyətimizdə bu 12-dir). Digər dəyərləri yoxlamaq üçün yuxarıdakı 
# proqramda num dəyərini dəyişə bilərsiniz.

#????????????????????????????????????????????????????????????????????????????????????????/




# 9. Python Program to Print the Fibonacci sequence

# Fibonacci ardıcıllığını çap etmək üçün Python proqramı
# Bu proqramda siz while loopundan istifadə edərək Fibonacci ardıcıllığını çap etməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Python while Loop
# Fibonaççi ardıcıllığı 0, 1, 1, 2, 3, 5, 8... tam ədədlər ardıcıllığıdır.

# İlk iki şərt 0 və 1-dir. Bütün digər şərtlər əvvəlki iki şərti əlavə etməklə əldə edilir. Bu o deməkdir ki, n-ci
#  hədd (n-1) və (n-2)-ci hədlərin cəmidir.

# Mənbə kodu
# n-ci dövrə qədər Fibonacci ardıcıllığını göstərmək üçün proqram

nterms = int(input("Neçə termin? "))

# ilk iki müddət
n1, n2 = 0, 1
say = 0

def Fibonacci(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(3, n+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
        

num = int(input())
Fibonacci(num)



def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

num = int(input())
for i in range(1, num+1):
    print(Fibonacci(i))



# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1






# 10. Python Program to Check Armstrong Number
# Armstrong nömrəsini yoxlamaq üçün Python proqramı
# Bu nümunədə siz n-rəqəmli tam ədədin Armstronq nömrəsi olub-olmadığını yoxlamağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Python while Loop
# Müsbət tam ədədə Armstronq sırası n if adlanır

# abcd... = an + bn + cn + dn + ...
# Armstronq nömrəsinin 3 rəqəmi olması halında, hər rəqəmin kublarının cəmi həmin rəqəmin özünə bərabərdir. Misal üçün:

# 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 Armstronq nömrəsidir.
# Mənbə kodu: Armstrong nömrəsini yoxlayın (3 rəqəm üçün)
# Nömrənin Armstrong nömrəsi olub-olmadığını yoxlamaq üçün # Python proqramı

# istifadəçidən giriş götürün
num = int(input("Nömrə daxil edin:"))


def check_Armstrong_number(n):
    n = str(n)
    z = 0
    for i in n:
        z += (int(i))**len(n)
    if int(n) == z:
        return f"{int(n)} is Armstrong number"
    else:
        return f"{int(n)}  isn't Armstrong number"


num = int(input("enter number:"))
if num < 0:
    print("you enter negativ number")
elif num == 0:
    print("you enter zero")    
else:    
    print(check_Armstrong_number(num))



# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))

# # initialize sum
sum = 0

# # find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# # display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# Burada istifadəçidən nömrə istəyirik və onun Armstrong nömrəsi olub-olmadığını yoxlayırıq.

# Hər rəqəmin kubunun cəmini hesablamalıyıq. Beləliklə, cəmini 0-a endiririk və % modul operatorundan istifadə edərək
# hər bir rəqəmi əldə edirik. Ədədin 10-a bölündüyü zaman qalanı həmin ədədin sonuncu rəqəmidir. Göstərici operatordan
# istifadə edərək kubları götürürük.

# Nəhayət, cəmini ilkin ədədlə müqayisə edirik və belə nəticəyə gəlirik ki, əgər onlar bərabərdirsə, Armstronq 
# nömrəsidir.

# Mənbə Kodu: Armstrongun n rəqəminin sayını yoxlayın

num = 1634

# # Changed num variable to string, 
# # and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# Mənbə kodundakı num dəyərini dəyişdirə və test etmək üçün yenidən işə sala bilərsiniz.


#  def-e yazim bunu!!!!!!!!!!!

def check_number(n):
   sum = 0
   x = len(str(n))
   z = n
   while z > 0:
      sum += (z % 10)**x
      z //= 10 
   if n == sum:
      return f"{n} is Armstrong number"
   else:
      return f"{n} isn't Armstrong number "    

num = int(input("enter number:"))
print(check_number(num))




# 11. Python Program to Find Armstrong Number in an Interval

# Armstronq nömrəsini bir intervalda tapmaq üçün Python proqramı
# Bu nümunədə Python-da iki interval arasında mövcud olan bütün Armstrong nömrələrini tapmağı öyrənəcəyik.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Python while Loop
# Müsbət tam ədədə Armstronq n sıralı ədəd deyilir

# abcd... = an + bn + cn + dn + ...
# Misal üçün,

# 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 Armstronq nömrəsidir.
# Python-da nömrənin Armstrong nömrəsi olub-olmadığını necə yoxlaya biləcəyinizi öyrənmək üçün bu səhifəyə daxil olun.

# Mənbə kodu
# Armstrong nömrələrini müəyyən intervalda yoxlamaq üçün proqram

lower = 100
upper = 2000


def check_Armstrong_number(n, z):
   c1 = 0
   for i in range(n, z+1):
      sum = 0
      x = len(str(i)) # x = 4

      for j in str(i):
        sum += int(j)**x


    #   z = i
    #   while z > 0:
    #      sum += (z % 10)**x
    #      z //= 10
      if i == sum:
         c1 = 1
         print(i, end=", ")
   if c1 == 0:
      print("There are not Armstrong numbers")      
                 
lower = int(input("enter number:"))
upper = int(input("enter nunmber:"))
check_Armstrong_number(lower, upper)


# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# Burada biz dəyişən aşağı həddi 100, yuxarı dəyişəndə ​​isə yuxarı həddi 2000 təyin etdik. Dəyişən aşağıdan yuxarıya
#  doğru təkrarlamaq üçün for loopundan istifadə etdik. İterasiyada aşağının dəyəri 1 artır və onun Armstronq nömrəsi
#  olub-olmaması yoxlanılır.
# Siz diapazonu dəyişdirə və aşağı və yuxarı dəyişənləri dəyişdirərək test edə bilərsiniz. Qeyd edək ki, bu proqramın
#  düzgün işləməsi üçün aşağı dəyişən yuxarıdan aşağı olmalıdır.




# 12. Python Program to Find the Sum of Natural Numbers

# Natural ədədlərin cəmini tapmaq üçün Python proqramı
# Bu proqramda siz while döngüsündən istifadə edərək n natural ədədin cəmini tapmağı və onu göstərməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Python while Loop
# Aşağıdakı proqramda num-a qədər natural ədədlərin cəmini hesablamaq üçün if...else ifadəsindən while dövrəsi ilə 
# birlikdə istifadə etdik.

# Mənbə kodu

# Num qədər natural ədədlərin cəmi
# sayı = 16


def find_the_sum(n):
   sum = 0
   for i in range(1, n+1):
      sum += i
   return f"Sum_{n} = {sum}"

number = int(input())
print(find_the_sum(number))




# Sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# Qeyd: Proqramı fərqli nömrə üçün yoxlamaq üçün num dəyərini dəyişdirin.
# Əvvəlcə cəmi 0-a təyin edilir. Və nömrə dəyişən numda saxlanılır.
# Sonra, biz ədəd sıfır olana qədər təkrarlamaq üçün while döngəsindən istifadə etdik. Döngənin hər iterasiyasında
# biz cəmə ədədi əlavə etdik və ədədin dəyəri 1 azaldılır.


# Aşağıdakı düsturdan istifadə etməklə yuxarıdakı problemi döngədən istifadə etmədən həll edə bilərdik.

# n*(n+1)/2
# Məsələn, n = 16 olarsa, cəmi (16*17)/2 = 136 olardı.

# Növbəniz: Aşağıdakı düsturdan istifadə edərək natural ədədlərin cəmini tapmaq üçün yuxarıdakı proqramı dəyişdirin.


def find_the_sum(n):
   return f"Sum_{n} = {(n*(n+1)) / 2}"

number = int(input())
print(find_the_sum(number))





# 13. Python Program to Create Pyramid Patterns

# Piramida nümunələri yaratmaq üçün Python proqramı
# Bu nümunədə siz Python Proqramlaşdırmada yarım piramidaları, tərs piramidaları, tam piramidaları, tərs tam 
# piramidaları, Paskal üçbucağını və Floyd üçbucağını çap etməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python if...else Bəyanat
# Döngü üçün Python
# Python while Loop
# Python qırılır və davam edir
# Mənbə kodunun siyahısı
# *, rəqəmlər və simvollardan istifadə edərək üçbucaqları çap etmək üçün kod
# * və rəqəmlərdən istifadə edərək tərs üçbucaqları çap etmək üçün kod
# Tam piramidaları çap etmək üçün kod
# Paskal üçbucağını çap etmək üçün kod
# Floydun üçbucağını çap etmək üçün kod
# *, rəqəmlər və simvollardan istifadə edərək üçbucaqları çap etmək üçün proqramlar

# Nümunə 1: * istifadə edərək yarım piramida çap etmək üçün proqram
# *
# * *
# * * *
# * * * *
# * * * * *

  
def half_pyramid(n):
    for i in range(1, n+1):
        print("* " * i)

num = int(input())
half_pyramid(num)



rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()



rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")



# Yuxarıdakı proqramda nümunənin necə çap edildiyinə baxaq.

# Əvvəlcə istifadəçidən piramida sıralarının hündürlüyünü alırıq.
# Birinci döngədə i = 0-dan i = sətirlərə qədər təkrar edirik.
# İkinci dövrə j = 0-dan i + 1-ə qədər işləyir. Bu döngənin hər təkrarlanmasında biz yeni sətir 
# olmadan i + 1 ədəd * çap edirik. Burada sətir nömrəsi həmin sətirdə çap üçün tələb olunan * sayını verir. 
# Məsələn, 2-ci cərgədə iki * çap edirik. Eynilə, 3-cü cərgədə üç * çap edirik.
# Daxili döngə bitdikdən sonra yeni sətir çap edirik və yeni sətirdə * çap etməyə başlayırıq.

################################################################################################################


# Nümunə 2: Rəqəmlərdən istifadə edərək yarım piramida a çap etmək üçün proqram
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def half_pyramid_using_number(n):
    str1 = ""
    for i in range(1, n+1):
        str1 += str(i) + " "
        print(str1)
        # print()
        
num = int(input())
half_pyramid_using_number(num)




def half_pyramid_number(n):
    for i in range(0, n):
        for j in range(1, i+1+1):
            print(j, end=" ")
        print()

num = int(input())
half_pyramid_number(num)





rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")


# Yuxarıdakı proqramda nümunənin necə çap edildiyinə baxaq.
# Əvvəlcə istifadəçidən piramida sıralarının hündürlüyünü alırıq.
# Birinci döngədə i = 0-dan i = sətirlərə qədər təkrar edirik.
# İkinci döngədə 1-dən j-ə qədər rəqəmləri çap edirik, burada j 0-dan i-ə qədər dəyişir.
# Birinci döngənin hər iterasiyasından sonra yeni bir sətir çap edirik.

##############################################################################################################


# Misal 3: Əlifbalardan istifadə edərək yarım piramida çap etmək üçün proqram

def pyramid_using_alphabets(alphabet): 
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = alphabets.index(alphabet)
    for i in range(x+1):
        print((alphabets[i] + " ") * (i+1))

alphabet = input()
pyramid_using_alphabets(alphabet)



rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")



# Yuxarıdakı nümunənin işi də yuxarıda müzakirə edilən digər nümunələrə bənzəyir, istisna olmaqla, ascii dəyərləri
# burada çap olunur. Əlifbalar üçün ascii dəyəri 65-dən başlayır (yəni A). Buna görə də, hər iterasiyada biz
# ascii_value dəyərini artırırıq və onun müvafiq əlifbasını çap edirik.

################################################################################################################



# * və rəqəmlərdən istifadə edərək tərs yarım piramida çap etmək üçün proqramlar

# Nümunə 4: * istifadə edərək tərs yarım piramida
# * * * * *
# * * * *
# * * *
# * *
# *


def half_pyramid(n):
    for i in range(n, 0, -1):
        print("* " * i)

num = int(input())
half_pyramid(num)



def half_pramid(n):
    for i in range(n, 0, -1):
    
        print("*" * i)

num = int(input())
half_pramid(num)




def half_pramid(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()    

num = int(input())
half_pramid(num)





rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print("\n")


# Bu nümunə dik piramidaya bənzəyir, istisna olmaqla, burada biz cərgələrin ümumi sayından başlayırıq və hər
# iterasiyada cərgələrin sayını 1 azaldırıq.

#################################################################################################################


# Nümunə 5: Rəqəmlərdən istifadə edərək tərs yarım piramida
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


def inverted_half_pyramid_using_numbers(n):
    str1 = ""
    for i in range(1, n+1):
        str1 += str(i)
    for i in range(len(str1), 0, -1):
        str2 =" ".join(str1[0:i])
        print(str2)
        # print()

    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

num = int(input())
inverted_half_pyramid_using_numbers(num)



def inverted_half_pyramid_using_number(n):
    for i in range(n, 0, -1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()    

num = int(input())
inverted_half_pyramid_using_number(num)




rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")

    print("\n")


# Rəqəmlərdən istifadə edən dik və tərs piramida arasındakı yeganə fərq, birinci döngənin cərgələrin ümumi 
# sayından 0-a qədər başlamasıdır.

################################################################################################################


# Tam piramidaları çap etmək üçün proqramlar

# Nümunə 6: * istifadə edərək tam piramidanı çap etmək üçün proqram
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


def full_pyramids(n):
    for i in range(n-1, -1, -1):
        print(("* " * ((2*n-1)-(2*i))).center((2*n-1)*2))

num = int(input())
full_pyramids(num)


#######################################################################
def pyramid(n):
    for i in range(1, n+1, 2):
        print(("*" * i).center(n))

num = int(input())
pyramid(num)
######################################################################
def pyramid(n):
    for i in range(1, n+1, 2):
        x = ("*" * i).center(n)
        y =" ".join(x)
        print(y)

num = int(input())
pyramid(num)
#########################################################################



####  ele de yaxsi anlamadim?????????????????????????????????

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    # while k!=(2*i-1):
    #     print("* ", end="")
    #     k += 1

    for j in range(1, 2*i):
        print("* ", end="")
    print()


# Bu piramida növü yuxarıda tədqiq etdiyimizlərdən bir qədər mürəkkəbdir.
# Ən xarici döngə i = 1-dən i = sətir + 1-ə qədər başlayır.
# İki daxili döngə arasında for döngəsi (sətir-i)+1 düsturundan istifadə edərək hər bir sıra üçün tələb olunan
# boşluqları çap edir, burada sətirlər cərgələrin ümumi sayı, i isə cari sıra nömrəsidir.
# while döngəsi 2 * i - 1 düsturundan istifadə edərək lazımi sayda ulduzları çap edir. Bu düstur hər bir sıra
# üçün ulduzların sayını verir, burada sıra i-dir.




# Nümunə 7: Ədədlərin Tam Piramidası
#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5




n = int(input())

for i in range(1, n + 1):
    x = i
    for k in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print(i+j-1, end=" ")

    print()





num = int(input())

def full_pyramid_of_numbers(n):
    for i in range(1, n + 1):
        for k in range(1, n-i+1):
            print(" ", end=" ")
        for j in range(i, 2*i):
            print(j, end=" ")    
        for z in range(2*i-2, i-1, -1):

            # if x == 0:
            #     break
            print(z, end=" ")
            # if z == i+1:
         #     break  
        
        print()
     
full_pyramid_of_numbers(num)





rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()


# 6-cı misal kimi, bu nümunə də for döngəsi daxilində iki döngədən istifadə edir.

# Xarici for döngəsi hər cərgədə təkrarlanır.
# Burada boşluqları və rəqəmləri çap etmək üçün müvafiq olaraq iki sayğacdan count və count1 istifadə edirik.
# Daxili for döngəsi (sətir-i)+1 düsturundan istifadə edərək tələb olunan boşluqları çap edir, burada sətirlər 
# cərgələrin ümumi sayı, i isə cari sıra nömrəsidir.
# while döngəsi rəqəmləri çap edir, burada 2 * i - 1 hər sətirdəki elementlərin sayını verir.





# Nümunə 8: *-in tərs tam piramidası
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *




def  Inverted_full_pyramid_of(n):
    for i in range(n):
        print(("* " * ((2*n-1)-(2*i))).center((2*n-1)*2))

num = int(input())
Inverted_full_pyramid_of(num)
        


def Inverted_full_pyramid_of(n):
    for i in range(n, 0, -2):
        print(("* " * i).center(n*2))

num = int(input())
Inverted_full_pyramid_of(num)




def Inverted_full_pyramid_of(n):
    for i in range(n, 0, -1):
        for j in range(1, n-i+1):
            print(" ", end=" ")
        
        for j in range(2*i, 1, -1):
            print("* ", end="")
        print()      

num = int(input())
Inverted_full_pyramid_of(num)



rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()


# Bu nümunədə biz cəmi 4 for döngəsindən istifadə etdik.
# Xarici for döngəsi i = sətirlərdən i = 1-ə qədər təkrarlanır.
# Birinci daxili for loop hər cərgədə tələb olunan boşluqları çap edir.
# İkinci daxili for loop piramidanın birinci yarısını (şaquli kəsilmiş), sonuncu daxili for loop isə digər yarısını
# çap edir.


# Example 9: Pascal's Triangle
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1



num = int(input())
def full_pyramid_of_numbers(n):
    for i in range(0, n+1):
        for k in range(1, n-i+1):
            print(" ", end="  ")
        for j in range(1, i+1):
            print(j, end="  ")
            
        for z in range(i+1, 0, -1):
            print(z, end="  ")
        print()
     
full_pyramid_of_numbers(num)



# Example 9: Pascal's Triangle
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1



binom = [[1], [1,1] ]

n = int(input())

for i in range(2, n+1):
    binom.append([])
    binom[i].append(1)
    for j in range(1,i):
        binom[i].append(binom[i-1][j-1] + binom[i-1][j])
    binom[i].append(1)
      
# print(binom)

for i in binom:
    if len(i) < len(binom):
        print(" ", end="")
    for k in range(len(binom)-len(i)):
        print(" ", end=" ")
    for j in i:
        print(j , end="   ")
    print()    




rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()


# Bu nümunədə biz üç for döngəsindən istifadə etdik.

# Xarici döngə 1-dən sətirlərə + 1-ə qədər təkrarlanır.
# Birinci daxili döngə boşluqları çap edir.
# İkinci daxili dövrə əvvəlcə coef = coef * (i - j) // j ifadəsindən istifadə edərək çap olunacaq nömrəni tapır və 
# sonra onu çap edir. Burada i sıra nömrəsi, j isə 0 ilə i arasında dəyişən dəyərdir.





# Example 10: Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10


def floryd_s_triangle(n):
    x = 1
    for i in range(n):
        # x = 1
        for j in range(1,i+2):
            print(x, end=" ")
            x += 1
        print()    
            
            

num = int(input())
floryd_s_triangle(num)            




rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()



# Bu ən asan nümunələrdən biridir.
# nömrə dəyişəni 1 dəyəri ilə işə salınır.
# Xarici for döngəsi 1-dən cərgələrin ümumi sayına qədər təkrarlanır.
# Daxili for döngəsi 1-dən i + 1-ə qədər başlayır, burada i sıra nömrəsidir. Hər iterasiyadan sonra nömrənin dəyəri artır.




# 14.  Python Program to Iterate Over Dictionaries Using for Loop

# Loop üçün istifadə olunan lüğətlər
# Bu nümunədə siz for loopundan istifadə edərək lüğətləri təkrarlamağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Döngü üçün Python
# Python lüğəti

# Misal 1: items() istifadə edərək həm açara, həm də dəyərə daxil olun

####    ???????????????????????????????????????

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)

[("a", "juice"), ("b", "grill"), ("c", "corn")]



# 15.  Python Program to Reverse a Number

# Nömrəni dəyişdirmək üçün Python proqramı
# Bu nümunədə siz rəqəmi tərsinə çevirməyi öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Döngü üçün Python
# Python while Loop
# Nümunə 1: Bir müddət döngəsindən istifadə edərək nömrəni tərsinə çevirin

num = 1234


def Reverse_a_Number(n):
    return f"{str(n)[::-1]}"

num = int(input())
print(Reverse_a_Number(num))


def Reverse_a_Number(n):
    i = 0
    str1 = ""
    while i < len(str(n)):
        str1 += str(n)[len(str(n))-1-i]
        i += 1
    return str1 
       
num = int(input())
print(Reverse_a_Number(num))




num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# print("Reversed Number: " + str(reversed_num))


# Bu proqramda, aşağıdakı addımlarda verildiyi kimi ədədi tərsinə çevirmək üçün while döngəsi istifadə olunur:
# Birincisi, 10-a bölünən ədədin qalan hissəsi dəyişən rəqəmində saxlanılır. İndi rəqəmin son rəqəmi, yəni 4 var.
# rəqəmi 10-a vurduqdan sonra əks dəyişənə əlavə edilir. 10-a vurma əks ədədə yeni yer əlavə edir. 1-ci yerin 10-a
#  vurulması onuncu yeri, onuncu yeri isə yüzüncü yeri verir və s. Bu halda, tərs_num 0 * 10 + 4 = 4 ehtiva edir.
# num sonra 10-a bölünür ki, indi yalnız ilk üç rəqəmi ehtiva edir: 123.
# İkinci iterasiyadan sonra rəqəm 3-ə bərabərdir, əksi 4 * 10 + 3 = 43 və ədəd = 12-ə bərabərdir.
# Üçüncü iterasiyadan sonra rəqəm 2-yə bərabərdir, əksi 43 * 10 + 2 = 432 və ədəd = 1-ə bərabərdir.
# Dördüncü iterasiyadan sonra rəqəm 1-ə bərabərdir, əksi 432 * 10 + 1 = 4321 və ədəd = 0-a bərabərdir.
# İndi num = 0, buna görə də test ifadəsi num != 0 uğursuz olur və while döngüsü çıxır. ters çevrilmiş artıq 4321
#  nömrəsini ehtiva edir.



# Misal 2: String dilimləmədən istifadə

# num = 123456
# print(str(num)[::-1])

# Simli dilimləmə konsepsiyasından istifadə edərək, simi tərsinə ala bilərsiniz. ::-1 start:stop:addım uyğun gəlir.
#  Addım olaraq -1-i keçəndə başlanğıc nöqtəsi sona gedir və öndə dayanır.


def reverse_a_numner(n):
    x = reversed(str(n))
    for i in x:
        print(i, end="")
    print()    

num = int(input())
reverse_a_numner(num)    



def reverse_a_numner(n):
    x = reversed(n)
    for i in x:
        print(i, end="")
    print()    

num = input()
reverse_a_numner(num)





# 16. Python Program to Compute the Power of a Number

# Nömrənin gücünü hesablamaq üçün Python proqramı
# Bu nümunədə bir ədədin gücünü hesablamağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python pow()
# Döngü üçün Python
# Python while Loop


# Misal 1: Bir müddət dövrəsindən istifadə edərək ədədin gücünü hesablayın
# əsas = 3
# eksponent = 4


def Calculate_power_of_a_number(n, z):
    return n**z

num = int(input())
power = int(input())
print(Calculate_power_of_a_number(num, power))



def Calculate_power_of_number(n, z):
    i = 0
    y = 1
    while i < z:
        y *= n
        i +=1
    return y

num = int(input())
power = int(input())
print(Calculate_power_of_number(num, power))
           


# base = 3
# exponent = 4

# result = 1

# while exponent != 0:
#     result *= base
#     exponent-=1

# print("Answer = " + str(result))


# Bu proqramda baza və eksponentə müvafiq olaraq 3 və 4 qiymətləri təyin edilir.
# while döngəsindən istifadə edərək, eksponent sıfır olana qədər nəticəni bazaya vurmağa davam edirik.
# Bu halda nəticəni cəmi 4 dəfə bazaya vururuq, nəticə = 1 * 3 * 3 * 3 * 3 = 81.



# Misal 2: For döngəsindən istifadə edərək ədədin gücünü hesablayın
# əsas = 3
# eksponent = 4


# def Calculate_power_of_a_number(n, z):
#     y = 1
#     for i in range(z):
#         y *= n
#     return y    

# num = int(input("enter number"))
# power = int(input("enter power"))
# print(Calculate_power_of_a_number(num, power))



# base = 3
# exponent = 4

# result = 1

# for exponent in range(exponent, 0, -1):
#     result *= base

# print("Answer = " + str(result))


# Burada while loopundan istifadə etmək əvəzinə biz for loopundan istifadə etdik.
# Hər iterasiyadan sonra eksponent 1 azalır və nəticə əsas göstəriciyə dəfələrlə vurulur.


# ?????????????????????? Mənfi eksponentiniz varsa yuxarıdakı hər iki proqram işləmir.??????????????/?/
# ?????????????? Bunun üçün Python kitabxanasındapow() funksiyasından istifadə etməlisiniz.????????????????????




# Misal 3: pow() funksiyasından istifadə edərək ədədin gücünü hesablayın
# əsas = 3
# eksponent = -4


#### ??????????????????????????????????????????????????????????? #####

###   pow()    funksiyasin kecmemisik



# def calculate_power_of_a_number(value, power):
#     return pow(value, power)

# num = int(input("enter number:"))
# power = int(input("enter power:"))
# print(calculate_power_of_a_number(num, power))



# base = 81
# exponent = -2

# result = pow(base, exponent)

# print("Answer = " + str(result))


# pow() iki arqument qəbul edir: əsas və eksponent. Yuxarıdakı misalda -4-ə yüksəldilmiş 3 pow() istifadə edərək
# hesablanır.


# def power_of_number(n,z):
#     return n**z                 #  menfi eded verende niye duz vermir?????????????

# num = int(input())
# power = int(input())

# print(power_of_number(num, power))









































































































































