# er = "MasalliM"

# # print(er.count("M"))

# print(er.count(er[0]))





# a6, b6 = input().split()

# print(f"{a6}{b6}")





# kitab = "Karlson"

# kitab = kitab.replace("rl", "tf")

# print(kitab)


# kitab1 = "karlson vaqifi akife satdi"


# kitab1 = kitab1.title()

# kitab1 = kitab1.replace("S", "s")

# print(kitab1)


# list41 = [32, 67, 0, 1 ,3 ,2]

# list42 = [-3, 45, 7, 9 ,6]

# list41.reverse()

# list43 = list41 + list42[2:]

# list43.reverse()

# print(list43)






# list21 = [-3, 21, 44, 55, 23, 0 , -39, "salam"]    #burda string olsa error verir?

# list22 = [7, -34, 6, 99]

# list21.sort()

# list22.sort()

# print(list21 + list22)





# list41 = [32, 67, 0, 1 ,3 ,2]

# list42 = [-3, 45, 7, 9 ,6]

# # list41.sort(reverse=True)

# list43 = list41 + list42[-3::-1]

# # list43.sort(reverse=True)

# print(list43)




# list1 = [1, 2]

# list2 = list("salam")


# print(list2)





# Matrix = [
#          [
#             [1,2], 
#             [2,3]
#          ], 
#          [
#             [3, 4], 
#             [5,6]
#          ]
#         ]                  # iterable = coxelemetli deyisenler
# Matrix1 = Matrix[0]
# Matrix1 = Matrix[0][0][0]  # [1,2] cap olunur

# print(Matrix1)



# list1 = [45, -20, 13, 34, 50, -21]
# list2 = list1[:3]
# list2.reverse()

# print(list2)




# list1 = [45, -20, 13, 34, 50, -21]
# list1.clear()
# # list1 = list1[0:3]
# # print(list1)

# print(list1)





# list200 = [5, 6, 89]

# list200.pop(2)

# print(list200)






# list1 = [45, -20, 13, 34, 50, -21]

# k = list1.pop(3)

# print(k)

# print(list1)



# set1 = {2, 3, 4}

# set1.update(8)

# print(set1)




# list1 = [4, "salam"]



# print(list1[1])




# extend             #Extend list by appending elements from the iterable.

# list1 = [45, -20, 13, 34, 50, -21]

# list1.extend("32")

# # print(list2)

# print(list1)





# list1 = [3, 4, 5]

# list2 = list1.copy()

# # list2 = list1

# print(list1)
# print(list2)






# h = "tirmanoldu irmanoldu"

# l = h.capitalize()

# print(l)







# a = 5

# b = 15

# if a < 6 and b > 15:
#     print("a 5-den kicikdir")
#     a = 6 
# elif a == 3 and b < 12:
#     print(" a = 3")
# if a == 5:
#     print(a)





# a = 5

# b = 15

# if a < 5 and b > 15:
#     print("a 5-den kicikdir")
#     a = 6 
# elif a == 3 and b < 12:
#     print(" a = 3")
# elif a == 5:
#     print(3)    










# a = 12

# b = 19


# if a > 5:
#     print("y")
    
# elif b:
#     print(9090)


# if a > 4:
#     if a < 2:     # niye error vermir?????
#         print(8)
    

    


#####  x**2 - 7x + 10 = 0

# a = 1

# b = -7

# c = 10

# D = b**2 - 4*a*c

# print(D)

# x1 = (-b + D**(1/2)) / 2*a
# x2 = (-b - D**(1/2)) / 2*a

# print(x1, x2)










# list = [3, 4, 4]





# print(list)



set = {1, 3}









# pl = "gence seheri"

# pl.capitalize


# print(pl.capitalize)



# list1 = [4, 4, 6]


# list1[2] = 12

# print(list1)





# list1 = [3, 4 ,4]

# list1 = list1.extend('53')

# print(list1)




# string = "lim"

# string = string.capitalize()

# print(string)



# p = "azerbaycan"

# # p = p.upper()

# print(p.upper())



# list = []
# a = int(input())


# for i in range(a):
#     b = int(input())
#     list.append(b)


# for i in list:
#     for j in range(2, i):
#         if not i % j:
#             print(f"{i} murekkeb ededdir")
#             break
#     else:
#         print(f"{i} sade ededdir")
             


    


# Mekteb = {
#     "Olke": "Azerbaycan",
#     "Seher": "Sumqayit",
#     "Nomre": 25,
#     "Istiqamet": "Pilot"
# }

# Mekteb.pop("Olke")
# Mekteb.pop("Seher")
# Mekteb.pop("Nomre")
# Mekteb.pop("Istiqamet")

# print(Mekteb)



# 5. İki int tipli a və b dəyişəni götürün. a və b aralığında mükəmməl ədədləri çapa verin.
# (Bütün bölənlərinin cəminə bərabər olan ədəd mükəmməl ədəddir. Məs: 6 = 1+2+3
# və s.)


# a = int(input())
# b = int(input())

# for i in range(a+1, b):
#     c = 0
#     for j in range(1, i):
#         if not i % j:
#             c += j
#     if c == i:
#         print(i, end=", ")        



# 7. Dövr operatorlarından istifadə edərək aşağıdakı fiquru çap edin:
# *********
#  *******
#   *****
#    ***
#     *




# a = int(input())
# b = int(input())

# for i in range(a+1, b):
#     c = 0
#     for j in range(1, i):
#         if not i % j:
#             c += j
#             if c == i:
#                 print(i, end=", ")   





# uu = "Menproqramlasdirmaoyrenirem."

# print(uu.split())



# for i in range(0, 9, 2):
#     x = 9-i
#     y = "*" * x
#     for j in range(0, 5):
#         t = j * " "
#         print(t + y )





# n = int(input())

# for i in range(n-1):
#     i = n-1-i
#     print(("*" * ((2*n-1) - (2*i))).center(2*n-1))
    

    
# for i in range(n):
#     print(("*" * ((2*n-1) - (2*i))).center(2*n-1))








# for i in range(5):
#     i = 4-i
#     print(("*" * (9-2*i)).center(9))







# uu = "Men proqramlasdirma oyrenirem."

# print(uu.split())

# print(uu.split("p")) 



# a = "imtahana az qalir"
# b = a.split(" ")
# print(b)
# b.reverse()

# b = " ".join(b)
# print(b)




# a = 5

# b = 15


# if print(a):
#     print(a)





# a = 0

# b = 15

# if a == 0 and b:
#     print(a)
# elif not a:
#     print(b) 






# matrix = []
# n = int(input())

# i = 0
# while i < n:
#     m = int(input())
#     List1 = []
#     j = 0
#     while j < m:
#         c = int(input())
#         List1.append(c)
#         j += 1
#     matrix.append(List1)
#     i += 1

# print(matrix)  

# i = 0
# while i < len(matrix):
#     x =matrix[i]
#     j = 1
#     max = x[0]
#     while j < len(x):
#         if x[j] > max:
#             max = x[j]
#         j += 1
#     i += 1
#     print(max, end=", ")



# matrix = []
# n = int(input())

# i = 0
# while i < n:
#     m = int(input())
#     List1 = []
#     j = 0
#     while j < m:
#         c = int(input())
#         List1.append(c)
#         j += 1
#     matrix.append(List1)
#     i += 1

# print(matrix)

# max = matrix[0][0]

# i = 0
# while i < len(matrix):
#     x = matrix[i]
#     j = 0
#     while j < len(x):
#         if x[j] > max:
#             max = x[j]
#         j +=1            
#     i += 1

# print(max)




# def myfunction(a,b):
#     c = a + b
#     return c
# myfunction = lambda a, b: a + b 

# a = int(input())
# b = int(input()) 
# print(myfunction(a, b))








# print(list(map(lambda n: n, range(10))))

# print(list(filter(lambda n: n, range(10))))



# print(list(map(lambda n: n > 5, range(10))))

# print(list(filter(lambda n: n > 5, range(10))))




# def my_function(n):
#     if n > 5:
#         return n

# n = int(input())
# print(list(filter(my_function, range(n))))


# def my_function(n):
#     return n > 5

# n = int(input())
# print(list(filter(my_function, range(n))))




# def my_function(n):
#     if n > 5:
#         return n

# n = int(input())
# print(list(map(my_function, range(n))))


# def my_function(n):
#     return n > 5

# n = int(input())
# print(list(map(my_function, range(n))))




# n = int(input())
# print(list(filter(lambda n: 2**n, range(n))))     #  hetta bu halda 0- i da goturdu????????????

# n = int(input())
# print(list(map(lambda n: 2**n, range(n))))






# def pow_2(n):
#     for i in range(n):
#         print(f"{2}^{n} = {2** i}")

# n = int(input())
# print(pow_2(n))







# my_list = [12, 65, 54, 39, 102, 339, 221,]

# for i in my_list:
#     if not i % 13:
#         print(f"{i} ededi 13-e bolunur") # burda nece bu sekilde yazim???????????
# #                                        # 65, 39, 221 ededleri 13-e bolunur#





# list1 = [input() for i in range(int(input()))]

# print(list1)



# x = input()

# list1 = [x for i in range(int(input()))]

# print(list1)





# x = input()
# a = int(input())
# list1 = [x for i in range(a)]

# print(list1)





# matrix = []
# n = int(input())

# for i in range(n):
#     m = int(input())
#     List1 = []
#     for j in range(m):
#         c = int(input())
#         List1.append(c)
#     matrix.append(List1)

# print(matrix)


# matrix = []

# for i in range(int(input())):
#     list1 = [int(input()) for j in range(int(input()))]
#     matrix.append(list1)

# print(matrix)



# matrix = [int(input()) for i in range([int(input()) for j in range(int(input()))])]



# n = int(input())
# list1 = list(map(lambda n: 2**n, range(n)))


# for i in list1:
#     print(f"{2} ^ {n} = {i}")



# def pow_2(n):
#     for i in range(n):
#         print(f"{2}^{n} = {2** i}")

# n = int(input())
# pow_2(n)



# pow_2 = lambda n: 2**n

# n = int(input())
# print(list(map(pow_2, range(n))))



# # Display the powers of 2 using anonymous function
# terms = 10

# # Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# # use anonymous function
# result = list(map(lambda x: 2 ** x, range(terms)))

# print("The total terms are:",terms)
# for i in range(terms):
#    print("2 raised to power",i,"is",result[i])  


# my_list = [12, 65, 54, 39, 102, 339, 221]
# list1 = []

# for i in my_list:
#     if not i % 13:
#         list1.append(str(i))
# list1 = ", ".join(list1)        
# print(list1, end=" ")   
# print("edeleri 13-e bolunur")        







# def recur_fib(
# n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return recur_fib(n-1) + recur_fib(n-2)

# a = int(input())
# if a < 0:
#     print("Plese enter a positive integer")
# else:
#     print(recur_fib(a))



# print(1//2)




# def binary_2(n):
#     str1 = ""
#     for i in range(n, 0, -1):
#         str1 += str(n % 2)
#         n //= 2
#         if n == 0:
#             break
#     return str1[::-1]

# number = int(input())
# print(binary_2(number))





# def binary_2(n):
#     for i in range(n, 0, -1):
#         y = n % 2
#         print(y)
#         n //= 2
#         if n == 0:
#             break
        

# number = int(input())
# binary_2(number)




# n = int(input())

# for i in range(2, n):
#     if not n % i:
#         print("Eded murekkebdir")
 





# lower = int(input())
# upper = int(input())

# def check_prime_numbers(n, z):
#     for i in range(n+1, z):
#         for j in range(2, i):
#             if not i % j:
#                 break
#         else:            
#             print(i, end=", ")

# check_prime_numbers(lower, upper)
# print()






# def factorial(x):
#     if x == 1 or x ==0:
#         return 1
#     else:
#         return (x * factorial(x-1))

# num = int(input())
# if num < 0:
#     print("Factorial is not defined for negative numbers")
# else:    
#     y = factorial(num)
#     print(f"{num} factorial is {y}")





# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         # recursive call to the function
#         return (x * factorial(x-1))


# change the value for a different result


# try:
#     num = int(input())
# except RecursionError:
#     print("maximum recursion depth exceeded")    
# else:
#     result = factorial(num)
#     print("The factorial of", num, "is", result)




# def multiplication_table_of_12(n, z):
#     for i in range(1, n):
#         print(f"{z}^{i} = {z*i}")

# number = int(input())
# multiply_number = int(input())
# multiplication_table_of_12(multiply_number, number)






# def fabionacci(n11):
#     a11 = 1
#     b11 = 1
#     print(a11)
#     print(b11)
#     for i in range(3, n11+1):
#         a11 = b11
#         b11 = a11 + b11      # a11, b11 = b11, a11 + b11
#         print(b11)

# n11= int(input())

# fabionacci(n11)





# def half_pyramid_using_number(n):
#     str1 = ""
#     for i in range(n, 0, -1):
#         str1 += ("*" + " ").center(i)   
#         print(str1)
#         # print()
        
# num = int(input())
# half_pyramid_using_number(num)



# alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# print(alphabets[0]*3)



# def pyramid(n):
#     str1 = ""
#     for i in range(1, n+1, 2):
#         print(("*" * i).center(n))

# num = int(input())
# pyramid(num)




# def pyramid(n):
#     for i in range(1, n+1, 2):
#         x = ("*" * i).center(n)
#         y ="  ".join(x)
#         print(y)

# num = int(input())
# pyramid(num)





# def recur_fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return recur_fib(n-1) + recur_fib(n-2)

# a = int(input())
# if a < 0:
#     print("Plese enter a positive integer")
# else:
#     for i in range(1, a + 1):
#         print(recur_fib(i))





# Nümunə 7: Ədədlərin Tam Piramidası
#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5

# n = int(input())

# for i in range(1, n + 1):
    
#     for k in range(1, n-i+1):
#         print(" ", end=" ")
#     for j in range(i, 2*i):
#         # print(i+j-1, end=" ")
#         print(j, end=" ")    
#     for z in range(2*i-1, 0, -1):
#         x = z-1
#         if x == 0:
#             break
#         print(x, end=" ")
#         if z == i+1:
#             break  
        
#     print()




# def full_pyramids(n):
#     for i in range(n-1, -1, -1):
#         print(("* " * ((2*n-1)-(2*i))).center((2*n-1)*2))

# num = int(input())
# full_pyramids(num)


# ######################################################################
# def pyramid(n):
#     for i in range(1, n+1, 2):
#         print(("*" * i).center(n))

# num = int(input())
# pyramid(num)



# x = 5

# def check_number(n):
#     if number > 0:      #   burda number yazdim sehv vermedi??????????????????
#         return x
#     if n < 0:
#         return "number is negative"
#     else:
#         return "you enter zero"     

# number = int(input())
# print(check_number(number))



# def p(n):
#         return 2


# num = int(input())
# print(p(num))




# x = sum(5,3)
# print(x)


# Example 9: Pascal's Triangle
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1

# def full_pyramid_of_numbers(n):
#     str1 = ""
#     for i in range(5):
#         str1 = i 
              

# num = int(input())
# full_pyramid_of_numbers(num)




# Example 9: Pascal's Triangle
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1

# num = int(input())
# def full_pyramid_of_numbers(n):
#     for i in range(1, n + 1):
#         for k in range(1, n-i+1):
#             print(" ", end=" ")
#         for j in range(1, i+1):
#             print(j, end=" ")    
#         for z in range(i-1, 0, -1):

#             # if x == 0:
#             #     break
#             print(z, end=" ")
#             # if z == i+1:
#          #     break  
        
#         print()
     
# full_pyramid_of_numbers(num)





# num = int(input())
# def full_pyramid_of_numbers(n):
#     for i in range(0, n+1):
#         for k in range(1, n-i+1):
#             print("x", end="  ")
#         for j in range(1, i+1):
#             print(j, end="  ")
            
#         for z in range(i+1, 0, -1):
#             print(z, end="  ")
#         print()
     
# full_pyramid_of_numbers(num)



# Example 9: Pascal's Triangle
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1


# binom = [[1], [1,1] ]

# n = int(input())

# for i in range(2, n+1):
#     binom.append([])
#     binom[i].append(1)
#     for j in range(1,i):
#         binom[i].append(binom[i-1][j-1] + binom[i-1][j])
#     binom[i].append(1)    
    
# print(binom)






# Example 9: Pascal's Triangle
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1



# num = int(input())
# def full_pyramid_of_numbers(n):
    
#     for i in range(0, n+1):
#         x = 2
#         for k in range(1, n-i+1):
#             print(" ", end=" ")
#         for z in range(1, x):
#             x += 1
#             print(z, end="   ")
#         print()
            
#         # for z in range(i+1, 0, -1):
#         #     print(z, end="   ")
#         # print()
     
# full_pyramid_of_numbers(num)







# class Person:
#     num_ears = 2
#     has_hands = True

#     def __init__(self, id, name, surname,sex, age, nationality, education):
#         self.id = id
#         self.name = name
#         self.surname = surname
#         self.sex = sex
#         self.age = age
#         self.nationality = nationality
#         self.education = education

#         print("Person obyekti yaradildi")

#     def get_fullname(self):
#         return self.name +" " + self.surname

#     def get_full_info(self):
#         return f"{self.id}  - {self.name} - { self.surname} -{self.sex} - {self.age} - {self.nationality} - {self.education}"


# class Teacher(Person):
#     has_bag = False
#     def __init__(self, num_lesson=0):
#         # super().__init__(id, name, surname,sex, age, nationality, education)
#         self.num_lesson = num_lesson

#         print("Teacher obyekti yaradildi")

#     def get_education(self):
#         return 5

# adem = Person(1, "Adem", "Orucov", "Kisi", 24, "azerbaycanli", "ali")
# idrak = Person(2, "Idrak", "Seyfullayev", "Kisi",35, "azerbaycanli", "ali")
# idrak = Teacher(100)


# # print(idrak.get_education())
# print(idrak.get_fullname())

# print(idrak.get_full_info())

# print(idrak.education)

# print(adem.age)
# print(idrak.age)



# print(idrak.get_education())





# def check_prime_composite_number(n):
#         if n <= 0:
#             return "isn't natural number"
#         elif n==1:
#             return "neither a prime nor a composite number"    
#         for i in range(2, n):
#             if not n% i:
#                 return "a composite number"
#         else:
#             return "a prime number" 

# num =49
# print(check_prime_composite_number(num))








# list1 = [2, 3, 4, 5, 9, 32 , 11]
# list2 = [4, 2,7, 8, 9, 3]
# list3 = []

# for i in list1:
#     if i not in list2:
#         list3.append(i)

# print(list3)        




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
#         return str1       # burda print(i,end= " ")  verende qarisdi printe verdiyim netice
                
        
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

#     def ekob(self, t):
#         return (self.n * t) / Math.ebob(self, t)  # eger bu class-da da coxlu obyekt olsa  idi onda nece taniyir self???
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

# print(f"Eded_{eded_10} - "
# f"Bolenlerin_sayi:{eded_10.bolenlerin_sayi()}, "
# f"Bolenleri:{eded_10.bolenleri_()} "
# f"EBOB({eded_10.n},{35})={eded_10.ebob(35)}, " 
# f"EKOB({eded_10.name},{45})={eded_10.ekob(45)} "
# f"Factorial_{eded_10}={eded_10.factorial()}, "
# f"Eded_{eded_10}:{eded_10.check_prime_composite_number()}, " 
# f"Eded_{eded_10}:{eded_10.check_perfect_number()}, "
# f"Eded_{eded_10}:{eded_10.check_square_number()}, "
# f"Arranged({eded_10},{5})={eded_10.calculate_arranged(5)}")



# func1_adds_15 = lambda n, 15: 


# list1 = [(10, 4, 87), (7, 45, 24), (23, -1, 100)]

# list1.sort(key=lambda x: x[2])
# print(list1)



# list1 = [4, -1, 0, -4, 3]

# list2 = sorted(list1)

# print(list2)



# n = 1
# while True:
#     x = n / 20
#     # print(x)
#     if x > 4:
#         break
#     print(n)
#     n += 1


# n = 1
# while n / 20 <= 4:
#     print(n)
#     n +=1


# n = 1
# while x < 4:
#     x = n / 20  
#     print(n)
#     n +=1



# n = 1
# x = 1
# while x < 4: # burda kodlarin oxunmasi qaydasi necedi????
#     x = n / 20  
#     print(n)
#     n +=1


# list_org = ["2","1",'-3','-4']
# print(list_org)
# list_1 = []
# list_2 = []

# y = list(filter(lambda x: list_1.append(int(x)) if int(x)>0 else list_2.append(int(x)), list_org))
# # for i in list_org:
# #     y(int(i))

# list_1.sort()
# list_2.sort()
# print(list_1 + list_2)



    


    
# list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# list_2 = [1, 2, 4, 8, 9]

# list_intersection = list(filter(lambda x: x if x in list_2 else "4", list_1))
# print(list_intersection)

# list_intersection = list(map(lambda x: x if x in list_2 else "4", list_1))
# print(list_intersection)



# list_5 = list(map(lambda x: x+5, range(5)))
# print(list_5)

# list_5 = list(filter(lambda x: x+5, range(5)))
# print(list_5)



# operator
# menimsetme =
# a = 5

# 2. Arifmetik operatorlar
# +, -, *, /, //, %, **


# print(1/3)
 
# a = -5
# b = -1
# print(a-b)


# c = 5

# a = "Fatime"
# b = c
# c  = float(c)
# b = c
# print(a + b)

# t = 5
# z = str(t)
# y = "2.5"
# y = float(y)
# # y = int(y)

# print(t+y)


# a= 10
# b =2
# c= 2 + 2 / 2
# print(c)
# print(type(b))
# print(type(c))
# print(type(a))


# 3. Artirma, Azaltma (Increment, Decrement) operatorlari
# +=, -=, *=, /=, //=, %=, **=


# a = 9
# b = 2
# a  **= b



ad = "Zamin"

for i in ad:
    print(i)
    









