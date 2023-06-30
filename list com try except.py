#                                          ### list comprehesion  ###

# adi qayda
list1 = []
a = int(input())
for i in range(a):
    b = int(input())
    list1.append(b)

print(list1)

# list comprehesion 
a = int(input())
list1 = [int(input()) for i in range(a)]

print(list1)



list1 = [int(input()) for i in range(int(input()))]

print(list1)



list1 = [i for i in range(int(input()))]

print(list1)



list1 = [i**2 for i in range(int(input()))]

print(list1)



list1 = [i**2 for i in range(1,int(input()))]

print(list1)



a = 5
b = 10

list1 = [a + b for i in range(int(input()))]

print(list1)



list1 = [input() for i in range(int(input()))]

print(list1)



x = input()

list1 = [x for i in range(int(input()))]

print(list1)



x = input()
a = int(input())

list1 = [x for i in range(a)]

print(list1)



x = input()
a = input()

list1 = [x for i in range(int(a))]

print(list1)



a = int(input())
b = int(input())

list1 = [a + b + i for i in range(int(input()))]

print(list1)



a = 10
b = 9

list1 = [i for i in range(int(input())) if a > b]

print(list1)



a = 6
b = 7

if a > b:
    c = a
else:
    c = b

c = a if a > b else b


list1 = [i if a < b else i**2 for i in range(int(input()))]



a = int(input())
b = int(input())

try:
    c = a//b
except:
    print("0-a bolmek olmaz")    



a = 5
b = "5"

try:
    c = a + b
except:
    print("toplamaq olmaz")     



a = 5
b = "5"

try:
    c = a + b
except:
    print("toplamaq olmaz")   
finally:
    print("eded daxil edin")




try:
    a = int(input())
    b = int(input())
except ValueError:
    print( "Zehmet olmasa eded daxil edin")   



try:
    a = int(input())
    b = int(input())
    c = a // b
except ZeroDivisionError:
    print("0-a bolmek olmaz")
except ValueError:
    print("zehmet olmasa eded daxil edn")
            



#                 ###    Ders 11. List-in daxil olunmasini qisa yazilisi. Comprehesion  ###
                     
#                                           # Ders 10 # 
# 5. İki list dəyişəni götürün. Birinci listdə olub, ikinci listdə olmayan elementləri yeni bir
# listə yığıb çapa verin.

list51 = [int(input()) for i in range(int(input()))]
list52 = [int(input()) for i in range(int(input()))]

print(list51)
print(list52)

list53= [i for i in list51 if i not in list52]

print(list53)



# 6. Elementləri list olan bir list dəyişəni götürün. Bu listin elementlərinin ən böyük
# elementlərini çap edin.

matrix = []
n = int(input())

for i in range(n):
    m = int(input())
    List1 = []
    for j in range(m):
        c = int(input())
        List1.append(c)
    matrix.append(List1)

print(matrix)


for i in matrix:
    max = i[0]
    for j in range(1, len(i)):
        if i[j] > max:
            max = i[j]
    
    print(max, end=" ") 


#####################################
matrix = []

for i in range(int(input())):
    list1 = [int(input()) for j in range(int(input()))]
    matrix.append(list1)

print(matrix)



# 8. Elementləri int tipli olan bir list dəyişəni götürün. Bu listin elementlərinin qiyməti
# qədər “*” çap edin.
# (Məs: [1, 5, 3, 2]
# *
# *****
# ***
# **
# )


list81 = [int(input()) for i in range(int(input()))]

for i in list81:
    print("*" * i)


#                                # Dərs 9. #                     

# 2. Bir list dəyişəni götürün. Bu listin 5-dən böyük və 20-dən kiçik olan elementlərini çap
# edin.


list21 = [int(input()) for i in range(int(input()))]

for i in list21:
    if i > 5 and i < 20:
        print(i, end=", ")




# 4. Bütün elementləri str tipində olan bir list dəyişəni götürün. List daxilində palindrom
# olan elementləri çapa verin. (Palindrom string tərsi özünə bərabər olan stringdir.
# Məsələn: kiçik, kələk və s.)

list41 = [input() for i in range(int(input()))]

for i in list41:
    if i == i[::-1]:
        print(i, end=", ")




# 12. Bir list dəyişəni götürün. Bu listin ən böyük elementi ilə ən kiçik elementini çap edin.

list12 = [int(input()) for i in range(int(input()))]

print(list12)

list12.sort()

print(f"{list12[-1]} en boyuk elementdir, {list12[0]} en kicik elementdir")





#                            # Dərs 10. Məsələlər həlli. Ev tapşırıqları #



# 6. Elementləri list olan bir list dəyişəni götürün. Bu listin elementlərinin ən böyük
# elementlərini çap edin.


list6 = []
a6 = int(input())

for i in range(a6):
    b6 = int(input())
    b7 = int(input())
    list6.append([b6,b7])

print(list6)

for i in list6:
    max = i[0]
    for j in range(1, len(i)):
        if i[j] > max:
            max = i[j]
    
    print(max, end=" ") 




############################################    

list6 = []
a6 = int(input())

i = 0
while i < a6:
    b6 = int(input())
    b7 = int(input())
    list6.append([b6, b7])
    i +=1

print(list6)    


i = 0
while i < len(list6):
    x =list6[i]
    j = 1
    max = x[0]
    while j < len(x):
        if x[j] > max:
            max = x[j]
        j += 1
    i += 1
    print(max, end=", ")




# 7. Elementləri list olan bir list dəyişəni (matris) götürün. Bu matrisdə olan ən böyük
# elementi çap edin.

list7 = []
a7 = int(input())

for i in range(a7):
    b7 = int(input())
    b8 = int(input())
    list7.append([b7,b8])

print(list7)

max = list7[0][0]

for i in list7:
    for j in i:
        if j > max:
            max = j

print(max)

#############################################


list7 = []
a7 = int(input())

i = 0
while i <a7:
    b7 = int(input())
    b8 = int(input())
    list7.append([b7,b8])
    i +=1

print(list7)

max = list7[0][0]

i = 0
while i < len(list7):
    x = list7[i]
    j = 0
    while j < len(x):
        if x[j] > max:
            max = x[j]
        j +=1            
    i += 1

print(max)




#                         ####  internet calismalari  ####


# try:
#     print(x)
# except NameError:
#     print(" x-in qiymeti taninmir")    




# list1 = list(input())

# print(list1)

# for i in range(len(list1)):
#     list1[i] = int(list1[i])

# print(list1)



# a = "imtahana az qalir"
# b = a.split(" ")
# print(b)
# b.reverse()
# print(b)
# b = " ".join(b)
# print(b)
# ????????????????????????????


# list1 = ["salam", "Baki", "Gence"]
# list1 =" ".join(list1)
# print(list1)

# list2 = ["5", "4", "3"]
# list2 =" ".join(list2)
# print(list2)



# a = input().split()

# print(a)




# a, b = input().split()
# a, b = int(a), int(b)
# print(a+b)

# a, b = input(), input()

# print(a+b)



# s = "imtahana az qalir"
# n = s.split(" ")
# m = len(n)
# print(n[m-2])


# a = "bir,iki,uc,dord"
# b = list(a) ; i =0
# print(b)
# while i < len(b):
#     if b[i] == "," and b[i+1] != " ":
#         b.insert(i+1, " ")
#     i = i +1
# b= "".join(b)
# print(b)        
# ????????????????   maraqli meseledi baxaq?????????????


# a = "alma,armud"
# b = list(a)
# print(b)



# list1 = ["salam", 51]
# print(list1[0][0])


# a = "salam"
# b = "t".join(a)
# print(b)


# c = "salam"
# p = c.split()



