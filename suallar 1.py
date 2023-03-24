# 8. İki str tipli dəyişən götürün. Əgər ikinci dəyişənin bütün simvolları birinci dəyişəndə
# varsa, bu dəyişənlərin birləşməsini, əks halda hər iki dəyişəni tərsinə birləşdirib çap
# edin.


# a81 = input()
# b82 = input()


# if b82 in a81:
#     print(a81 + b82)
# else:
#     print((a81 + b82)[::-1])






#  6. Bir list dəyişəni götürün. Bu listin ən böyük elementini çap edin.


# list61 = []


# for i in range(10):
#     a6 = int(input())
#     list61.append(a6)

# max = list61[0]

# for i in range(1, len(list61)):
#     if list61[i] > max:
#         max = list61[i]



# print(max)




# list61 = []
# a6 = int(input())

# for i in range(a6):
#     b6 = int(input())
#     list61.append(b6)

# list61.sort()
# print(list61[-1])






# 10. Bir list dəyişəni götürün. Əgər listdəki element 5-dən kiçikdirsə, onu kvadratı ilə, 5-ə
# bərabərdirsə, 2 misli ilə, 5-dən böyükdürsə, kubu ilə əvəz edin.


# list10 = []
# g = int(input())


# for i in range(g):
#     a10 = int(input())
#     list10.append(a10)



# for i in range(len(list10)):
#     if list10[i] < 5:
#         list10[i] = list10[i]**2
#     elif list10[i] == 5:
#         list10[i] = list10[i]*2
#     else:
#         list10[i] = list10[i]**3        

# print(list10)   







# list10 = []
# g = int(input())


# for i in range(g):
#     a10 = int(input())
#     list10.append(a10)



# for i in list10:
#     if i < 5:
#         list10[i] = list10[i]**2
#     elif i == 5:
#         list10[i] = list10[i]*2
#     else:
#         list10[i] = list10[i]**3        

# print(list10) 



################################



# a = int(input())
# b = int(input()) 
# c = int(input())
# d = int(input())

# list = [a, b, c, d]

# print(list)




##################################

# 11.Listin elementlerinin sade ve ya murekkeb oldugunu yoxla.


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


#####   0 ve 1 daxil edende onlari da cixardir
#########################################################        




# # 5. İki int tipli a və b dəyişəni götürün. a və b aralığında mükəmməl ədədləri çapa verin.
# # (Bütün bölənlərinin cəminə bərabər olan ədəd mükəmməl ədəddir. Məs: 6 = 1+2+3
# # və s.)


# a = int(input())
# b = int(input())

# for i in range(a+1, b):
#     c = 0
#     for j in range(1, i):
#         if not i % j:
#             # print(j)
#             c += j
#     if c == i:
#         print(i)   



###################################################################################


# def topla(*args):
#     a = 0
#     for i in args:
#         a += i
#         return(a)  # burda niye 3 cap olundu??????????????????????????
# print(topla(3, 5, 8, 9))



# my_list = [12, 65, 54, 39, 102, 339, 221,]

# for i in my_list:
#     if not i % 13:
#         print(f"{i} ededi 13-e bolunur") # burda nece bu sekilde yazim???????????
# #                                        # 65, 39, 221 ededleri 13-e bolunur#




print(list(map(lambda n: n, range(10))))

print(list(filter(lambda n: n, range(10))))



print(list(map(lambda n: n > 5, range(10))))

print(list(filter(lambda n: n > 5, range(10))))




def my_function(n):
    if n > 5:
        return n

n = int(input())
print(list(filter(my_function, range(n))))


def my_function(n):
    return n > 5

n = int(input())
print(list(filter(my_function, range(n))))




def my_function(n):
    if n > 5:
        return n

n = int(input())
print(list(map(my_function, range(n))))


def my_function(n):
    return n > 5

n = int(input())
print(list(map(my_function, range(n))))






n = int(input())
print(list(filter(lambda n: 2**n, range(n))))     #  hetta bu halda 0- i da goturdu????????????

n = int(input())
print(list(map(lambda n: 2**n, range(n))))





def binary_2(n):
    for i in range(n, 0, -1):
        y = n % 2
        print(y)
        n //= 2
        if n == 0:
            break
        # burda print verende niye duz cap olunmur????

number = int(input())
binary_2(number)



def binary_recur(n):
    if n <=1:
        return "1"
    else:
        return binary_recur(n // 2)  +  str(n % 2)   # bu qaranliqdi mene??????????????


n = int(input())
print(binary_recur(n))






# Function to print binary number using recursion
# def convertToBinary(n):
#    if n > 1:
#        convertToBinary(n//2)
#    print(n % 2,end = '')

# # decimal number
# dec = int(input())

# convertToBinary(dec)
# print()  # bu qaranliqdi mene??????????????





class Math:
    pi = 3.14
    e = 2.71

    def __init__(self, name, n):
        self.name = name
        self.n = n

    def __str__(self):
        return self.name
    

    def ekob(self, t):
        return (self.n * t) / Mathchild.ebob(eded_2, t) #  mentiqi basa dusdum amma yazilis sadece bir az qaranliqdir???
        # return (self.n * t) / self.ebob(t) 2-ci forma

class Mathchild(Math):

    def __init__(self, ad, z):
        self.name = ad
        self.z = z

    def ebob(self, m):
        x = self.z 
        while x != m:
            if x > m:
                x = x - m
            else:
                m = m - x
        return x

eded_10 = Math("10", 10)
eded_1 = Mathchild("18", 5)
eded_2 = Mathchild("9", 15)

print(f"EKOB({eded_10.name},{45})={eded_10.ekob(45)}")



