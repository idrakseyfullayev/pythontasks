# set1 = {1, 2, 3, 3, "alma", "armud", "alma"}

# print(set1)

# list1 = [1, 2, 3, 3, 5, 5, 1, 1]

# set1 = set(list1)

# list2 = list(set1)

# print(list2)


# print(list1)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set3 = set1 + set2   error olur

# print(set3)





# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set1.add(10)

# print(set1)





# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set1.remove(10)    #error verir

# print(set1)




# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set1.discard(19)

# print(set1)







# set1 = {10, 11, 21, 3}
# set2 = {2, 3, 4, 5}

# print(set1.pop())

# print(set1)






# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set1.update(set2)
# # set1.update(10)      #iterable olmadigindan error verdi?
# # set1.update({2, 5, 8, "salam"})
# # set1.update((1, 3, 5))
# # set1.update([3, 22, 7, -8])

# print(set1)






# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set3 = set1.union(set2)

# print(set3)






# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set3 = set1.intersection(set2)

# print(set3)







# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set1.intersection_update(set2)

# print(set1)






# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set3 = set1.difference(set2)

# print(set3)






# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 5}

# set1.difference_update(set2)

# print(set1)







# set1 = {1, 2, 3, 4, 56}
# set2 = {2, 3, 4, 5}

# set3 = set1.symmetric_difference(set2)

# print(set3)







# set1 = {1, 2, 3, 4, 56}
# set2 = {2, 3, 4, 5}

# set1.symmetric_difference_update(set2)

# print(set1)
# print(set2)







# set1 = {1, 2, 3}
# set2 = {1,2}
# set3 = {2, 3, 4, 5}
# set5 = {10, 4}

# a = set2.issubset(set1)

# print(a)

# b = set3.issubset(set1)

# print(b)








# set1 = {1, 2, 3}
# set2 = {1,2}

# c = set1.issuperset(set2)

# print(c)

# d = set2.issuperset(set1)

# print(d)






# set1 = {1, 2, 3}
# set2 = {1,2}
# set3 = {50, 45}

# j = set1.isdisjoint(set2)

# print(j)

# h = set1.isdisjoint(set3)

# print(h)



#                                        # Dərs 5. Set. Set metodları.ev tapsiriqlari


# 1. Bir set dəyişəni götürün. Bu dəyişənə ardıcıl olaraq iki element əlavə edib çapa verin.

set1 = {4, 7, 9}

set1.add(5)
set1.add(6)

print(set1)


set1 = {4, 7, 9}

set1.update((5, 6))

print(set1)





# 2. İki set dəyişəni götürün. Onların birləşməsi ilə kəsişməsini çapa verin.

set21 = {'salam', 2, 3}

set22 = {'salam', -4, 49, "ok"}

set23 = set21.union(set22)

set24 = set21.intersection(set22)

print(set23)

print(set24)




# 3. Bir set dəyişəni götürün. Bu dəyişəni başqa bir set dəyişəninə kopyalayın. Birinci seti
# təmizləyərək hər iki seti çapa verin.


set31 = {41, "Baki", -99, "Merakesh"}

set32 = set31.copy()

set31.clear()

print(set31)   # bu niye tuple kimi capa verildi?????   set = {}    set1 = set()

print(set32)



# 4. İki set dəyişəni götürün və onların birləşməsini, kəsişməsini, fərqini, simmetrik fərqini
# çapa verin.


set41 = {78, -67, 44, 55 ,66}
set42 = {-1, -2, -44, 44, 55, 78}

print(set41.union(set42))

print(set41.intersection(set42))

print(set41.difference(set42))

print(set41.symmetric_difference(set42))





# 5. İki set dəyişəni götürün. Birinci setin ikinci setin alt seti və super seti olub-olmadığını
# yoxlayın.


set51 = {0, -99, "Azerbaijan", "Iceri seher", 10, 99, 77}
set52 = {77, "Azerbaijan", 0}

alt_seti = set51.issubset(set52)

super_seti = set51.issuperset(set52)

print(alt_seti)

print(super_seti)







# 6. İki set dəyişəni götürün. Əvvəlcə bu setlərin kəsişməsi olub olmadığını yoxlayın. Sonra
# kəsişməsini çapa verin.


set61 = {"55", 55, 89, "89", 12, 'armud meyvesi'}   # tek dirnaqla da ..???????

set62 = {"alma", "armud meyvesi", 12, "89"}

print(set61.isdisjoint(set62))

print(set61.intersection(set62))




# 7. İki set dəyişəni götürün. Birinci setə ikinci seti əlavə edərək çapa verin.


set71 = {"stekan", 9, 8, 7, 0}

set72 = {0, "w", 1, 2, 3, 8, 7}

set71.update(set72)


print(set71)





# 8. Bir set dəyişəni götürün. Əvvəlcə setdən bir element silin. Sonra setə başqa bir
# element əlavə edərək çapa verin.



set81 = {"Elnur", "telefon", 23, -90, 89}

set81.discard(89)   # ve ya  set81.remove(89)


set81.add(99.99)

print(set81)






# 9. Üç set dəyişəni götürün. Birinci setdən bir element silin. İkinci setə bir element əlavə
# edin. Üçüncü setə bir neçə element əlavə edin. Birinci set ilə ikinci setin birləşməsini,
# birinci set ilə üçüncü setin kəsişməsini, birinci set ilə üçüncü setin fərqini çapa verin.


set91 = {"komputer", "Nou Camp", 89, 4, 3}
set92 = {4, "komputer", "Kim Cen In", 0, -23}
set93 = {12, 34, -900, 1000.5}

set91.discard(3)
set92.add("back end web dveloper")
set93.update(("tort", 4, 899.09,))


print(set91.union(set92))

print(set91.intersection(set93))

print(set91.difference(set93))




# 10. Bir list dəyişəni götürün və bu listdəki eyni elementləri ataraq çapa verin.

list1 = [12, -12, 90, -12, "Don Ki Xot", 'Don Ki Xot']

list1 = set(list1)

print(list1)


















































































































