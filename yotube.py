# print("second \" line")
# print('second " line')
# print("second ' line")
# print("second \n     line")
# print("second \nline")
# print("second \nl\ni\nn\ne")
# print("second \t line")  sanki tab sixilib
# print("second   line")
# print("second\\line")     #biri cap oulunur
# print("second \\ line")   #biri cap oulunur

# a = pow(5, 3) # quvvete yukseltme
# print(a)

# b = pow(3, 2 , 2 )   # yani  2 ** 3 % 2   demekdir
# print(b)

# t = abs(-18)  #  modul
# print(t)

# list1 = [4, 4, 6, -11]
# print(sum(list1))

# list1 = [4, 4, 6, -11, "salam"]   # error verir
# print(sum(list1))




# fruits = ['apple', 'banana', 'mango'] 

# for index, j in enumerate(fruits):
#     print('"%s" (%s)' % (j, index))




# list1 = [1, 2, 3] 
# list2 = ['a', 'b', 'c', 'd']

# for x, y in zip(list1, list2):
#     print(x, y)


# print(list(zip(list1, list2)))


# squared_numbers = [x**2 for x in range(1, 6)]

# print(squared_numbers)
# #[1, 4, 9, 16, 25]


# add = lambda x, y: x + y 

# result = add(10,100)
# print(result)


# numbers = [1, 2, 3, 0, 4]

# result = any(numbers)
# result1= all(numbers)
# print(result)
# print(result1)




# import itertools 
# numbers = [1, 2, 3] 
# result = list(itertools.permutations(numbers))
# print(result)


#output all the permutations 
#[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 0 1 1 2 3 5 8 13 21 34 55 89 144
### Generators created using yield keyword 
# def fibonacci_series(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# # Driver code to check above generator function 
# for number in fibonacci_series(10):
#     print(number)




# def log_function(func):
#     def wrapper(*args, **kwargs):
#         print(f'Running {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'{func.__name__} returned {result}')
#         return result
#     return wrapper

# @log_function
# def add(x, y):
#     return x + y


# print(add(5,7))


# def topla (x,y):
#     def pr():
#         print("cem")
#     return pr

# topla(3,5)() 



# def topla (x,y):
#     def pr():
#         print("cem")
#     return pr

# a = topla(3,5)
# a()





# def dec(func):

#     def inner_func():
#         print("Funksiya cagirildi")
#         print(func(5, 10))
#         print("Funksiya icra olundu")
#     return inner_func    

# @dec
# def topla(x, y):
#     return x+y

# topla()

# print()


# def print_arguments(*args, **kwargs):
#     print(args)
#     print(kwargs)

# print_arguments(1, 2, 3, name='John', age=30, )

#(1, 2, 3)
#{'name': 'John', 'age': 30}

# def print_arguments(*args, **kwargs):
#     for i in args:
#         print(i)
#     for i in kwargs:
#         print(kwargs[i])

# print_arguments(1, 2, 3, name='John', age=30)

#(1, 2, 3)
#{'name': 'John', 'age': 30}





# import importlib

# module_name = 'math'
# module = importlib.import_module(module_name)
# result = module.sqrt(9)
# result1 = module.modf(2.1)
# print(result)
# print(result1)


# squared_numbers = {x: x**2 for x in range(1, 6)}
# print(squared_numbers)

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}





# class Adder:
#     def __call__(self, x, y):
#         return x + y

# adder = Adder()
# result = adder(3, 4)

# print(result)




# num_test = 100_345_405 # this is the number

# print(num_test)

# ## 100345405


# a = 111_11-1
# print(a)





# dictionary_one = {"a": 1, "b": 2}
# dictionary_two = {"c": 3, "d": 4}

# merged = {**dictionary_one, **dictionary_two}

# print(merged)  
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# dictionary_one.update(dictionary_two)

# print(dictionary_one)


# Dəyişən o deməkdir ki, yaddaşdakı obyektin göstəricisini dəyişmədən obyekti (siyahı, dəst və ya lüğət) dəyişdirə
#  və ya yeniləyə bilərik. Gəlin bunu fəaliyyətdə görək.

# Aşağıdakı nümunədə biz yeni şəhər əlavə etməklə şəhərlər siyahısını yeniləyirik. İD-nin (obyekt göstəricisi) eyni
#  qaldığını görə bilərik. Eyni şey dəstlər və lüğət üçün də keçərlidir.

# cities = ["Munich", "Zurich", "London"]
# print(id(cities)) # 2797174365184
# cities.append("Berlin")
# print(id(cities)) # 2797174365184

# my_set = {1, 2, 3}
# print(id(my_set))  # 2797172976992
# my_set.add(4)
# print(id(my_set))  # 2797172976992



###Dictionary 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(id(thisdict))  #2797174128256
# thisdict["engine"] = "2500cc"
# print(id(thisdict))  #2797174128256



# a =3
# print(a) 
# print(id(a))
# a += 1
# print(a)
# print(id(a))



# a = 1
# b = 0
# c = 0

# if ((a or b) and c):
#     print("ok")


# if (a or b and c):
#     print("ko")







# #For loop in one line
# mylist = [200, 300, 400, 500]
# #Single line For loop
# result = [] 
# for x in mylist: 
#     if x > 250: 
#         result.append(x) 
# print(result) # [300, 400, 500]
# #One-line code way
# result = [x for x in mylist if x > 250] 
# print(result) # [300, 400, 500]










# mylist = [200, 300, 400, 500]

# result = [x for x in mylist if x>250 ]
# print(result)

# result1 = list(filter(lambda x: x>250, mylist))
# print(result1)





#Method 1 Single Statement   
# while True: print(1) #infinite 1  
#Method 2 Multiple Statements  
# x = 0   
# while x < 5: print(x); x= x + 1 # 0 1 2 3 4 5

# x = 0
# while x <= 5: print(x); x += 1



























































