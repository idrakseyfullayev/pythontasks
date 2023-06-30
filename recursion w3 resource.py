#                                  Recursion [ 11 exercises with solution]




# 1. Write a Python program to calculate the sum of a list of numbers. Go to the editor
# Click me to see the sample solution

# 1. Rəqəmlər siyahısının cəmini hesablamaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin

def rec_sum_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + rec_sum_list(num_list[1:])


num_list = [2, 4, 5, 6, 7]
print(rec_sum_list(num_list))



# 2. Write a Python program to convert an integer to a string in any base. Go to the editor
# Click me to see the sample solution

# 2. İstənilən bazada tam ədədi sətirə çevirmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin

#???????????????????????????????????????

def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))




# 3. Write a Python program to sum recursion lists. Go to the editor
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
# Click me to see the sample solution

# 3. Rekursiya siyahılarını cəmləmək üçün Python proqramı yazın. Redaktora gedin
# Test Məlumatı: [1, 2, [3,4], [5,6]]
# Gözlənilən Nəticə: 21
# Nümunə həllini görmək üçün mənə klikləyin


list_1=[1, 2, [3,4], [5,6]]
def rec_sum_list(sum_list):
    sum_ = 0
    for num in sum_list:
        if type(num) != type([]):
            sum_ += num
        else:
            sum_ += rec_sum_list(num)
    return sum_

print(rec_sum_list(list_1))


def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))


list_1=[1, 2, [3,4], [5,6]]
def sum_list(list_):
    sum_=0
    for i in list_:
        if str(i).isdigit():
            sum_ += i
        else:
            for j in i:
                sum_ += j
    return sum_            
print(sum_list(list_1))            



list_1=[1, 2, [3,4], [5,6]]
def sum_list(list_):
    sum_ = 0
    for i in list_:
        try:
            sum_ += i
        except TypeError:
            for j in i:
                sum_+=j
    return sum_            
print(sum_list(list_1))




# 4. Write a Python program to get the factorial of a non-negative integer. Go to the editor
# Click me to see the sample solution

# 4. Mənfi olmayan tam ədədin faktorialını almaq üçün Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin


def rec_fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n * rec_fac(n-1)

try:
    num = int(input())
    print(rec_fac(num))            
except ValueError:
    print("You enter the text, Please, enter only positive number")
except RecursionError:
    print("You enter negative number, Please enter only positive number")


# 5. Write a Python program to solve the Fibonacci sequence using recursion. Go to the editor
# Click me to see the sample solution

# 5. Rekursiyadan istifadə edərək Fibonaççi ardıcıllığını həll etmək üçün Python proqramı yazın. Redaktora gedin
# Nümunə həllini görmək üçün mənə klikləyin

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
def rec_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)

try:
    num = int(input())
    print(rec_fib(num))            
except ValueError:
    print("You enter the text, Please, enter only positive number")
except RecursionError:
    print("You enter negative number or zero, Please enter only positive number")


def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

print(fibonacci(7))


# a = 200
# b = 100

# if a == 200 and b < 150 and (a+b) > 301:
#     print('netice boyukdur 50-den')
# elif not (not (a > 250 or b > 150) and not a < 300 or not b > 100) :
#     print('ifade dogrudur')   


# a = 0

# if a == 0:
#     print('Beli')


# ax**2 +bx +c = 0
# 2x**2 -5x +2 = 0



