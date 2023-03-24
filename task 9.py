#                                             ###  for  ####  operatoru

# a, b = 10, 5

# a, b = b, a


# if a > b:
#     print(a)
# else:
#     print(b)


# print(a) if a > b else print(b)






# if a > b and a ==  10:
#     print(a)
# else:
#     print(b)


# print(a) if a > b and a == 10 else print(b)






# for i in range(1, 100):
#     print(i)



# for i in range(1, 100, 2):
#     print(i)



# for i in range(2, 100, 2):
#     print(i)


# sum = 0

# for i in range(0,100):   
#     # sum += i
#     x = 100-i
#     print(x)

# print(sum)



# sum = 0

# for i in range(2, 100, 2):
#     sum += i

# print(sum)



# sum = 0

# for i in range(1, 100, 2):
#     sum += i

# print(sum)




# text = "salam"

# for i in text:
#     print(i)




# str = "a"




# text = "salam"

# for i in range(len(text)):
#     print(text[i:])




# text = "salam"

# for i in range(len(text)):
#     print(text[0:len(text)-i])






# text = ""


# for i in range(10):
#     char = input()
#     text += char

# print(text)





# sum = 0

# for i in range(1,100):
#     if i % 2:
#         sum += i  

# print(sum)




# text = input()


# for i in range(len(text)):
#     print(text[:len(text)-i])




# list = []


# for i in range(5):
#     x = int(input())
#     list.append(x)

# print(list)    








#                           #### Dərs 8. Dövr operatorları (for). Ev tapşırıqları

# 1. Bir list dəyişəni götürün. Bu listin elementlərini terminaldan daxil edin. Sonra bu listin
# elementlərini aralarında vergül qoymaqla çap edin.

list1 = []

m = int(input())

for i in range(m):
    a = input()
    list1.append(a)

for i in list1:
    print(i, end=",")


# 2. 1-dən 100-dək ədədlərin kvadratları cəmini çapa verin.

a2 = 0

for i in range(1,100):
    a2 += i**2

print(a2)


# 3. Bir list dəyişəni götürün. Bu listin 5-dən böyük olan elementlərini çapa verin.

list31 = []

for i in range(5):
    a3 = int(input())
    list31.append(a3)

for i in list31:
    if i > 5:
        print(i, end=" ")


list32= []

for i in range(10):
    a3 = int(input())
    list31.append(a3)

for i in list31:
    if i >  5:
        list32.append(i)
    
print(list32)


# 4. Bir list dəyişəni götürün. Bu listin tək elementlərinin kvadratları ilə cüt elementlərinin
# kubları cəmini hesablayıb çapa verin.

list41 = []
t = int(input())
x41 = 0

for i in range(t):
    y = int(input())
    list41.append(y)


for i in list41:
    if i % 2:
        x41 += i**2
    else:
        x41 += i**3
        
print(x41)


# 5. İnt tipli a və b (a < b) dəyişənləri götürün. a və b aralığında 5-ə bölünen ədədlərin
# hasilini çap edin.

a = int(input())
b = int(input())
x = 1

for i in range(a+1, b):
    if not i % 5:
        x *= i
            
print(x)
        

# 6. Bir list dəyişəni götürün. Bu listin ən böyük elementini çap edin.

list61 = []

for i in range(5):
    a6 = int(input())
    list61.append(a6)

max = list61[0]

for i in range(1, len(list61)):
    if list61[i] > max:
        max = list61[i]

print(max)


# 7. Terminaldan daxil edilmiş ədədin faktorialını hesablayıb çap edin.
# Məs: 5! = 1*2*3*4*5 və s.

a7 = int(input())
x = 1

for i in range(2, a7+1):
    x *= i
    
print(x)


# 8. Terminaldan daxil edilmiş ədədi sadə və ya mürəkkəb olduğunu çap edin.

n = int(input())

for i in range(2, n):
    if not n % i:
        print("Eded murekkebdir")
        break
else:
    print("Eded sadedir")


# 9. For dövr operatorundan istifadə edərək, aşağıdakı fiquru çap edin.
# *
# **
# ***
# ****
# *****

a = int(input())

for i in range(1, a +1):           
    print("*"*i)


for i in range(1, 6):
    print("*" * i)


# 10. Bir list dəyişəni götürün. Əgər listdəki element 5-dən kiçikdirsə, onu kvadratı ilə, 5-ə
# bərabərdirsə, 2 misli ilə, 5-dən böyükdürsə, kubu ilə əvəz edin.

list10 = []
g = int(input())

for i in range(g):
    a10 = int(input())
    list10.append(a10)


for i in range(len(list10)):
    if list10[i] < 5:
        list10[i] = list10[i]**2
    elif list10[i] == 5:
        list10[i] = list10[i]*2
    else:
        list10[i] = list10[i]**3        

print(list10)        


# 11.Listin elementlerinin sade ve ya murekkeb oldugunu yoxla.

list1 = [143, 27, 17, 55]

for i in list1:
    for j in range(2,i):
        if not i % j:
            print(f"{i} murekkebdir")
            break
    else:
        print(f"{i} sadedir")    


# 12.############################################

text = ""

for i in range(10):
    char = input()
    text += char

print(text)


















