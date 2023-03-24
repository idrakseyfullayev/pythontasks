#                   #  w3resource. Python Exercises, Practice, Solution. List of Python Exercises : #
#                            # Python functions [21 exercises with solution] #


# 1. Write a Python function to find the Max of three numbers. Go to the editor

# 1. Üç ədədin Max tapmaq üçün Python funksiyasını yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin


# def Max_of_three_numbers(n1, n2, n3):
#     if n1 >= n2 and n1 >= n3:
#         return f"The Max of these numbers i {n1}"
#     elif n2 >= n1 and n2 >= n3:
#         return f"The Max of these numers is {n2}"
#     else:
#         return f"The Max of these numbers i {n3}"

# num1 = int(input("enter number_1:"))
# num2 = int(input("enter number_2:"))
# num3 = int(input("enter number_3:"))
# print(Max_of_three_numbers(num1, num2, num3))




# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))



# 2. Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# 2. Siyahıdakı bütün ədədləri cəmləmək üçün Python funksiyasını yazın. Redaktora gedin
# Nümunə Siyahısı: (8, 2, 3, 0, 7)
# Gözlənilən nəticə: 20


# def sum_of_list(*args):
#     x = 0
#     for i in args:
#         x += i
#     return x    

# print(sum_of_list(8,2,3,0,7))



# def sum_of_list(*args):
#     return sum(args)

# print(sum_of_list(8, 2, 3, 0, 7))    



# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))  


# def sum1(numbers):
#     return sum(numbers)

# print(sum1((8, 2, 3, 0, 7)))





# def sum_all_the_numbers(n1, n2, n3, n4, n5):
#     return sum([n1, n2, n3, n4, n5])

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())
# print(sum_all_the_numbers(num1, num2, num3, num4, num5))




# 3. Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# 3. Siyahıdakı bütün ədədləri çoxaltmaq üçün Python funksiyasını yazın. Redaktora gedin
# Nümunə Siyahısı: (8, 2, 3, -1, 7)
# Gözlənilən Nəticə: -336


# def multiply_all_the_numbers(*args):
#     x = 1
#     for i in args:
#         x *= i
#     return x

# print(multiply_all_the_numbers(8, 2, 3, -1 ,7))



# def mutiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total

# print(mutiply((8, 2, 3, -1,7)))      



# 4. Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# 4. Sətri tərsinə çevirmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə sətri: "1234abcd"
# Gözlənilən Nəticə: "dcba4321"


# def to_reverse_a_string(string):
#     return f"Reverse of the {string} is {string[::-1]}"

# word = input("enter the word:")
# print(to_reverse_a_string(word))



# def to_reverse_a_string(string):
#     return string[::-1]

# word = input("enter the word:")
# print(f"Reverse of the {word} is {to_reverse_a_string(word)}")



# def to_reverse_a_string(string):
#     return string[::-1]

# word = input("enter the word:")
# print(f"Reverse of the {word} is {to_reverse_a_string(string=word)}")   # bes bu ne usuldu tesadufen tapdim??? 


# def to_reverse_a_string(string):
#     str1 = ""
#     for i in range(len(string)):
#         str1 += string[len(string)-1-i]
#     return str1

# word = input("enter word:")
# print(to_reverse_a_string(word))



# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))





# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts
#  the number as an argument. Go to the editor

# 5. Ədədin (mənfi olmayan tam ədəd) faktorialını hesablamaq üçün Python funksiyasını yazın. Funksiya rəqəmi 
# arqument kimi qəbul edir. Redaktora gedin


# def  the_factorial_of_a_number(n):
#     x1 = 1
#     for i in range(1, n+1):
#         x1 *= i
#     return x1

# num = int(input())
# print(f"The factorial of {num} is {the_factorial_of_a_number(num)}")



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))




# 6. Write a Python function to check whether a number falls in a given range. Go to the editor

# 6. Ədədin verilmiş diapazona düşdüyünü yoxlamaq üçün Python funksiyasını yazın. Redaktora gedin


# def check_number_given_range(n, x, y):
#     for i in range(x, y+1):
#         if n == i:
#             return f"{n} is in range{x,y}"     # burda niye moterize ozu verir???????
#     else:
#         return f"{n} isn't in range({x}, {y})"

# num = int(input())
# beginning_interval = int(input())
# end_of_interval = int(input())
# print(check_number_given_range(num, beginning_interval, end_of_interval))



# def check_number_given_range(n, x, y):
#     if n in range(x, y):                    # yoxladim if ile de yazmaq olur??????????????
#         print(f"{n} is in range({x}, {y})")
#     else:
#         print(f"{n} isn't in range({x}, {y})")    

# num = int(input())
# x = int(input())
# y = int(input())
# check_number_given_range(num, x, y)




# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)



# def test_range(n, start_num, end_num = 0):
#   return start_num <= n <= end_num if end_num >= start_num else end_num <= n <= start_num
# print(test_range(5, 2, 7))
# print(test_range(5, 7))
# print(test_range(1, 3, 6))
# print(test_range(6, 5))






# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case
#  letters.  Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


# 7. Simli qəbul edən Python funksiyasını yazın və böyük və kiçik hərflərin sayını hesablayın. Redaktora gedin
# Nümunə simli: 'The quick Brow Fox'
# Gözlənilən Nəticə:
# Böyük hərflərin sayı: 3
# Kiçik hərflərin sayı: 12

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
#     print(f"In '{text}' text have {c} upper letter and {t} lower letter")
#     # print(f" No. of Upper case characters : {c}")
#     # print(f" No. of lower case characters : {t}")

# string1 = 'The quick Brown Fox'
# count_upper_lower_letter(string1)



# def count_upper_lower_letter(text):
#     uppers = 0
#     lowers = 0
#     for i in text:
#         if i.isupper():
#             uppers +=1
#         elif i.islower():
#             lowers += 1    
#     print(f" No. of Upper case characters : {uppers}")
#     print(f" No. of Lower case Characters : {lowers}")

# string1 = 'The quick Brown Fox'
# count_upper_lower_letter(string1)




# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The quick Brown Fox')




# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
#  Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


# 8. Siyahı götürən və birinci siyahının unikal elementləri ilə yeni siyahı qaytaran Python funksiyasını yazın.
#  Redaktora gedin
# Nümunə Siyahısı: [1,2,3,3,3,3,4,5]
# Unikal siyahı : [1, 2, 3, 4, 5]


# def list_with_unique_elements(list1):
#     x = set(list1)
#     list1 = list(x)
#     return list1

# print(list_with_unique_elements([1,2,3,3,3,3,4,5]))



# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5])) 





# 9. Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1
#  and itself.

# 9. Bir ədədi parametr kimi qəbul edən Python funksiyasını yazın və ədədin sadə olub olmadığını yoxlayın.
#  Redaktora gedin
# Qeyd: Sadə ədəd (və ya sadə) 1-dən böyük və 1 və özündən başqa müsbət bölənləri olmayan natural ədəddir.


# def check_a_prime_number(n):
#     if n < 1:
#         return "is not a natural number"
#     elif n == 1:
#         return "neither a prime nor a composite number"    
#     for i in range(2, n):
#         if not n % i:
#             return "a composite number"
#     else:
#         return "a prime number"        

# num = int(input())
# print(check_a_prime_number(num))



# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(17))


# anlamadim ??????????????????????????????????????????

# from math import sqrt
# def is_prime(num):
#   if num <= 1 or (num % 2 == 0 and num > 2): 
#     return False
#   return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))
# print(is_prime(11))
# print(is_prime(13))
# print(is_prime(16))
# print(is_prime(17))
# print(is_prime(97))




# 10. Write a Python program to print the even numbers from a given list. Go to the editor
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# 10. Verilmiş siyahıdan cüt ədədləri çap etmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə Siyahısı: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Gözlənilən Nəticə : [2, 4, 6, 8]


# def print_even_numbers_from_list(list1):
#     even_number_list = []
#     for i in list1:
#         if not i % 2:
#             even_number_list.append(i)
#     return even_number_list

# print(print_even_numbers_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))



# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))




# 11. Write a Python function to check whether a number is perfect or not. Go to the editor
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum
#  of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself 
# (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its
#  positive divisors (including itself). Example : The first perfect number is 6, because 1, 2, and 3 are its 
# proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its 
# positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is
#  followed by the perfect numbers 496 and 8128

# 11. Ədədin mükəmməl olub olmadığını yoxlamaq üçün Python funksiyasını yazın. Redaktora gedin
# Vikipediyaya görə: Ədədlər nəzəriyyəsində mükəmməl ədəd onun müvafiq müsbət bölənlərinin cəminə, yəni ədədin
#  özü xaric olan müsbət bölənlərinin cəminə bərabər olan müsbət tam ədəddir (həmçinin onun aliquot cəmi kimi
#  tanınır). Ekvivalent olaraq mükəmməl ədəd bütün müsbət bölənlərinin (özü də daxil olmaqla) cəminin yarısı 
# olan ədəddir. Nümunə : Birinci mükəmməl ədəd 6-dır, çünki 1, 2 və 3 onun müvafiq müsbət bölənləridir
#  və 1 + 2 + 3 = 6. Ekvivalent olaraq, 6 rəqəmi bütün müsbət bölənlərin cəminin yarısına bərabərdir:
#  ( 1 + 2 + 3 + 6 ) / 2 = 6. Növbəti mükəmməl ədəd 28 = 1 + 2 + 4 + 7 + 14-dür. Bunun ardınca 496 və 8128 mükəmməl
#  ədədləri gəlir.


# def check_perfect_number(n):
#     if n <=1:
#         return "isn't a perfect number"
#     x = 0       
#     for i in range(1, n):
#         if not n % i:
#             x += i
#     if n == x:
#         return "is a perfect number"
#     else:
#         return "isn't a perfect number"            

# num = int(input())
# print(check_perfect_number(num))


# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))





# 12. Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or
#  nurses run.

# 12. Keçirilmiş sətirin palindrom olub olmadığını yoxlayan Python funksiyasını yazın. Redaktora gedin
# Qeyd: Palindrom irəli ilə eyni geri oxunan söz, ifadə və ya ardıcıllıqdır, məsələn, xanım və ya tibb bacıları qaçır.


# def check_palindrome_word(word):
#     a = word.split()
#     b = "".join(a)
#     if b == b[::-1]:
#         return "is palidrom word"
#     else:
#         return "isn't palidrom word"    
#     # print()
# word = input("enter_word:")
# print(check_palindrome_word(word))




# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('nurses run')) 




# 13. Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

# Sample Pascal's triangle :

# Pascal's triangle
# Each number is the two numbers above it added together Go to the editor

# 13. Paskal üçbucağının ilk n sətirini çap edən Python funksiyasını yazın. Redaktora gedin
# Qeyd : Paskal üçbucağı ilk dəfə Blez Paskal tərəfindən təsəvvür edilən arifmetik və həndəsi fiqurdur.

# Paskal üçbucağının nümunəsi:

# Paskal üçbucağı
# Hər bir nömrə yuxarıdakı iki rəqəmdir, bir-birinə əlavə olunur. Redaktora gedin


# def pascal_s_triangle(n):
#     # list1 = []
#     matrix = [[1],[1,1]]
#     matrix.append([n])
#     if n == 0 :
#         return matrix[0]
#     elif n == 1:
#         return matrix[1]    
#     else:
#         matrix[n].append(pascal_s_triangle(n-1)[n-2]+pascal_s_triangle(n-1)[n-1])   
#     return matrix
    


# num = int(input())
# print(pascal_s_triangle(num))



# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6) 


 

# 14. Write a Python function to check whether a string is a pangram or not. Go to the editor
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


# 14. Sətin panqram olub-olmadığını yoxlamaq üçün Python funksiyasını yazın. Redaktora gedin
# Qeyd: Panqramlar ən azı bir dəfə əlifbanın hər hərfini ehtiva edən sözlər və ya cümlələrdir.
# Məsələn: "Tez qəhvəyi tülkü tənbəl itin üstündən tullanır"


# def check_pangrams_string(string1):
#     alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     string2 = string1.upper()
#     list1 = string2.split()
#     string3 = "".join(list1)
#     set1 = set(string3)
#     list2 = list(set1)
    
#     list2.sort()
#     # return list2
   
#     string4 = "".join(list2)
#     # return string4
    
#     if string4 == alphabet1:   
#         return "is pangram word"  # burda niye none qaytarir?????????????
# #     # # if  len(string1) == 26:
# #     #     return "is pangram word"
# #     # else:
# #     #     return "isn't pangram word"
# def check_pangrams_string(string1):
#     alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for i in alphabet1:
#         if i not in string1.upper():
#             return "pangram deyil"
#     else:
#         return "pangramdir"

# word = "The quick brown fox jumps over the lazy dog"
# print(check_pangrams_string(word))



### ?????????????????????????????????????
# import string, sys
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
 
# print ( ispangram('The quick brown fox jumps over the lazy dog')) 






# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in
#  a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

# 15. Sözlərin defislə ayrılmış ardıcıllığını giriş kimi qəbul edən və sözləri əlifba sırası ilə sıraladıqdan
# sonra defislə ayrılmış ardıcıllıqla çap edən Python proqramı yazın. Redaktora gedin



# def sorting_alphabetically(string1):
#     list1 = string1.split("-")
#     list1.sort()
#     string2 = "-".join(list1)
#     return string2

# word = "green-red-yellow-black-white"
# print(sorting_alphabetically(word))


# items=[n for n in input().split('-')]   # bunu aydinlasdiraq???????
# print(items)
# items.sort()
# print('-'.join(items))


# 16. Write a Python function to create and print a list where the values are square of numbers
# between 1 and 30 (both included). Go to the editor

# 16. Dəyərlərinin 1 və 30 (hər ikisi daxildir) arasında olan ədədlərin kvadratı olduğu siyahı yaratmaq və 
# çap etmək üçün Python funksiyasını yazın. Redaktora gedin


# def square_of_numbers():
#     x = 1
#     while  True:
#         if x**0.5 == int(x**0.5):
#             print(x)
#         if x**0.5 >= 30:
#             break
#         x += 1  

# square_of_numbers()


# def square_of_numbers():
#     x = 1
#     while  x**0.5 <= 30:
#         if x**0.5 == int(x**0.5):
#             print(x)
#         x += 1    
# square_of_numbers()
    




# def printValues():
# 	l = list()
# 	for i in range(1,31):
# 		l.append(i**2)
# 	print(l)
		
# printValues()







# 17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.
#  Go to the editor

# 17. Python-da funksiya dekoratorları zəncirini (qalın, kursiv, alt xətt və s.) yaratmaq üçün Python proqramı
# yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin
###   ???????????????????????????

# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world"
# print(hello()) ## returns "<b><i><u>hello world</u></i></b>"

###  ??????????????????????????????????




# 18. Write a Python program to execute a string containing Python code. Go to the editor
# Click me to see the sample solution
# 18. Python kodunu ehtiva edən sətri icra etmək üçün Python proqramını yazın. Redaktora gedin


# mycode = 'print("hello world")'
# code = """
# def mutiply(x,y):
#     return x*y

# print('Multiply of 2 and 3 is: ',mutiply(2,3))
# """
# exec(mycode)
# exec(code)




# 19. Write a Python program to access a function inside a function. Go to the editor
# Click me to see the sample solution

# 19. Funksiya daxilində funksiyaya daxil olmaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin


# def test(a):
#     def add(b):
#         nonlocal a
#         a += 1
#         return a+b
#     return add    



# func = test(4)
# print(func(4))



# def test(func,a=4):
#     def add(b=4):
#         nonlocal a
#         a += 1
#         return a+b
#     return add    

# @test
# def test1():
#     return 4
    
# print(test1())



# 20. Write a Python program to detect the number of local variables declared in a function. Go to the editor
# Sample Output:

# 20. Funksiyada elan edilmiş lokal dəyişənlərin sayını aşkar etmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə çıxışı:


# def abc():
#     x = 1
#     y = 2
#     str1= "w3resource"
#     print("Python Exercises")

# print(abc.__code__.co_nlocals)




# 21. Write a Python program that invoke a given function after specific milliseconds. Go to the editor
# Sample Output:
# Square root after specific miliseconds:
# 4.0
# 10.0
# 158.42979517754858

# 21. Müəyyən millisaniyələrdən sonra verilmiş funksiyanı işə salan Python proqramını yazın. Redaktora gedin
# Nümunə çıxışı:
# Xüsusi milisaniyələrdən sonra kvadrat kök:
# 4.0
# 10.0
# 158.42979517754858


# from time import sleep
# import math
# def delay(fn, ms, *args):
#   sleep(ms / 1000)
#   return fn(*args)
# print("Square root after specific miliseconds:") 
# print(delay(lambda x: math.sqrt(x), 100, 16))
# print(delay(lambda x: math.sqrt(x), 1000, 100))
# print(delay(lambda x: math.sqrt(x), 2000, 25100))







































