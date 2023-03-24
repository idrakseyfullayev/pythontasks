#                         Python conditional statements and loops [44 exercises with solution]


# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and
#  2700 (both included)

# 1. 7-ə bölünən və 5-ə çoxlu, 1500 ilə 2700 arasında olan ədədləri tapmaq üçün Python proqramı yazın
#  (hər ikisi daxildir)


# def divisible_by_7_multiple_of_5():
#     list_1 = []
#     for i in range(1500, 2700+1):
#         if not i % 5 and not i % 7:
#             list_1.append(str(i))
#     return ", ".join(list_1)        
            
# print(divisible_by_7_multiple_of_5())


# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))



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

# c = 60
# f = ((9*c) / 5) + 32
# print(f)

# def Prog(temp):
#     try:
#         degree = int(temp[:-1])
#     except ValueError:
#         return "enter number"    
#     celsius_or_fahrenheit = temp[-1]

#     if celsius_or_fahrenheit.upper() == "F":
#         result_celsium  = ((degree-32)/9)*5
#         return f"{result_celsium} C"
#     elif celsius_or_fahrenheit.upper() == "C":
#         result_fahrenheit = ((9*degree) / 5) + 32
#         return f"{result_fahrenheit} F"
#     else:
#         return "error input: enter C or F after number"


# temp = (input())
# print(Prog(temp))



# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]

# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")




# 3. Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until
# the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# 3. 1-dən 9-a qədər rəqəm tapmaq üçün Python proqramı yazın. Redaktora keçin
# Qeyd: İstifadəçidən təxmin daxil etmək təklif olunur. İstifadəçi səhv təxmin edərsə, təxmin doğru olana
# qədər sorğu yenidən görünür, uğurlu təxmində istifadəçi "Yaxşı təxmin etdin!" mesajı göndərin və proqram çıxacaq.

# def enter_guess(n):
#     if n < 1 or n > 9:
#         num = int(input("Please, enter guess number beetween 1 to 9:"))
#         return enter_guess(num)
#     elif n == 3:
#         return "well guessed!    / if you will stop program enter: exit /"
#     else:
#         num = int(input("You guessed wrong, please enter again:"))
#         return enter_guess(num)

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
    # finally:
    #     print(enter_guess(num))

    


# try:
#     num = int(input("enter guess number beetween 1 to 9:"))
#     # print(enter_guess(num))
# except ValueError:
#     print("Please enter number")
# finally:    
#     num = int(input("enter guess number beetween 1 to 9:"))
#     print(enter_guess(num))    


# import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')



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


# def pattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("* ", end="")
#         print()    
#     for i in range(n-1, 0, -1): 
#         for j in range(i):
#             print("* ", end="")
#         print()    
           
# num = 5
# pattern(num)


# def pattern(n):
#     for i in range(n):
#         print("* " * (i+1))
#     for i in range(n-1, 0, -1):
#         print("* " * i)    
                
# num = 5
# pattern(num)



# n=5
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
	

# 5. Write a Python program that accepts a word from the user and reverse it

# 5. İstifadəçidən sözü qəbul edən Python proqramı yazın və onu tərsinə çevirin


# class Reverse_word:
    
#     def __init__(self, name, word):
#         self.name = name
#         self.word = word

#     def __str__(self):
#         return self.name

#     def reverse_word(self):
#         return self.word[::-1]

#     def reverse_word_for(self):
#         str = ""
#         for i in range(len(self.word)-1, -1, -1):
#             # print(i)
#             str += self.word[i]
#         return str            

# word_1 = input()
# word_1 = Reverse_word(f"{word_1}_word", word_1)


# # print(word_1.reverse_word())
# print(word_1.reverse_word_for())


# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")
# print("\n")



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


# def count_odd_even_number(numbers):
#     even_count = 0
#     odd_count = 0
#     for i in numbers:
#         if not i % 2:
#             even_count +=1
#         else:
#             odd_count += 1    
#     return f"Number of even numbers : {even_count}\nNumber of odd numbers : {odd_count}"



# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(count_odd_even_number(numbers))



# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x % 2:
#         count_even+=1
#     else:
#     	count_odd+=1
# print("Number of even numbers :",count_even)
# print("Number of odd numbers :",count_odd)




# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# Click me to see the sample solution

# 7. Aşağıdakı siyahıdan hər bir elementi və onun uyğun növünü çap edən Python proqramını yazın.
# Nümunə Siyahısı : datalist = [1452, 11.23, 1+2j, Doğrudur, 'w3resource', (0, -1), [5, 12], {"sinif":'V', "bölmə":'A'} ]
# Nümunə həllini görmək üçün mənə klikləyin

# def type_(data):
#     for i in data:
#         print(f"{i} : {type(i)}")

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]        
# type_(datalist)

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
# {"class":'V', "section":'A'}]
# for item in datalist:
#    print ("Type of ",item, " is ", type(item))
   


# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
# Click me to see the sample solution

# 8. 3 və 6-dan başqa 0-dan 6-ya kimi bütün rəqəmləri çap edən Python proqramı yazın.
# Qeyd: "Davam et" ifadəsindən istifadə edin.
# Gözlənilən Nəticə : 0 1 2 4 5
# Nümunə həllini görmək üçün mənə klikləyin

# def prints_all_the_numbers_from_0_to_6_except_3_an_6():
#     for i in range(6+1):
#         if i==3 or i==6:
#             continue
#         print(i, end=" ")
#     print()

# prints_all_the_numbers_from_0_to_6_except_3_an_6()

# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')
# print("\n")
	

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


# def fib(n):
#     n1 = 0
#     n2 = 1
#     str_ = ""
#     while True:
#         str_ += str(n2) + ","
#         # print(n2, end=" ")
#         n1, n2 = n2 , n1+n2
#         if n2 >= n:
#             break
#     # print()
#     return str_ [:-1]   

# num = int(input())
# print(fib(num))




# x,y=0,1

# while y<50:
#     print(y)
#     x,y = y,x+y
	



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


# def fizzbuzz():
#     for i in range(1,51):
#         if not i % 3 and not i % 5:
#             print("fizzbuzz")
#         elif not i % 3:
#             print("fizz")
#         elif not i % 5:
#             print("buzz")
#         else:
#             print(i)    

# fizzbuzz()



# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)
	








# x = "Fatime"
# y = 3
# print(x)

# if y == 2:
#     print(x[0:])
# else:
#     print(x[4])        




# for i in x[0:5]:
#     print(i)




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



# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col

# print(multi_list)




# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case). Go to the editor
# Click me to see the sample solution



# 12. Sətirlər ardıcıllığını (xitam vermək üçün boş sətir) giriş kimi qəbul edən və sətirləri çıxış kimi çap edən (bütün simvollar kiçik hərflərlə) Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin




# def upper():
#     lines = []
#     while True:
#         l = input()
#         if l:
#             lines.append(l.upper())
#         else:
#             break

#     for l in lines:
#         print(l)


# upper()



# 13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010


# 13. Vergüllə ayrılmış 4 rəqəmli ikili ədədlər ardıcıllığını giriş kimi qəbul edən Python proqramını yazın. Proqram 5-ə bölünən rəqəmləri vergüllə ayrılmış ardıcıllıqla çap edəcək. Redaktora gedin
# Nümunə Məlumat: 0100,0011,1010,1001,1100,1001
# Gözlənilən nəticə: 1010


# items = []
# num = [x for x in input().split(',')]
# print(num)
# for p in num:
#     x = int(p, 2)
#     print(x)
#     if not x%5:
#         items.append(p)
# print(','.join(items))

# print(1100/5)



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


# def let_num_dig_num(string_):
#     let_num = dig_num = 0
#     for i in string_:
#         if i.isalpha():
#             let_num +=1
#         elif i.isdigit():
#             dig_num +=1
#     return f"Letters {let_num}\nDigits {dig_num}"        

    
# sample_data = "Python 3.2"
# print(let_num_dig_num(sample_data))



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



# def check_password(password):
#     alpha_lower = "abcdefghijklmnopqrstuvwxyz"
#     alpha_upper = alpha_lower.upper()
#     numbers = "0123456789"
#     characters = "$#@"
#     alpha_lower_check = False
#     alpha_upper_check = False
#     num_check = False
#     char_check = False
#     max_len_check = False
#     min_len_check = False
    
#     for i in password:
#         if i in alpha_lower:
#             alpha_lower_check = True
#         if i in alpha_upper:
#             alpha_upper_check = True
#         if i in numbers:
#             num_check =True
#         if i in characters:
#             char_check = True
#         if len(password) <= 16:
#             max_len_check = True
#         if len(password) >= 6:
#             min_len_check = True
            
#     if alpha_lower_check == False:
#         return "At least 1 letter between [a-z]"
#     if  alpha_upper_check == False:
#         return "At least 1 letter between[A-Z]"
#     if  num_check == False:
#         return "At least 1 number between [0-9]"
#     if char_check == False:
#         return "At least 1 character from [$#@]"
#     if  max_len_check == False:
#         return "Maximum length 16 characters"  
#     if min_len_check == False:
#         return "Minimum lenght 6 characters"
#     if alpha_lower and alpha_upper_check and num_check and char_check and max_len_check and min_len_check:
#         return "User Created"

# user_password = "aW01$$"
# print(check_password(user_password))




# import re
# p= input("Input your password:")
# x = True
# while x:  
#     if (len(p)<6 or len(p)>12):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[A-Z]",p):
#         break
#     elif not re.search("[$#@]",p):
#         break
#     elif re.search("\s",p):
#         break
#     else:
#         print("Valid Password")
#         x=False
#         break

# if x:
#     print("Not a Valid Password")


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































