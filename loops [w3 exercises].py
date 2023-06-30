#                         Python conditional statements and loops [44 exercises with solution]


# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and
#  2700 (both included)

# 1. 7-ə bölünən və 5-ə çoxlu, 1500 ilə 2700 arasında olan ədədləri tapmaq üçün Python proqramı yazın
#  (hər ikisi daxildir)


def divisible_by_7_multiple_of_5():
    list_1 = []
    for i in range(1500, 2700+1):
        if not i % 5 and not i % 7:
            list_1.append(str(i))
    return ", ".join(list_1)        
            
print(divisible_by_7_multiple_of_5())


nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))



# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# 2. Temperaturları selsi, fahrenheit və selsiyə çevirmək üçün Python proqramı yazın. Redaktora gedin
# [ Formula : c/5 = f-32/9 [ burada c = selsidə temperatur və f = farenheitdə temperatur ]
# Gözlənilən Nəticə:
# 60°C Farenheitdə 140 dərəcədir
# 45°F, Selsi üzrə 7 dərəcədir
# f = 140
# c = ((f-32)/9)*5
# print(c)

c = 60
f = ((9*c) / 5) + 32
print(f)

def Prog(temp):
    try:
        degree = int(temp[:-1])
    except ValueError:
        return "enter number"    
    celsius_or_fahrenheit = temp[-1]

    if celsius_or_fahrenheit.upper() == "F":
        result_celsium  = ((degree-32)/9)*5
        return f"{result_celsium} C"
    elif celsius_or_fahrenheit.upper() == "C":
        result_fahrenheit = ((9*degree) / 5) + 32
        return f"{result_fahrenheit} F"
    else:
        return "error input: enter C or F after number"


temp = (input())
print(Prog(temp))



temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")




# 3. Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until
# the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# 3. 1-dən 9-a qədər rəqəm tapmaq üçün Python proqramı yazın. Redaktora keçin
# Qeyd: İstifadəçidən təxmin daxil etmək təklif olunur. İstifadəçi səhv təxmin edərsə, təxmin doğru olana
# qədər sorğu yenidən görünür, uğurlu təxmində istifadəçi "Yaxşı təxmin etdin!" mesajı göndərin və proqram çıxacaq.

def enter_guess(n):
    if n < 1 or n > 9:
        num = int(input("Please, enter guess number beetween 1 to 9:"))
        return enter_guess(num)
    elif n == 3:
        return "well guessed!    / if you will stop program enter: exit /"
    else:
        num = int(input("You guessed wrong, please enter again:"))
        return enter_guess(num)

# while(True):
#     num = input("enter guess number beetween 1 to 9:") # "5a"
#     if num != "exit":
#         try:
#             num = int(num)
#             print(enter_guess(num))
#         except ValueError:
#             print("Please enter number")
#     else:
#         break
#         finally:
# print(enter_guess(num))

    


try:
    num = int(input("enter guess number beetween 1 to 9:"))
    # print(enter_guess(num))
except ValueError:
    print("Please enter number")
finally:    
    num = int(input("enter guess number beetween 1 to 9:"))
    print(enter_guess(num))    


import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')



# 4. Write a Python program to construct the following pattern, using a nested for loop.

# 4. İç içə for döngəsindən istifadə edərək aşağıdakı nümunəni qurmaq üçün Python proqramını yazın.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()    
    for i in range(n-1, 0, -1): 
        for j in range(i):
            print("* ", end="")
        print()    
           
num = 5
pattern(num)


def pattern(n):
    for i in range(n):
        print("* " * (i+1))
    for i in range(n-1, 0, -1):
        print("* " * i)    
                
num = 5
pattern(num)



n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	

# 5. Write a Python program that accepts a word from the user and reverse it

# 5. İstifadəçidən sözü qəbul edən Python proqramı yazın və onu tərsinə çevirin


class Reverse_word:
    
    def __init__(self, name, word):
        self.name = name
        self.word = word

    def __str__(self):
        return self.name

    def reverse_word(self):
        return self.word[::-1]

    def reverse_word_for(self):
        str = ""
        for i in range(len(self.word)-1, -1, -1):
            # print(i)
            str += self.word[i]
        return str            

word_1 = input()
word_1 = Reverse_word(f"{word_1}_word", word_1)


# print(word_1.reverse_word())
print(word_1.reverse_word_for())


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")



# 6. Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# 6. Bir sıra ədədlərdən cüt və tək ədədlərin sayını hesablamaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə nömrələr: ədədlər = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Gözlənilən Nəticə:
# Cüt ədədlərin sayı: 5
# Tək ədədlərin sayı: 4


def count_odd_even_number(numbers):
    even_count = 0
    odd_count = 0
    for i in numbers:
        if not i % 2:
            even_count +=1
        else:
            odd_count += 1    
    return f"Number of even numbers : {even_count}\nNumber of odd numbers : {odd_count}"



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(count_odd_even_number(numbers))



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even+=1
    else:
    	count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)




# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# Click me to see the sample solution

# 7. Aşağıdakı siyahıdan hər bir elementi və onun uyğun növünü çap edən Python proqramını yazın.
# Nümunə Siyahısı : datalist = [1452, 11.23, 1+2j, Doğrudur, 'w3resource', (0, -1), [5, 12], {"sinif":'V', "bölmə":'A'} ]
# Nümunə həllini görmək üçün mənə klikləyin

def type_(data):
    for i in data:
        print(f"{i} : {type(i)}")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]        
type_(datalist)

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
   


# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
# Click me to see the sample solution

# 8. 3 və 6-dan başqa 0-dan 6-ya kimi bütün rəqəmləri çap edən Python proqramı yazın.
# Qeyd: "Davam et" ifadəsindən istifadə edin.
# Gözlənilən Nəticə : 0 1 2 4 5
# Nümunə həllini görmək üçün mənə klikləyin

def prints_all_the_numbers_from_0_to_6_except_3_an_6():
    for i in range(6+1):
        if i==3 or i==6:
            continue
        print(i, end=" ")
    print()

prints_all_the_numbers_from_0_to_6_except_3_an_6()

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")
	

# 9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34


# 9. Fibonacci seriyasını 0-dan 50-yə qədər əldə etmək üçün Python proqramı yazın. Redaktora keçin.
# Qeyd: Fibonaççi ardıcıllığı rəqəmlər seriyasıdır:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Hər növbəti nömrə özündən əvvəlki iki ədədi toplamaqla tapılır.
# Gözlənilən nəticə : 1 1 2 3 5 8 13 21 34


def fib(n):
    n1 = 0
    n2 = 1
    str_ = ""
    while True:
        str_ += str(n2) + ","
        # print(n2, end=" ")
        n1, n2 = n2 , n1+n2
        if n2 >= n:
            break
    # print()
    return str_ [:-1]   

num = int(input())
print(fib(num))




x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y
	



# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead
#  of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and
#  five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
# Click me to see the sample solution


# 10. 1-dən 50-yə qədər tam ədədləri təkrarlayan Python proqramı yazın. Üçə çarpanlar üçün ədədin yerinə "Fizz"
#  və beşin qatları üçün "Buzz" yazın. Həm üç, həm də beşin qatları olan nömrələr üçün "FizzBuzz" yazın.
# Nümunə çıxışı:
# fizzbuzz
# 1
# 2
# fizz
# 4
# vızıltı
# Nümunə həllini görmək üçün mənə klikləyin


def fizzbuzz():
    for i in range(1,51):
        if not i % 3 and not i % 5:
            print("fizzbuzz")
        elif not i % 3:
            print("fizz")
        elif not i % 5:
            print("buzz")
        else:
            print(i)    

fizzbuzz()



for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	








x = "Fatime"
y = 3
print(x)

if y == 2:
    print(x[0:])
else:
    print(x[4])        




for i in x[0:5]:
    print(i)




# 11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
# Click me to see the sample solution


# 11. Giriş kimi iki rəqəm m (sətir) və n (sütun) götürən və iki ölçülü massiv yaradan Python proqramı yazın. Massivin i-ci sətir və j-ci sütunundakı element dəyəri i*j olmalıdır. Redaktora gedin
# Qeyd :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Məlumatı : Satır = 3, Sütunlar = 4
# Gözlənilən Nəticə : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
# Nümunə həllini görmək üçün mənə klikləyin



row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)




# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case). Go to the editor
# Click me to see the sample solution



# 12. Sətirlər ardıcıllığını (xitam vermək üçün boş sətir) giriş kimi qəbul edən və sətirləri çıxış kimi çap edən (bütün simvollar kiçik hərflərlə) Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin




def upper():
    lines = []
    while True:
        l = input()
        if l:
            lines.append(l.upper())
        else:
            break

    for l in lines:
        print(l)


upper()



# 13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010


# 13. Vergüllə ayrılmış 4 rəqəmli ikili ədədlər ardıcıllığını giriş kimi qəbul edən Python proqramını yazın. Proqram 5-ə bölünən rəqəmləri vergüllə ayrılmış ardıcıllıqla çap edəcək. Redaktora gedin
# Nümunə Məlumat: 0100,0011,1010,1001,1100,1001
# Gözlənilən nəticə: 1010


items = []
num = [x for x in input().split(',')]
print(num)
for p in num:
    x = int(p, 2)
    print(x)
    if not x%5:
        items.append(p)
print(','.join(items))

print(1100/5)



# 14. Write a Python program that accepts a string and calculates the number of digits and letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

# 14. Simli qəbul edən və rəqəm və hərflərin sayını hesablayan Python proqramı yazın. Redaktora gedin
# Nümunə Məlumat: Python 3.2
# Gözlənilən Nəticə:
# Məktublar 6
# Rəqəmlər 2


def let_num_dig_num(string_):
    let_num = dig_num = 0
    for i in string_:
        if i.isalpha():
            let_num +=1
        elif i.isdigit():
            dig_num +=1
    return f"Letters {let_num}\nDigits {dig_num}"        

    
sample_data = "Python 3.2"
print(let_num_dig_num(sample_data))



# 15. Write a Python program to check the validity of passwords input by users. Go to the editor
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Click me to see the sample solution


# 15. İstifadəçilər tərəfindən daxil edilən parolların etibarlılığını yoxlamaq üçün Python proqramı yazın. Redaktora gedin
# Doğrulama:

# [a-z] arasında ən azı 1 hərf və [A-Z] arasında 1 hərf.
# [0-9] arasında ən azı 1 ədəd.
# [$#@] simvolundan ən azı 1 simvol.
# Minimum uzunluq 6 simvol.
# Maksimum uzunluq 16 simvol.
# Nümunə həllini görmək üçün mənə klikləyin



def check_password(password):
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha_lower.upper()
    numbers = "0123456789"
    characters = "$#@"
    alpha_lower_check = False
    alpha_upper_check = False
    num_check = False
    char_check = False
    max_len_check = False
    min_len_check = False
    
    for i in password:
        if i in alpha_lower:
            alpha_lower_check = True
        if i in alpha_upper:
            alpha_upper_check = True
        if i in numbers:
            num_check =True
        if i in characters:
            char_check = True
        if len(password) <= 16:
            max_len_check = True
        if len(password) >= 6:
            min_len_check = True
            
    if alpha_lower_check == False:
        return "At least 1 letter between [a-z]"
    if  alpha_upper_check == False:
        return "At least 1 letter between[A-Z]"
    if  num_check == False:
        return "At least 1 number between [0-9]"
    if char_check == False:
        return "At least 1 character from [$#@]"
    if  max_len_check == False:
        return "Maximum length 16 characters"  
    if min_len_check == False:
        return "Minimum lenght 6 characters"
    if alpha_lower and alpha_upper_check and num_check and char_check and max_len_check and min_len_check:
        return "User Created"

user_password = "aW01$$"
print(check_password(user_password))




import re
p= input("Input your password:")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")


# import re

# def check_password(password):
#     if re.search("[A-Z]", password):
        



import re
def check_password(password_):
    if (re.search("[0-9]", password_) and re.search("[a-z]", password_) and len(password_)>5):
        return True, "valid password"
    else:
        return False, "not valid password"  


user_password =""
print(check_password(user_password))      







# if a in alpha_lower:
#     print("yes")

# def check_password():
#     a = "salamalsqwdwdjhwquhd"
#     alpha_lower = "abcdefghijklmnopqrstuvwxyz"
#     for i in a:
#         if i in alpha_lower:
#             return("yes")

# print(check_password())



# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is
# an even number. The numbers obtained should be printed in a comma-separated sequence. Go to the editor
# Click me to see the sample solution


# 16. Ədədin hər bir rəqəminin cüt ədəd olduğu 100 ilə 400 (hər ikisi daxildir) arasındakı ədədləri tapmaq üçün 
# Python proqramı yazın. Alınan nömrələr vergüllə ayrılmış ardıcıllıqla çap edilməlidir. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin



def check_even_num(x, y):
    list1  = []
    for i in range(x, y+1):
        s = str(i)
        for j in range(len(s)):
            if int(s[j]) % 2:
                break
        else:
            list1.append(s)
    print(','.join(list1))    
            



num1 = 100
num2 = 400

check_even_num(num1, num2)



def check_even_num(x, y):
    list1 = []
    while x < y+1:
        s = str(x)
        j = 0
        while j < len(s):
            if int(s[j]) % 2:
                break
            j += 1
        else:
            list1.append(s)
        x += 1     
    print(','.join(list1))
           



num1 = 100
num2 = 400

check_even_num(num1, num2)



# 5. İki int tipli a və b dəyişəni götürün. a və b aralığında mükəmməl ədədləri çapa verin.
# (Bütün bölənlərinin cəminə bərabər olan ədəd mükəmməl ədəddir. Məs: 6 = 1+2+3
# və s.)

def perfect_num(a, b):
    list1 = []
    for i in range(a, b+1):
        c = 0
        for j in range(1, i):
            if not i % j:
                c += j
                
        
        if i == c:
            list1.append(str(i))
    print(",".join(list1))           



a = int(input())
b = int(input())
perfect_num(a, b)            


def perfect_num(a, b):
    list1 = []
    while a <= b:
        x = 1
        c = 0
        while x < a:
            if not a % x:
                c += x
            x +=1
        if a == c:
            list1.append(str(a))
        a += 1
    print(", ".join(list1))    

num1 = int(input())
num2 = int(input())

perfect_num(num1, num2)


from collections import deque

list1 = deque([1, 2, 3, 4, 5], maxlen=5)
list1.append(6)
list1.append(9)
list1.pop()
print(list1)


# 17. Write a Python program to print the alphabet pattern 'A'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *

# 17. 'A' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:

def alphabet_A():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if row == 0 and column == 0:
                result_str += " "
            if row == 0  and column < 3:
                result_str += "*"
            if (row != 0 and row != 3) and(column > 1 and column < 5):
                result_str += " "    
            if (row != 0 and row != 3) and(column < 1 or column>5):
                result_str += "*"   
            if row == 3 and column < 5:
                result_str += "*"       
        result_str += "\n"        

    return result_str

print(alphabet_A())

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)


# 18. Write a Python program to print the alphabet pattern 'D'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 

# 18. 'D' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:
    
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if ((row == 0 or row == 6) and column < 4):
            result_str += "*"
        if (row != 0 and row != 6) and column > 1 and column < 5:
            result_str += " "
        if row !=0 and row != 6 and (column < 1 or column > 5):
            result_str += "*"
            
    result_str += "\n"        

print(result_str)



result_str=""  
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):  
            result_str +="*"    
        else:      
            result_str += " "    
    result_str += "\n"    
print(result_str)


# 19. Write a Python program to print the alphabet pattern 'E'. Go to the editor
# Expected Output:

#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *
#  *****

# 19. 'E' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:

#  *****
#  *
#  *
#  ****
#  *
#  *
#  *****


def alphbet_E():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((row == 0 or row == 6) and (column > 0 and column < 6)) or (row == 3 and column > 0 and column < 5) or (row != 0 and row != 6 and column > 0 and column < 2):
                result_str += "*"
            else:
                result_str +=" "    
        result_str += "\n"
    return result_str    

print(alphbet_E())


result_str=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)



# 20. Write a Python program to print the alphabet pattern 'G'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

# 20. 'G' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:


def alphabet_G():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((row == 0 or row == 6) and (column > 1 and column < 5)) or ((row != 0 and row != 6 ) and (column == 1)) or ((row != 0 and row != 6 and row != 2) and (column == 5)) or (row == 3 and (column == 4 or column == 3)):
                result_str += "*"
            else:
                result_str += " "    
        result_str += "\n"        

    return result_str

print(alphabet_G())



result_str=""  
for row in range(0,7):    
    for column in range(0,7):     
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)





# 21. Write a Python program to print the alphabet pattern 'L'. Go to the editor
# Expected Output:

#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****

# 21. 'L' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:

#  *
#  *
#  *
#  *
#  *
#  *
#  *****


def alphabet_L():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (row == 6 and column != 0 and column != 6 ) or (row != 6  and column == 1):
                result_str += "*"
            else:
                result_str += " "

        result_str += "\n"    

    return result_str        

print(alphabet_L())


result_str=""
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)



# 22. Write a Python program to print the alphabet pattern 'M'. Go to the editor
# Expected Output:

#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *
# Click me to see the sample solution


# 22. 'M' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:


def alphabet_M():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or column == 5 ) or (row == 2 and (column == 2 or column == 4 )) or (row == 3 and column == 3):
                result_str += "* "
            else:
                result_str += "  "    
        result_str += "\n"
            
    return result_str

print(alphabet_M())




result_str="" 
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            result_str=result_str+"* "    
        else:      
            result_str=result_str+"  "    
    result_str=result_str+"\n"    
print(result_str)



a = 0000
print(list(str(a)))



# 23. Write a Python program to print the alphabet pattern 'O'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

# 23. 'O' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:


def alphabet_O():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if ((row != 0 and row != 6)  and (column == 1 or column == 5)) or ((row == 0 or row == 6) and (column > 1 and column < 5)):
                result_str += "*"
            else:
                result_str += " "    
        result_str += "\n"        

    return result_str        


print(alphabet_O())



result_str=""   
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)




# 24. Write a Python program to print the alphabet pattern 'P'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *  

# 24. 'P' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:



def alphabet_P():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if ((column > 0 and column < 5) and (row == 0 or row == 3)) or ((row != 0 and row != 3) and (column ==1)) or ((row == 1 or row == 2) and column == 5):
                result_str += "*"
            else:
                result_str += " "      
        result_str += "\n"
    return result_str

print(alphabet_P())


result_str=""  
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)




# 25. Write a Python program to print the alphabet pattern 'R'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *



# 25. 'R' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:



def alphabet_R():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if (((row == 0 or row == 3) and (column > 0 and column < 5)) or ((row == 1 or row == 2) and (column == 5 or column == 1)) 
                or (row == 4 and (column == 3 or column == 1)) or (row == 5 and (column == 4 or column == 1)) or 
                (row == 6 and (column == 5 or column == 1)))  :
                result_str += "*"
            else:
                result_str += " "    
        result_str += "\n"

    return result_str

print(alphabet_R())



result_str=""   
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)




# 26. Write a Python program to print the following patterns. Go to the editor
# Expected Output:

#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 
 
#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 



# 26. Aşağıdakı nümunələri çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən nəticə:


def alphabet_S():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if ( ((row == 0) and (column > 1 and column < 6)) or (row == 3 and (column > 1 and column < 5)) or 
            (row == 6 and (column > 0 and column < 5)) or ((row == 1 or row == 2) and column == 1) or 
            ((row == 4 or row == 5) and column == 5) ):
                result_str += "*"
            else:
                result_str += " "    
        result_str += "\n"        

    return result_str

print(alphabet_S())


result_str=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)


#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo


def alphabet_S():
    result_str = ""
    for row in range(15):
        for column in range(17):
            if ( (((row == 3 or row == 4 or row == 5) and column < 4) or 
            ((row == 9 or row ==10 or row == 11) and column > 12)) or
            (row != 3 and row != 4 and row != 5 and row != 9 and row != 10 and row != 11) ):
                result_str += "o"
            else:
                result_str += " "
        result_str += "\n"            

    return result_str

print(alphabet_S())




row=15    
col=18   
result_str=""    
for i in range(1,row+1):    
    if((i<=3)or(i>=7 and i<=9)or(i>=13 and i<=15)):    
        for j in range(1,col):    
            result_str=result_str+"o"    
        result_str=result_str+"\n"    
    elif(i>=4 and i<=6):    
        for j in range(1,5):    
            result_str=result_str+"o"    
        result_str=result_str+"\n"    
    else:    
        for j in range(1,14):    
            result_str=result_str+" "    
        for j in range(1,5):    
            result_str=result_str+"o"    
        result_str=result_str+"\n"    
print(result_str)





str = "idrak mp3; vahid mp4; sadiq mp5"

def design(t):
    if ";" in t:
        t = t.replace(";", "\n")
    return t 

print(design(str))   





# 27. Write a Python program to print the alphabet pattern 'T'. Go to the editor
# Expected Output:
#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *  
# Click me to see the sample solution

# 27. 'T' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin


def alphabet_T():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if (row == 0 and (column > 0 and column < 6)) or (row != 0 and column == 3):
                result_str += "*"
            else:
                result_str += " "
        result_str += "\n"            
    return result_str            

print(alphabet_T())        

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 3 or (row == 0 and column > 0 and column <6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);




# 28. Write a Python program to print the alphabet pattern 'U'. Go to the editor
# Expected Output:

#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 


# 28. 'U' əlifba modelini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:


def alphabet_U():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if (row == 6 and (column > 1 and column < 5)) or ((row != 6) and (column == 1 or column == 5 )):
                result_str += "*"
            else:
                result_str += " "    
        result_str += "\n"    
    return result_str        

print(alphabet_U())

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);




# 29. Write a Python program to print the alphabet pattern 'X'. Go to the editor
# Expected Output:

#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *
# Click me to see the sample solution


def alphabet_X():
    result_str = ""
    for row in range(7):
        for column in range(7):
            if ((row < 2 or row > 4) and (column == 1 or column == 5)) or ((row == 2 or row == 4) and (column ==2 or column == 4)) or (row == 3 and column == 3):
                result_str += "*"
            else:
                result_str += " "    
        result_str += "\n"        
    return result_str

print(alphabet_X())


result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row == 4) or (column == 4 and row == 2)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);




# 30. Write a Python program to print the alphabet pattern 'Z'. Go to the editor
# Expected Output:

# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******

# 30. 'Z' əlifba nümunəsini çap etmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:


def alphabet_Z():
    result_str = ""
    for row in range(7):
        for column in range(7, 0, -1):
            if (row == 0 or row ==6) or (row == column-1):
                result_str += "*"
            else:
                result_str += " "

        result_str += "\n"

    return result_str        

print(alphabet_Z())



result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);



# 31. Write a Python program to calculate a dog's age in dog years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73


# 31. İt illərində itin yaşını hesablamaq üçün Python proqramı yazın. Redaktora gedin
# Qeyd: İlk iki ildə bir it ili 10,5 insan ilinə bərabərdir. Bundan sonra hər it ili 4 insan ilinə bərabərdir.
# Gözlənilən Nəticə:

# İnsan illərində itin yaşını daxil edin: 15
# İt illərində itin yaşı 73-dür


def dog_age(age):
    if age == "string":
        result = "Age must be number"
    elif age < 0:
        result = "Age must be postive number"
    elif age <= 2:
        result = age*10.5
    else:
        result =  2*10.5 + (age-2)*4  

    return result
        
try:
    d_age = int(input())
except ValueError:
    d_age = "string"

print(dog_age(d_age))


h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
	print("Age must be positive number.")
	exit()
elif h_age <= 2:
	d_age = h_age * 10.5
else:
	d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)



# 32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.


# 32. Əlifbanın sait və ya samit olduğunu yoxlamaq üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:

def check_letter(let):
    consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowel = ["a",'e','i','o',"u"]
    if let.lower() in vowel: 
        return f'{let} is vowel'
    elif let.lower() in consonant:
        return f'{let} is consonant'
    else:
        return "Please enter letter"

x = input()
print(check_letter(x))


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
	



# 33. Write a Python program to convert a month name to a number of days. Go to the editor
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 


# 33. Ay adını bir neçə günə çevirmək üçün Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:

# Ayların siyahısı: yanvar, fevral, mart, aprel, may, iyun, iyul, avqust
# , sentyabr, oktyabr, noyabr, dekabr
# Ayın adını daxil edin: Fevral
# Günlərin sayı: 28/29 gün

def num_day_of_month(mon):
    if mon.capitalize() in ["January", "March", "May", "July", "August", "October", "December"]:
        return "%s" % ("No. of days: 31 days")
    elif mon.capitalize() in ["April", "June", "September", "November"]:
        return "{}".format('No. of days: 30 days')
    elif mon.capitalize() in ["February"]:
        return f'No. of days: 28 days'
    else:
        return "{0}".format("Wrong month name")

month = input()
print(num_day_of_month(month))    

    

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 
	


# 34. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20

# 34. İki tam ədədi cəmləmək üçün Python proqramı yazın. Lakin, cəmi 15 ilə 20 arasında olarsa, 20-ni qaytaracaq


def sum_integers(int_1, int_2):
    sum_ints = int_1 + int_2
    if sum_ints in range(15, 20):
        return 20
    else:
        return sum_ints
    
num_1 = int(input())
num_2 = int(input())
print(sum_integers(num_1, num_2))


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))



# 35. Write a Python program that checks whether a string represents an integer or not. Go to the editor
# Expected Output:

# Input a string: Python                                                  
# The string is not an integer.

# 35. Sətin tam ədədi təmsil edib-etmədiyini yoxlayan Python proqramı yazın. Redaktora gedin
# Gözlənilən Nəticə:

# Sətir daxil edin: Python
# Sətir tam ədəd deyil.


def check_string(str_):
    if type(str_) != int:
        return '{}'.format('The string is not an integer')
    else:
        return '%s' % ('The string is an integer')

try: 
    string = int(input())
except ValueError:
    string = "string"    
print(check_string(string))    




text = input("Input a string: ")
text = text.strip()
if len(text) < 1:
    print("Input a valid text")
else:
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")
    elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         print("The string is an integer.")
    else:
        print("The string is not an integer.") 
		


x = "sal1ram"
y = "sawfwefwfelwefwf1ramqdwedwe"

if all(i in y for i in x):
    print(1) 



def check_string(str_):
    if str_.strip(" +- ").isnumeric():
        return f'The string is an integer'
    else:
        return f'The string is not an integer'
    
string = input()
print(check_string(string))    



x = {2:{"a": 2}, 3:{"b": "salam"}}

for valu in x:
    print(valu)


def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)
        print(mid, 'mid', end=',')
        guess = list[mid]
        print(guess, 'guess', end=',')
        if guess == item:
            return mid, "result"
        if guess > item:
            high = mid-1
            print(high, 'high', end=',')
        else:
            low = mid + 1
            print(low, 'low', end=',')
    return None
    # return list.index(item)

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1))        



def binary_search(guess):
    low = 1-1
    high = 100+1
    mid = (low + high) // 2
    count = 0

    while True:
        print(mid, low, high) 
        count += 1
        if mid == guess:
            
            return f'guess={mid}, try={count}' 
        if mid > guess:
            low = low
            high = mid
            mid = low + ((high - low) // 2)
        else:
            low = mid
            high = high
            mid = low + ((high - low) // 2)
           
           
guess = 61
print(binary_search(guess))






def alphabet_X():
    result_str = ""
    for raw in range(7):
        for column in range(7):
            if raw == column or raw == 6 - column:
                result_str += "*"
            else:
                result_str += " "    

        result_str += "\n"        
                    
    return result_str

print(alphabet_X())



# 36. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle  
# Click me to see the sample solution

# 36. Üçbucağın bərabərtərəfli, ikitərəfli və ya miqyaslı olduğunu yoxlamaq üçün Python proqramı yazın.
# Qeyd :
# Bərabər üçbucaq, hər üç tərəfinin bərabər olduğu üçbucaqdır.
# Skalen üçbucağı üç qeyri-bərabər tərəfi olan üçbucaqdır.
# İkitərəfli üçbucaq (ən azı) iki bərabər tərəfi olan üçbucaqdır.
# Gözlənilən Nəticə:

# Üçbucağın tərəflərinin giriş uzunluqları:
# x: 6
# y: 8
# z: 12
# Skalen üçbucağı
# Nümunə həllini görmək üçün mənə klikləyin


def check_triangle(a, b, c):
    if a is None:
        return('ok')
    if a == b == c:
        return (f'equilateral triangle')
    elif a != b and a != c and b != c:
        return (f"scalene triangle")
    else:
        return (f'isosceles triangle')



try:
    x = int(input())
    y = int(input())
    z = int(input())
    print(check_triangle(x, y, z))
except (ValueError):
    print('enter number')
      



print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")




# 37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
# Expected Output:

# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn  


# 37. Ay və günü təmsil edən iki tam ədədi oxuyan və həmin ay və gün üçün mövsümü çap edən Python proqramı yazın.
# Gözlənilən Nəticə:

# Ayı daxil edin (məsələn, yanvar, fevral və s.): iyul
# Gün daxil edin: 31
# Mövsüm payızdır

def check_season():
	spring = ('March', 'April', 'May', 'June')
	summer = ('June', 'Jule', "August", "September")
	autumn = ('Septmber','October', 'November', "December")
	winter = ('December', "January", "Febrary", "March")



import datetime

x = datetime.date





from datetime import date
 

def get_season(date):
  m = date.month
  x = m%12 // 3 + 1
  if x == 1:
    season = print("Winter")
  if x == 2:
    season = print("Spring")
  if x == 3:
    season = print("Summer")
  if x == 4:
    season = print("Autumn")
  return season
 
year = int(input())
month = int(input())
day = int(input())
x = get_season(date(year,month,day))
print(x, "-->", get_season(x))



#import required modules and packages
import datetime
from datetime import date
 
#defining function
def get_season(date):
  m = date.month
  d = date.day
  if 0 < m < 3 or (m == 12 and d > 20) or (m == 3 and d <= 20) :
    season = "Winter"
  elif 3 < m < 6 or (m == 3 and d > 20) or (m == 6 and d <= 20):
    season = "Spring"
  elif 6 < m < 9 or (m == 6 and d > 20) or (m == 9 and d <= 20):
    season = "Summer"
  elif 9 < m < 12 or (m == 9 and d > 20) or (m == 12 and d <= 20)  :
    season = "Autumn"
  return season


year = 2020
try:
  month = (input())
  from time import strptime
  month = strptime(month,'%B').tm_mon
  day = int(input())
  print(get_season(date(year, month, day)))
except ValueError:
  month = int(input())
  day1 = day

  



 




