# for i in range(1, 100):
#     if i == 10:
#        break
#     print(i)

# for i in range(1, 100):
#     if i == 10:
#         continue
#     print(i)    


 

# list1 = [143, 27, 17, 55]


# for i in list1:
#     for j in range(2,i):
#         if not i % j:
#             print(f"{i} murekkebdir")
#             break
#     else:
#         print(f"{i} sadedir")    
    




# i = 0

# while i < 100:
#     i += 1
#     print(i)




# i = 0

# while i < 100:
#     print(100 - i)
#     i += 1







# i = 104

# while i > 100:
#     print(i)
#     i -= 1




# i = 0

# while i < 100:
#     print(i)
#     i += 1
#     if i == 40:
#         break






# i = 0

# while i < 100:
#     i += 1
#     print(i)
    


# i = 0

# while True:
#     print(i)
#     i += 1
#     if i ==10:
#         break





# i = 100

# while i:
#     print(i)
#     i -= 1


# for i in range(1, 100):
#     if i == 10:
#        break
#     print(i)

# for i in range(1, 100):
#     if i == 10:
#         continue
#     print(i) 


#                         ##  Dərs 9. Dövr operatorları. While dövr operatoru. Ev tapşırıqları  ##
#                               (Məsələləri həm for, həm də while operatoru ilə həll edin.)

# 1. İki int tipli a və b dəyişəni götürün. a və b aralığında eyni anda həm 2-yə, həm də 3-ə
# bölünən ədədlərin cəmini hesablayın.

a1 = int(input())
b1 = int(input())
c1 = 0

for i in range(a1 + 1, b1):
    if not i % 2 and not i % 3:
        c1 += i
                                   
if c1 == 0:
    c1 = "bu araligda bele eded yoxdur"
           
print(c1)


#########################

a1 = int(input())
b1 = int(input())
c1 = 0

i = a1
while i < b1-1:
    i += 1
    if not i % 2 and not i % 3:
        c1 += i

if c1 == 0:
    c1 = "bu araligda bele eded yoxdur"

print(c1)


# 2. Bir list dəyişəni götürün. Bu listin 5-dən böyük və 20-dən kiçik olan elementlərini çap
# edin.

list2 = []
a2 = int(input())

for i in range(a2):
    b2 = int(input())
    list2.append(b2)

for i in list2:
    if i > 5 and i < 20:
        print(i, end =" ")

###################################################

list2 = []
a2 = int(input())

i = 0
while i < a2:
    i += 1
    b2 = int(input())
    list2.append(b2)

j = 0
while j < len(list2):
    
    if list2[j] > 5 and list2[j] < 20:
        print(list2[j], end= " ")
    j += 1

print(list2)      # bunu nece edim novbeti setrde cap olunsun yani asagida???????????


# 3. Bir int tipli dəyişən götürün. Daxil olunmuş ədədin bütün bölənlərini çapa verin.

a3 = int(input())

for i in range(1, a3 +1):
    if not a3 % i:
        print(i, end= ",")

##############

a3 = int(input())

i = 0
while i < a3:
    i += 1
    if not a3 % i:
        print(i, end= ",")


# 4. Bütün elementləri str tipində olan bir list dəyişəni götürün. List daxilində palindrom
# olan elementləri çapa verin. (Palindrom string tərsi özünə bərabər olan stringdir.
# Məsələn: kiçik, kələk və s.)

list4=[]
a4 = int(input())

for i in range(a4):
    b4 = input()
    list4.append(b4)

for i in list4:
    if i == i[::-1]:
        print(i, end=", ")

#################################

list4 = []
a4 = int(input())

i = 0
while i < a4:
    i += 1
    b4 = input()
    list4.append(b4)


j = -1
while j < len(list4) - 1:
    j += 1
    if list4[j] == list4[j][::-1]:
        print(list4[j], end=", ")


# 5. İki int tipli a və b dəyişəni götürün. a və b aralığında mükəmməl ədədləri çapa verin.
# (Bütün bölənlərinin cəminə bərabər olan ədəd mükəmməl ədəddir. Məs: 6 = 1+2+3
# və s.)

a5 = int(input())
b5 = int(input())

for i in range(a5+1, b5):
    c5 = 0
    for j in range(1, i):
        if not i % j:
            c5 += j
    if c5 == i:
        print(i, end=" ")

#################################

a = int(input())
b = int(input())

i = a
while i < b+1:
    j = 1
    c = 0
    while j < i:
        if not i % j:
            c += j
            
        j += 1
        
    if c == i:
        print(f"{i} mukemmel ededdir")
    i += 1    


# 6. Dövr operatorlarından istifadə edərək aşağıdakı fiquru çap edin:
# *****
# ****
# ***
# **
# *

for i in range(0,5):
    x = 5-i
    print("*" * x)

##############################################

i = -1
while i < 4:
    i += 1
    x = 5-i
    print("*" * x)

    
# 7. Dövr operatorlarından istifadə edərək aşağıdakı fiquru çap edin:
# *********
#  *******
#   *****
#    ***
#     *

for i in range(5):
    print(("*" * (9-2*i)).center(9))

n = int(input())
for i in range(n):
    print(("*" * ((2*n-1)-2*i)).center(2*n-1))
    
##################################################

i = 0
while i < 5:
    print(("*" * (9-2*i)).center(9))
    i +=1

n = int(input())
i = 0
while i < n:
    print(("*" *((2*n-1)-2*i)).center(2*n-1))
    i += 1


# 8. İki int tipli a və b dəyişəni götürün. a və b aralığında kvadrat ədədlərin hasilini tapın.

a8 = int(input())
b8 = int(input())

for i in range(a8 + 1, b8):
    if i**0.5 == int(i**0.5):
        print(i)

##############################################

a8 = int(input())
b8 = int(input())

i = a8+1
while i < b8:
    if i**(1/2) == int(i**(1/2)):
        print(i, end=", ")
    i += 1


# # 9. İki int tipli a və b dəyişəni götürün. a və b aralığında bölənlərinin sayı 3 olan ədədləri
# çap edin.

a9 = int(input())
b9 = int(input())

for i in range(a9+1, b9):
    c9 = 0
    for j in range(1, i+1):
        if not i % j:
            c9 += 1
    if c9 == 3:
        print(i, end=" ") 

##############################################

a9 = int(input())
b9 = int(input())

i = a9+1
while i < b9:
    c = 0
    j = 1
    while j < i+1:
        if not i % j:
            c += 1
        j += 1    
    if c == 3:
        print(i, end=" ")         
    i += 1


# 10. Dövr operatorlarından istifadə edərək aşağıdakı vurma cədvəlini çapa verin:
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# .....
# 5 * 10 = 50

for i in range(1, 11):
    x = 5*i
    print(f"{5} * {i} = {x}")

#######################################

i = 0
while i < 10:
    i += 1
    x = 5 * i
    print("{} * {} = {}".format(5, i, x))


# 11. İki int tipli a və b dəyişəni götürün. Onların aranjemanını hesablayıb çap edin.
# (Aranjeman bu düsturla hesablanır: A(a,b) = a!/(a-b)!)

a11 = int(input())
b11 = int(input())
c11 = 1
d11 = 1

for i in range(2, a11+1):
    c11 *= i

for j in range(2, a11-b11+1):
    d11 *= j

print(c11/d11)

###############################################

a11 = int(input())
b11 = int(input())
c11 = 1

for i in range(a11-b11+1, a11+1):
    c11 *= i
print(c11)

################################################

a11 = int(input())
b11 = int(input())
c11  = 1
d11  = 1

i = 1
while i < a11:
    i += 1
    c11 *= i
    
j = 1
while j < a11 - b11:
    j  += 1
    d11 *= j
    
print(c11/d11)


# 12. Bir list dəyişəni götürün. Bu listin ən böyük elementi ilə ən kiçik elementini çap edin.

list12 = []
a12 = int(input())

for i in range(a12):
    b12 = int(input())
    list12.append(b12)

list12.sort()
print(f"{list12[0]} en kicik elementdir", end=", ")
print("%d en boyuk elementdir" % (list12[-1]))

#########################################

list12 = []
a12 = int(input())

i = 0
while i < a12:
    i += 1
    b12 = int(input())
    list12.append(b12)

list12.sort()
print("{} en kicik elementdir, {} en boyuk elementdir".format(list12[0], list12[-1]))




#                      #   Dərs 10. Məsələlər həlli. Ev tapşırıqları #

# 1. Dövr operatorlarından istifadə edərək aşağıdakı fiquru çap edin.
#   *
#  ***
# *****
#  ***
#   *

n = int(input())

for i in range(n-1):
    i = n-1-i
    print(("*" * ((2*n-1) - (2*i))).center(2*n-1))
    
for i in range(n):
    print(("*" * ((2*n-1) - (2*i))).center(2*n-1))

#########################################################

n = int(input())

i = 0
while i < n-1:
    x = n-1-i
    print(("*" * ((2*n-1) - (2*x))).center(2*n-1))
    i += 1
    
i = 0
while i < n:
    print(("*" * ((2*n-1) - (2*i))).center(2*n-1))
    i += 1


# 2. Daxil olunmuş ədədin 1-dən və özündən fərqli ən kiçik böləni ilə ən böyük böləninin
# cəmini tapın.

a2 = int(input())

for i in range(2, a2):
    if not a2 % i:
        print(i + a2//i)
        break
else:
    print("boleni yoxdur")

############################################

a2 = int(input())

c = 0

i = 2
while i < a2:
    if not a2 % i:
        print(i + a2//2)
        c = 1
        break
    i += 1

if not c:
    print("boleni yoxdur")


# 3. Bir int tipli dəyişən götürün və fibonaçi seriyasının bu həddəki qiymətini tapın.
# (Fibonaççi seriyası: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 və s. Birinci və ikinci həddin qiyməti 1,
# 3-cü həddən başlayaraq hər hədd özündən əvvəlki iki həddin cəminə bərabərdir.)

n = int(input())
a = 1
b = 1

for i in range(3, n+1):
    a,b = b, a+b

print(b)

###############################

n = int(input())
a = 1
b = 1

i = 3
while i < n+1:
    a, b = b, a+b
    i += 1

print(b)    


# 4. Daxil olunmuş ədədin armstronq olub-olmadığını yoxlayın.
# (Armstronq ədəd: , burada qüvvət üstü rəqəmlərin sayına bərabərdir.)

a4 = int(input())

x = 0

for i in str(a4):
    x += int(i)**len(str(a4))
    
if a4 == x:
    print(f"{a4} armstronq ededdir")     
else:
    print(f"{a4} armstronq eded deyil") 

#####################################   

a4 = int(input())
x = 0

i = 0
while i < len(str(a4)):
    x += int(str(a4)[i])**len(str(a4))
    i +=1

if a4 == x:
    print(f"{a4} armstronq ededdir")
else:
    print(f"{a4} armstronq eded deyil")   


# 5. İki list dəyişəni götürün. Birinci listdə olub, ikinci listdə olmayan elementləri yeni bir
# listə yığıb çapa verin.

list51 = []
a5 = int(input())

for i in range(a5):
    b5 = input()
    list51.append(b5)

print(list51)

list52 = []
a6 = int(input())

for j in range(a6):
    b6 = input()
    list52.append(b6)

print(list52)    

list53 =[]

for i in list51:
    if i not in list52:
        list53.append(i)

print(list53)

########################################

list51 = []
a5 = int(input())

i = 0
while i < a5:
    b5 = input()
    list51.append(b5)
    i += 1

print(list51)

list52 = []
a6 = int(input())

i = 0
while i < a6:
    b6 = input()
    list52.append(b6)
    i += 1

print(list52)    


list53 = []

i = 0
while i < len(list51):
    if list51[i] not in list52:
        list53.append(list51[i])
    i += 1

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

############################################    

matrix = []
n = int(input())

i = 0
while i < n:
    m = int(input())
    List1 = []
    j = 0
    while j < m:
        c = int(input())
        List1.append(c)
        j += 1
    matrix.append(List1)
    i += 1

print(matrix)  

i = 0
while i < len(matrix):
    x =matrix[i]
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

max = matrix[0][0]

for i in matrix:
    for j in i:
        if j > max:
            max = j

print(max)

#############################################

matrix = []
n = int(input())

i = 0
while i < n:
    m = int(input())
    List1 = []
    j = 0
    while j < m:
        c = int(input())
        List1.append(c)
        j += 1
    matrix.append(List1)
    i += 1

print(matrix)

max = matrix[0][0]

i = 0
while i < len(matrix):
    x = matrix[i]
    j = 0
    while j < len(x):
        if x[j] > max:
            max = x[j]
        j +=1            
    i += 1

print(max)


# 8. Elementləri int tipli olan bir list dəyişəni götürün. Bu listin elementlərinin qiyməti
# qədər “*” çap edin.
# (Məs: [1, 5, 3, 2]
# *
# *****
# ***
# **
# )

list8 = []
a8 = int(input())

for i in range(a8):
    b8 = int(input())
    list8.append(b8)

print(list8)

for j in list8:
    print("*" * j)

########################

list8 =[]
a8 = int(input())

i = 0
while i < a8:
    b8 = int(input())
    list8.append(b8)
    i += 1

print(list8)

j = 0
while j < len(list8):
    print("*" * list8[j])
    j += 1








































