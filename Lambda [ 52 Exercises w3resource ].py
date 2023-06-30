#                             w3resource.  Python Lambda [ 52 Exercises with Solution ]                     



# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an
#  argument, also create a lambda function that multiplies argument x with argument y and print the result.
#  Go to the editor

# 1. Arqument kimi ötürülən verilmiş ədədə 15 əlavə edən lambda funksiyası yaratmaq üçün Python proqramı yazın, 
# həmçinin x arqumentini y arqumenti ilə çoxaldan lambda funksiyası yaradın və nəticəni çap edin. Redaktora gedin

func_adds_15 = lambda n: n + 15

n = 5
print(func_adds_15(n))


func_multiplies = lambda x, y: x * y

x = int(input("enter number_1:"))
y = int(input("enter number_2:"))
print(func_multiplies(x, y))


r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))



# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied
#  with an unknown given number. Go to the editor
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

# 2. Bir arqument alan funksiya yaratmaq üçün Python proqramı yazın və həmin arqument naməlum verilmiş ədədlə
#  vurulacaq. Redaktora gedin
# Nümunə çıxışı:
# 15 = 30 sayını iki dəfə artırın
# 15 = 45-in sayını üç dəfə artırın
# 15 = 60-ın sayını dörd dəfə artırın
# 15 = 75 rəqəmini beşliyə çatdırın


def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))



# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# 3. Lambda istifadə edərək dəstlərin siyahısını çeşidləmək üçün Python proqramı yazın.
# Tuples orijinal siyahısı:
# [('İngilis dili', 88), ('Elm', 90), ('Riyaziyyat', 97), ('Sosial elmlər', 82)]
# Tuples siyahısının çeşidlənməsi:
# [('Sosial elmlər', 82), ('İngilis dili', 88), ('Elm', 90), ('Riyaziyyat', 97)]



list1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

list1.sort(key=lambda x: x[0])
print(list1)

# ???????????????????????????????????????????????????????????????

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)




# 4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

# 4. Lambda istifadə edərək lüğətlərin siyahısını çeşidləmək üçün Python proqramı yazın. Redaktora gedin
# Lüğətlərin orijinal siyahısı:
# [{'make': 'Nokia', 'model': 216, 'rəng': 'Qara'}, {'make': 'Mi Max', 'model': '2', 'rəng': 'Qızıl' },
#  {'make': 'Samsung', 'model': 7, 'rəng': 'Mavi'}]

# Lüğətlərin siyahısının çeşidlənməsi:
# [{'make': 'Nokia', 'model': 216, 'rəng': 'Qara'}, {'make': 'Samsung', 'model': 7, 'rəng': 'Mavi'},
# { 'make': 'Mi Max', 'model': '2', 'rəng': 'Qızıl'}]


list1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

list1.sort(key=lambda x: x["color"])

print(list1)



models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)




# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]


# 5. Lambda istifadə edərək tam ədədlərin siyahısını filtrləmək üçün Python proqramı yazın. Redaktora gedin
# Tam ədədlərin orijinal siyahısı:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sözügedən siyahıdan cüt rəqəmlər:
# [2, 4, 6, 8, 10]
# Göstərilən siyahıdan tək nömrələr:
# [1, 3, 5, 7, 9]



org_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num_list = list(filter(lambda x: not x % 2, org_list ))
print(f"Even numbers from the said list:\n{even_num_list}")

odd_num_list = list(filter(lambda x: x % 2, org_list))
print(f"Odd numbers from the said list:\n{odd_num_list}")






nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)


print((lambda x: (x % 2 and 'Odd number' or 'Even number'))(5))
print((lambda x: (x % 2 and 'Odd number' or 'Even number'))(8))

print((lambda x: not x % 2 and "even number" or "odd number")(int(input())))

y = lambda x: not x % 2 and "cut eded" or "tek eded"
x = int(input())
print(y(x))

print((lambda x: 2**x)(4)) 


def test(n):
    if n < 2:
        return n % 2 == 0
    return test(n-2)
print(test(23))        



# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# 6. Lambda istifadə edərək verilmiş tam ədədlər siyahısındakı hər bir ədədi kvadrat və kuba çevirmək üçün
# Python proqramını yazın. Redaktora gedin
# Tam ədədlərin orijinal siyahısı:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Göstərilən siyahının hər nömrəsini kvadrata çəkin:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Sözügedən siyahının hər nömrəsini kub edin:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

org_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list of integers:\n{org_integers}")

square_umber_list = list(map(lambda x: x**2, org_integers)) 
print(f"Square every number of the said list:\n{square_umber_list}")

Cube_number_list = list(map(lambda x: x**3, org_integers))
print(f"Cube every number of the said list:\n{Cube_number_list}")



# 7. Write a Python program to find if a given string starts with a given character using Lambda. Go to the editor
# Sample Output:
# True
# False    

# 7. Lambda-dan istifadə edərək verilmiş sətirin verilmiş simvolla başlayıb-başlamadığını tapmaq üçün Python proqramı
#  yazın. Redaktora gedin
# Nümunə çıxışı:
# Doğru
# Yalan

def check_starts_given_character(character,string1):
    if character == string1[0]:
        return True
    else:
        return False

character = input()
string1 = input()
print(check_starts_given_character(character, string1))



def check_starts_given_character(character,string1):
    if character in string1[0]:
        return True
    else:
        return False

character = input()
string1 = input()
print(check_starts_given_character(character, string1))



def check_starts_given_character(character,string1):
    return string1.startswith(character)

character = input()
string1 = input()
print(check_starts_given_character(character, string1))


result = lambda x: x.startswith(character)
character = input()
string1 = input()

print(result(string1))



starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))




# 8. Write a Python program to extract year, month, date and time using Lambda. Go to the editor
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# 8. Lambda istifadə edərək il, ay, tarix və vaxt çıxarmaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə çıxışı:
# 15-01-2020 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178


import datetime
now = datetime.datetime.now()
# import calendar
# n = calendar.month(now.year, now.month)
# print(n)
print(f"""{now}
{now.year}
{now.month}
{now.day}
{now.time()}""")

import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
print(year(now))
month = lambda x: x.month
print(month(now))
day = lambda x: x.day
print(day(now))
time = lambda x: x.time()
print(time(now))



# 9. Write a Python program to check whether a given string is number or not using Lambda. Go to the editor
# Sample Output:
# True
# True
# False
# True
# False
# True
# Print checking numbers:
# True

# 9. Lambda istifadə edərək verilən sətirin nömrə olub-olmadığını yoxlamaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə çıxışı:
# Doğru
# Doğru
# Yalan
# Doğru
# Yalan
# Doğru
# Yoxlama nömrələrini çap edin:
# Doğru


string1 = input()

check_srting_is_num = lambda x: x.replace(".","").replace("-","").isdigit()
print(check_srting_is_num(string1))


string1 = input()

check_srting_is_num = lambda x: "is number" if x.replace(".","").replace("-","").isdigit() else "isn't number"
print(check_srting_is_num(string1))


def check_srting_is_num(string1):
    try:
        float(string1) 
    except (NameError, ValueError):
        return "isn't num"
    return "is num"        

string1 = 'ty'
print(check_srting_is_num(string1))


is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r) #????????????????????????????????????????
print(is_num1('-16.4'))
print(is_num1('-24587.11'))



# 10. Write a Python program to create Fibonacci series upto n using Lambda. Go to the editor
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# Click me to see the sample solution



# 10. Lambda istifadə edərək n-ə qədər Fibonacci seriyası yaratmaq üçün Python proqramı yazın. Redaktora gedin
# Fibonacci seriyası 2:
# [0, 1]
# Fibonacci seriyası 5-ə qədər:
# [0, 1, 1, 2, 3]
# 6-ya qədər Fibonacci seriyası:
# [0, 1, 1, 2, 3, 5]
# 9-a qədər Fibonacci seriyası:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# Nümunə həllini görmək üçün mənə klikləyin

# ??????????????????????????????????????????????????????/
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+ x[-2]], range(n-2), [0, 1])
print(fib_series(10))



# 11. Write a Python program to find the intersection of two given arrays using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]
# Click me to see the sample solution



# 11. Lambda istifadə edərək verilmiş iki massivin kəsişməsini tapmaq üçün Python proqramı yazın. Redaktora gedin
# Orijinal massivlər:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Sözügedən massivlərin kəsişməsi: [1, 2, 8, 9]
# Nümunə həllini görmək üçün mənə klikləyin


list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
list_2 = [1, 2, 4, 8, 9]

list_intersection = list(filter(lambda x: x in list_2, list_1))
print(list_intersection)




# 12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda. Go to the editor
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]
# Click me to see the sample solution


# 12. Lambdadan istifadə edərək verilmiş massivdə müsbət və mənfi ədədləri yenidən yerləşdirmək üçün Python
#  proqramını yazın. Redaktora gedin
# Orijinal massivlər:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Sözügedən massivin müsbət və mənfi ədədlərini yenidən təşkil edin:
# [2, 5, 7, 8, 9, -10, -3, -1]
# Nümunə həllini görmək üçün mənə klikləyin


list_org = [-1, 2, -3, 5, 7, 8, 9, -10]

list_pos = []
list_neg = []

y = list(filter(lambda x: list_pos.append(x) if x > 0 else list_neg.append(x), list_org))

list_pos.sort()
list_neg.sort()
list_rearrange = list_pos + list_neg
print(list_rearrange)




array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)


array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
array_nums.sort(key=lambda i: 0 if i == 0 else -1 / i)
print(array_nums)


# 13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5


# 13. Lambdadan istifadə edərək verilmiş tam ədədlər massivindəki cüt və tək ədədləri saymaq üçün Python proqramı yazın. Redaktora gedin
# Orijinal massivlər:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Yuxarıdakı massivdəki cüt ədədlərin sayı: 3
# Yuxarıdakı massivdəki tək ədədlərin sayı: 5


org_list = [1, 2, 3, 5, 7, 8, 9, 10]
list_even = []
list_odd = []
list(map(lambda x: list_even.append(x) if not x % 2 else list_odd.append(x), org_list))
n_even_num = len(list_even)
n_odd_num = len(list_odd)
print(
f"""Number of even numbers in the above array: {n_even_num}
Number of odd numbers in the above array: {n_odd_num}"""
)



array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)




# 14. Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda. Go to the editor
# Sample Output:
# Monday
# Friday
# Sunday
# Click me to see the sample solution


# 14. Lambda istifadə edərək siyahıdakı dəyərlərin uzunluğunun 6 olub-olmadığını müəyyən etmək üçün verilmiş siyahını süzgəcdən keçirmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə çıxışı:
# bazar ertəsi
# cümə
# bazar günü

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list_1 = []
days = list(filter(lambda x: x if len(x)==6 else "", weekdays))
print("\n".join(days))
print(list_1)

i = 0
while i < len(days):
    print(days[i])
    i+=1

i = 0
while True:
    print(days[i])
    i+=1
    if i == len(days):
        break





weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)



# 15. Write a Python program to add two given lists using map and lambda. Go to the editor
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]
# Click me to see the sample solution


# 15. Map və lambda istifadə edərək verilmiş iki siyahı əlavə etmək üçün Python proqramı yazın. Redaktora gedin
# Orijinal siyahı:
# [1, 2, 3]
# [4, 5, 6]
# Nəticə: iki siyahı əlavə etdikdən sonra
# [5, 7, 9]
# Nümunə həllini görmək üçün mənə klikləyin

list_1 = [1, 2, 3]
list_2 = [4, 5, 6, 10, 17, 10, 100]
list_add = []
    
for i in range(len(list_1)):
    list_add.append(list_1[i] +list_2[i])  
print(list_add)      
list_3 = []
list_add = list(map(lambda x,y: x+y, list_1, list_2 ))
print(list_add)
print(list_3)

   

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("Original list:")
print(nums1)
print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
print("\nResult: after adding two list")
print(list(result))




list_1 = [1, 2, 3, 10, 15, 100, -11]
list_2 = [4, 5, 6]

if len(list_1) > len(list_2):
    t = len(list_1)-len(list_2)
    z = 0
    for i in range(t):
        list_2.append(z)
else:
    t = len(list_2) - len(list_1)
    z = 0
    for i in range(t):
        list_1.append(z)        

list_4 = []
for i, j in zip(list_1, list_2):
    list_4.append(i+j)
print(list_4) 



list_1 = [1, 2, 3, 10, 15, 100, -11]
list_2 = [4, 5, 6, 10, 15]

if len(list_1)>len(list_2):
    list_3 = list_1
    length = len(list_2)
else:
    list_3 = list_2
    length = len(list_1)

print(list_3)
print(length)
for i in range(length):
    list_3[i] = list_1[i] +list_2[i]

print(list_3)






