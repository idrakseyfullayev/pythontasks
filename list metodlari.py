                                       ## list-in metodlari ##
# append  -    listin axirina append()-e yazdigimiz qiymeti elave edirik ve none qyatrir.
# list1.append(4.5)

# remove  -    listden remove()-a yazdigimiz qiymeti silirik ve none qaytarir.
# list1.remove(4)

# insert  -    listin necenci element sirasina qiymet daxil etmek ucun birinci indeksi sonra qiymeti yazirik 
# list1.insert(5, "salam")   # meselen: insert(0, "salam") ve none qaytarir.

# pop     -    default veziyyetde yani pop() listin element sirasindan axirinci elementi silir ve elemntin qiymetini 
# list1.pop()     # qaytrir ve yaxud pop()-a yazdigimiz indeksi listin element sirasindan silir ve elemntin qiymetini 
# list1.pop(3)    # qaytarir.

# extend  -    extend() -e daxil etdiyimiz iterable tipli deyiseni string kimi parcalayaraq listin axirina ayri-ayri
# list1.extend("53")    # elemenler(string kimi ' 5', '3') kimi elave edir ve none qaytarir.

# count   -     count() -a daxil etdiyimiz dəyərin baş vermə sayını qaytarır ve liste hec bir deyisiklik etmir.
# k = list1.count(50)

# index   -     index() -e daxil etdiyimiz deyerin indeksini qaytarir ve liste hec bir deyisiklik etmir.
# k = list1.index(-21)

# reverse -     reverse() listi tersine cevirir ve none qaytarir.
# list1.reverse()

# sort    -     sort() listi azdan coxa, sort(reverse=True) ise coxdan aza nizamlayir ve none qaytirir her iki halda.
# list1.sort()
# list1.sort(reverse=True)

# clear   -     clear() listi elementlerini tamamile silir ve none qaytarir.
# list1.clear()

# copy    -     copy() listin nusxesini yaradir ve yeni bir deyisene yazilmalidr ve hecne de qaytarmir.
# list2 = list1.copy()

# listin elementini deyismek ucun - meselen list[3] = 9  listde  3-cu element qiymeti   9 qiymeti ile evez olundu.
#     
# listde indeksi yazib qiymeti capa vermek ucun - meselen  print(list[5])  5-ci elementin qiymetni capa verir.

# iterble tipli deyisenin elemetlerinin sayi(uzunlugu) - meselen print(len(tuple103))


# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Qeyd: Python-da Massivlər üçün daxili dəstək yoxdur, lakin bunun əvəzinə Python Lists istifadə edilə bilər.


list1 = [2, 5, 9, 11, 4]

list2 = [23, 41, 20, 14 , -1]

tuple1 = (4, 5, 6)

list1.append(4.5)
list1.remove(4)
list1.insert(5, "salam")
list1.pop()
list1.pop(3)
list1.extend("53")
k = list1.count(50)
k = list1.index(-21)
list1.reverse()
list1.sort()
list1.sort(reverse=True)
list3 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list3.sort(key=lambda x: x[0])
list4 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
list4.sort(key=lambda x: x["color"])
list4.sort(key=lambda i: 0 if i == 0 else -1 / i)
list4.sort(key= lambda x: len(x))
list4.sort(reverse=True, key=lambda x: len(x)   )
list1.clear()
list2 = list1.copy()
list[3] = 9
print(list[5])
print(len(tuple1))




#### Lists/Tuples ####

# List metodlari

# append()
# insert()
# remove()
# pop()
# extend()
# reverse()
# sort()
# copy()
# clear()
# count()
# index()

# Cox elementli deyisenlerin uzunlugu(elementlerinin sayi) ==> len()
# list to tuple ==> tuple()
# tuple to list ==> list()

