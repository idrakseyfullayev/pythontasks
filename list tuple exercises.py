# list1 = [1, 2]

# list2 = list(2, 3)  # bu qaydada liste ancaq bir eded qiymet vermek olur ya bos olmalidir, ya da string tipli qiymet ?

# print(list2)

# list[0]

# list = [1, 2, 'salam', 4.5, True]

# Matrix = [[1, 2], [3, 4]]                  # iterable = coxelemetli deyisenler

# Matrix1 = Matrix[0][0]

# Matrix3 = Matrix1[0]

# print(Matrix3)  # Matrix listinin 1 ededini capa vermek ucun ancaq bu usul kecerlidir? yoxsa qisa yolu da vardir yani birbasa?


# print(list[0] + list[-1])


# list1 = list[:3] + list[3:]

# list1 = list[:3] * 3

# print(list1)


# list1 = [3, 2, 1, 4, 5, "kukla"]

# list2 = list1[-1:-6:-1]

# list3 = list1[2]

# list3 = list1[2:3]      # bunu niye list kimi capa verir?

# print(list3)



# print(len(list1))



# #append   # append object to the end of the list

# list1 = [45, -20, 13, 34, 50, -21]

# list1.append(4.5)

# print(list1.append(4.5))   

# print(list1)        #burda niye list1-in sonuna 2 defe 4.5 edidi artirildi?



# list2 = list1.append(4.5)

# print(list2)

# print(list1)

# print(len(list1))




# a = "salam"

# print(len(a))

# print(len(a[0:3]))





#remove    #Remove first occurrence of value     # Raises ValueError if the value is not present.

# list1 = [45, -20, 13, 34, 50, -21]

# list1.remove(4)

# print(list1.remove(4))

# print(list1)         #   burda da eyni sey oldu?


# list2 = list1.remove(-20)

# print(list2)

# print(list1)






# insert       #Insert object before index.


# list1 = [45, -20, 13, 34, 50, -21]

# list2 = list1.insert(5, "salam")

# list1.insert((0, "salam"), (1, "dam"))    # iki index e   nese elvae etmek?

# print(list2)

# print(list1)










# pop          # Remove and return item at index (default last).    # Raises IndexError if list is empty or index is out of range.

# list1 = [45, -20, 13, 34, 50, -21]

# list1.pop()

# print(list1.pop())

# print(list1)                 #burda da eyni seydi?


# k = list1.pop()

# k = list1.pop(3)

# print(k)

# print(list1)



# m = list1.pop(1)

# print(m)

# print(list1)






# extend             #Extend list by appending elements from the iterable.

# list1 = [45, -20, 13, 34, 50, -21]

# list2 = list1.extend("32")

# print(list2)

# print(list1)



# count        Return number of occurrences of value.

# list1 = [45, -20, 50, 13, 50, 34, 50, -21]

# k = list1.count(50)

# print(k)

# print(list1)



# index                # Return first index of value.  # Raises ValueError if the value is not present.

# list1 = [45, -20, 50, 13, 50, 34, 50, -21]


# k = list1.index(-21)

# print(k)

# print(list1)




# reverse          # (method) reverse: ()

# list1 = [45, -20, 13, 34, 50, -21]

# list2 = list1.reverse()

# list2 = list1[0:3].reverse()    # bele bir sey niye alinmir?

# print(list2)

# print(list1)

# list1 = list1[::-1]

# print(list1)




#sort                      # Sort the list in ascending order and return None.


# list1 = [45, -20, 13, 34, 50, -21]

# list2 = list1.sort()

# print(list2)

# print(list1)

# list2 = list1.sort(reverse=True)

# print(list2)

# print(list1)




# clear                         # (method) clear()

# list1 = [45, -20, 13, 34, 50, -21]

# list2 = list1.clear()     

# list2 = list1[0:6].clear()   # # bele bir sey niye alinmir?

# print(list2)

# print(list1)



#copy                                 # Return a shallow copy of the list.

# list1 = [45, -20, 13, 13, 34, 50, -21]

# list2 = list1.copy()

# list2 = list1       # ferq nedir ki burda?


# print(list2)









                                                 #tuple
# list1 = [2, 1, 0, 4, -5]

# list1[3] = 9

# print(list1)

# print(list1[3])


# tuple1 = (2, 1, 0, 4, 0, -5)                                                 

# tuple1[2] = 6

# print(tuple1[2])

# print(tuple1)

# tuple2 = tuple1.count(0)

# print(tuple2)

# tuple2 = tuple1.count(0)

# print(tuple2)

# tuple2 = tuple1.index(4)

# print(tuple2)


# tuple1 = (2, 1, 0, 4, 0, -5)  

# print(tuple1)

# list2 = list(tuple1)

# list2[3] = 20

# print(list2)



                              ## Ev tapşırıqları  Dərs 4. List/Tuple. ##



# 1. İki list dəyişəni götürün. Birinci listin ilk iki elementi ilə ikinci listin son üç elementinin
# cəmini tapın. Alınan listi tərs sıra ilə çapa verin.

list1 = [2, 5, 9, 11, 4]

list2 = [23, 41, 20, 14 , -1]

list3 = list1[0:2] + list2[2:]

list14 = []
list14.append(list1[0] + list2[0])

list3.reverse()

print(list3)





# 2. İki list dəyişəni götürün və onları nizamlayın (sort). Alınmış listlərin cəmini çapa verin.


list21 = [-3, 21, 44, 55, 23, 0 , -39,]    #burda string olsa error verir?

list22 = [7, -34, 6, 99]

list21.sort()

list22.sort()

print(list21 + list22)




# 3. Bir list dəyişəni götürün və həmin listə “Python” sözünün hər bir simvolunu əlavə
# edib çapa verin.

list31 = [" ", 4, 67, -1, "qubernator", 4]

list31.extend("Python")

print(list31)



# 4. İki list dəyişəni götürün. Birinci listi tərs sıra ilə nizamlayıb, ikinci listin son 3 elementi
# ilə toplayın. Alınan listi tərs sıra ilə nizamlayıb çapa verin.

list41 = [32, 67, 0, 1 ,3 ,2]

list42 = [-3, 45, 7, 9 ,6]

list41.sort(reverse=True)

list43 = list41 + list42[-4:-1]

list43.sort(reverse=True)

print(list43)





# 5. İki list dəyişəni götürün və birinci listdə ikinci listin ilk elementinin sayını tapın.

list51 = [3, 78, 44, 23, 44, 56]

list52 = [44, 22, 33, "salam"]

print(list51.count(list52[0]))






# 6. Üç list dəyişəni götürün. “a” simvolunu birinci listin 0-cı, ikinci listin sonuncu, üçüncü
# listin 5-ci indeksinə əlavə edin.

list61 = [3, "m", "l", "3", 9]

list62 = [89, 101, 100, 0, -90]

list63 = ["klon", 'Z', 4, 8, -4, 23, 55, 66]


list61.insert(0, "a")
list62.insert(5, "a")    # list62.insert(-1, "a")  niye axira elave etmedi?
list63.insert(5, "a")

print(list61)
print(list62)
print(list63)



# 7. Bir list dəyişəni götürün və bu listi başqa bir dəyişənə kopyalayın və bu listlərin
# cəminin tərsini yeni bir dəyişənə yazın. Alınmış listin elementlərini 1 element
# ötürərək çapa verin.



list71 = [-89, 38, 1001, 1987, 31, 3]

list72 = list71.copy()

list73 = list71 + list72

list73.reverse()

print(list73[0::2])




# 8. İki list dəyişəni götürün. Birinci listin ilk elementini, ikinci listin son elementini silin.
# Birinci listi tərs sıra ilə, ikinci listi düz sıra ilə nizamlayıb çapa verin.


list81 = [5, 14, -2, -1, 44, 0, 89, 1001, 99]

list82 = [202, 100, 67, 89, 34, 35, 89, 2]

list81.remove(5)    # ve ya list81.pop(0)

list82.remove(2)     # ve yalist82.pop(-1)


list81.sort(reverse=True)

print(list81)


list82.sort()

print(list82)






# 9. Bir tuple dəyişəni götürün. Bu dəyişənin sonuna yeni bir element əlavə edərək çapa
# verin.

tuple91 = (5, 56, 76, "salam")

list91 = list(tuple91)

list91.append("gelincik")   # veya   list91.insert(4, "gelincik")

print(list91)




# 10. İki tuple dəyişəni götürün. Onların cəmini yeni bir dəyişənə yazın. Alınmış yeni
# dəyişənin uzunluğunu çapa verin.


tuple101 = (-999, 888, "Idark", "motor")

tuple102 = ("seher", 4, 5)

tuple103 = tuple101 + tuple102

print(len(tuple103))



