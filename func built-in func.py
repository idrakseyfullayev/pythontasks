# def myfunction(a,b):
#     return a + b

# myfunction = lambda a, b: a + b     # funksiyanin qisa yazilisi

# print(myfunction(5, 3))




# def myfunction(a,b):
#     c = a + b
#     return c

# myfunction = lambda a, b: a + b    # funksiyanin qisa yazilisi

# print(myfunction(5, 3))



# myfunction = lambda a, b: a + b if a < b else a - b

# print(myfunction(5, 3))



###       built in fuksiyalari

# 1. map() funsiyasi
 

# def pow_2(n):
#     return 2** n

# n = int(input())
# print(list(map(pow_2, range(n))))



# def pow_2(n):
#     if n > 3:
#         return 2** n

# n = int(input())
# print(list(map(pow_2, range(n))))


# def pow_2(n):
#     n = n + 5
#     return 2** n

# n = int(input())
# print(list(map(pow_2, range(n))))






# pow_2 = lambda n: 2**n

# n = int(input())

# print(list(map(pow_2, range(n))))




# pow_2 = lambda n: 2**n

# n = int(input())

# print(list(map(pow_2, range(1, n))))



# n = int(input())
# print(list(map(lambda n: 2**n, range(n))))



# print(list(map(lambda n: n, range(10))))



# 2. chr ve ord   ASCII  funksiyalari

# x = chr(97)
# y = ord(x)
# print(x, y)

# print(chr(100))
# print(ord("g"))

# print(list(map(ord, "salam")))

# print(list(map(chr, range(97,123))))

# lowers = (list(map(chr, range(97,123))))
# print(lowers)



# 3. enumerate

# print(list(enumerate(iterable)))
# print(list(enumerate([5, 9, 3, 7, 2])))



# 4. zip()

# print(list(zip([1,2,3], [5,9,8], [2,0,4])))

# print(list(zip([1,2,3,7], [5,9,8,6], [2,0,4])))



# 5. filter()

# def my_function(n):
#     if n > 5:
#         return n

# n = int(input())
# print(list(filter(my_function, range(n))))




# print(list(filter(lambda n: n > 5, range(10))))



# print(list(filter(lambda n: n > -1, range(10))))



# print(list(filter(lambda n: n > -5, range(10))))



# print(list(filter(lambda n: n, range(10))))



# def my_function(n):
#     return n

# n = int(input())
# print(list(filter(my_function, range(n))))



# n = int(input())
# print(list(filter(lambda n: 2**n, range(n))))



####################################################################################################




# n = int(input())
# print(list(filter(lambda n: 2**n, range(n))))   #  hetta bu halda 0- i da goturdu????????????


# n = int(input())
# print(list(map(lambda n: 2**n, range(n))))