                                            ## set-in metodlari ##
# add             -   set -e ozunun mueyyen etdiyi yere add() -a yalniz bir qiymet vermekle hemin qiymeti set -e elave 
# set1.add(5)         # edirik ve none qaytarir. add() -a iterable yazsaq error verecek

# update          -   set -e iterable tipli deyisen elave etmek ucun update() -e iterable -i yaziriq ve none qaytarir 
# set1.update(set2)   # mes: set1.update({2, 5, 8, "salam"}) , set1.update((1, 3, 5)) , set1.update([3, 4, 7, 8]) .

# remove          -   set-den remove()-a yazdigimiz qiymeti silirik ve none qaytarir. Qiymet set-de 
# set1.remove(10)     # yoxdursa  KeyError: qiymet    capa verir.

# discard         -   set-den discard()-a yazdigimiz qiymeti silirik ve none qaytarir. Qiymet set-de
# set1.discard(10)    # yoxdursa set hec bir deyisiklik olmadan cap olunur.

# pop             -   pop() set -den rondom olaraq bir elememt silir ve hemin elementin qiymetini qaytarir.
# set1.pop()

# union           -   set1.union(set2) bu set-leri birlesdirir ve yeni bir set yaradir ki ya yeni bir deyisene 
# set3 = set1.union(set2)   # yazilmalidir ve ya  print  ediilmelidir.

# intersection    -   set3 = set1.intersection(set2) bu set-lerin kesismesini verir ve yeni bir set yaradir ki 
# set3 = set1.intersection(set2)   # ya yeni bir deyisene yazilmalidir ve ya  print  edilmelidir.

# intersection_update  -  set1.intersection_update(set2) bu set-lerin kesismesini birinci(set1) set-e menimsedir
# set1.intersection_update(set2)      # ve none qaytarir.

# difference      -    set1.difference(set2) birinci set-den ikinci set-de eyni olan elementler cixilir ve yeni bir 
# set3 = set1.difference(set2)      # set yaradir ki ya yeni bir deyisene yazilmalidir ve ya  print  edilmelidir.

# difference_update   -   set1.difference_update(set2) birinci set-den ikinci set-de eyni olan elementler cixilib 
# set1.difference_update(set2)   #  birinci(set1) set-e menimsedilir ve none qaytarir.

# symmetric_difference   -   set1.symmetric_difference(set2) bu set-lerde eyni olan elementler cixilir ve set-ler  
# set3 = set1.symmetric_difference(set2) # birlesdirilib yeni bir set yaradir ki ya yeni bir deyisene yazilmalidir 
                                         #  ve ya  print  edilmelidir.

# symmetric_difference_update   -   set1.symmetric_difference_update(set2) bu set-lerde eyni olan elementler cixilir
# set1.symmetric_difference_update(set2)    # ve set-ler birlesdirilib birinci(set1) set-e menimsedilir ve none 
                                            # qaytarir.

# issubset       -      set2.issubset(set1)  set2 set1-in alt coxlugudursa true, deyilse False verecek. Ya yeni bir
# a = set2.issubset(set1)   # deyisene yazilmalidr ve ya print edilmelidir.

# issuperset     -      set1.issuperset(set2)  set1 set2-in super coxlugudursa True, deyilse False verecek. Ya yeni
# c = set1.issuperset(set2)  # bir deyisene yazilmalidr ve ya print edilmelidir.

# isdisjoint     -      set1.isdisjoint(set2)  set-ler kesisirse False, kesismirse True verir. Ya yeni bir deyisene
# j = set1.isdisjoint(set2)   # yazilmalidr ve ya print edilmelidir.



                                   ## set metodlarinin formullari ##


set1 ={1, 2, 3}
set2= {2, 3, 4, 4, 8}

set1.add(5)
set1.update(set2)
set1.remove(10)
set1.discard(10)
set1.pop()
set3 = set1.union(set2)
set3 = set1.intersection(set2)
set1.intersection_update(set2)
set3 = set1.difference(set2)
set1.difference_update(set2)
set3 = set1.symmetric_difference(set2)
set1.symmetric_difference_update(set2)
a = set2.issubset(set1)
c = set1.issuperset(set2)
j = set1.isdisjoint(set2)


#### Set ####

# Setde indekslenme ve element sirasi yoxdur. Elemente muraciet etmek olmur. Eyni elementden yalniz birini saxlayir.

# Set metodlari
# add()
# remove()
# discard() 
# pop()
# copy()
# clear()
# update()
# union()
# intersection()
# intersection_update()
# difference()
# difference_update()
# symmetric_difference()
# symmetric_difference_update()
# issubset()
# issuperset()
# isdisjoint()