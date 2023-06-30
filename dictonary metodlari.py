                                      ### dictionary-nin metodlari###
# get      - key -i kitab.get() -a daxil etdikde deyerini qaytarir. Eger hemin deyir dictionary-de yoxdursa
# Ad1 = kitab.get("Ad")         # none qaytarir. Ya yeni bir deyisene yazilmalidir ve ya print edilmelidr.

# Ad2 = kitab["Ad"] - key -i []-a daxil etdikde deyerini qaytarir. Eger hemin deyir dictionary-de yoxdursa
                                # error qaytarir. Ya yeni bir deyisene yazilmalidir ve ya print edilmelidr.

# items    - kitab.items() hem keyleri, hem de deyerleri qaytarir. Tuple -in daxilinde ayri-ayri lislerde qaytarir.  
# kitab1 = kitab.items()        # Ya yeni bir deyisene yazilmalidir ve ya print edilmelidir.

# keys     - kitab.keys() butun key -leri qayatrir. Tuple -in daxilinde qaytarir. Ya yeni bir deyisene yazilmalidir
# kitab1 = kitab.keys()         # ve ya print  edilmelidir.

# values   - kitab.values() butun deyerleri qaytarir. Tuple -in daxilinde qaytarir. Ya yeni bir deyisine yazilmalidir 
# kitab1 = kitab.values()       # ve ya print  edilmelidir.

# pop      - kitab.pop() -a daxil etdiyimiz key -i deyeri ile birlikde silir ve key -in deyerini qaytarir.
# kitab.pop("Ad")

# popitem  - kitab.popitem() dictionary -dan son key -i deyeri ile birlikde silir ve hem key-i, hem de deyeri  
# kitab.popitem()               # qaytarir.

# kitab["Qiymet"] = 5 - dictionary-ya key -i deyeri ile birlikde daxil edir ve ya hemin key movcuddursa deyerini 
                                # daxil etdiyimiz deyer vasitesile deyisirik. Esasen bu usul stifade olunur. 

# setdefault  - dictionary-ya key -i deyeri ile birlikde daxil edir, lakin hemin key movcuddursa dictionary-e
# kitab.setdefault("Qiymet", 5) -   # hec bir deyisiklik etmir ve amma her iki halda deyerleri qaytarir.

# update   - kitab.update(Film) birinci dictionary-ye ikinci dictonary elave olunur ve eyni key-ler varsa birinci 
# kitab.update(Film)            # dictionary-deki ortaq key-lerin deyeri ikinci dictionary-deki ortaq keylerin   
                                # deyeri ile evez olunur ve none qaytarir.

# fromkeys  -  Dict1 = Dict.fromkeys("Salam", 5) bu qaydada string parcalanir ve her herfi bir key olur ve her key-in 
# Dict1 = Dict.fromkeys("Salam", 5)    # deyeri daxil etdiyimiz deyer olur.

# clear     - kitab.clear()  dictionary-nin icin silir ozu qalir ve none qaytarir.
# kitab.clear()

# copy      - kitab1 = kitab.copy() bu qaydada kitab kitab1-e de nusxelenir.
# kitab1 = kitab.copy() 


                                   ### dictionary metodlarinin formullari ### 

# kitab = {
#     "Ad1": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }    


# Film = {
#     "Ad": "The Martian",
#     "Reytinq": 8.1,
#     "Rejissor": ["", ""],
#     "Aktyorlar": ["Mat Damon", ""],
#     "Sloqan": "jkjkj",
#     "Muellif": {
#         "Ad": "",
#         "Soyad": ""
#     }
# }


# Dict = {}

# Dict1 = Dict.fromkeys("Salam", 5)

# print(Dict1)


# Ad1 = kitab.get("Ad")
# Ad2 = kitab["Ad"]
# kitab1 = kitab.items()
# kitab1 = kitab.keys()
# kitab1 = kitab.values()
# kitab.pop("Ad")
# kitab.popitem()
# kitab["Qiymet"] = 5
# kitab.setdefault("Qiymet", 5)
# kitab.update(Film)
# Dict1 = Dict.fromkeys("Salam", 5)
# kitab.clear()
# kitab1 = kitab.copy()

# dictionary_one = {"a": 1, "b": 2}
# dictionary_two = {"c": 3, "d": 4}

# merged = {**dictionary_one, **dictionary_two}
# output {'a': 1, 'b': 2, 'c': 3, 'd': 4}



#### Dictionary ####

# Dictde indeksler acarlardir. Elementlerin sirasi movcuddur. Eyni acara aid olan elementlerden yalniz birini saxlayir.

# Dictdeki elementin qiymetini deyismek ve ya yeni element elave etmek :
# Dict["movcud_element"] = yeni_qiymet
# Dict["yeni_element"] = qiymet

# Dict metodlari

# setdefault()
# pop()
# popitem()
# clear()
# copy()
# update()
# items()
# keys()
# values()
# get()
# fromkeys()



# c = set({})
# print(type(c))



# kitab = {}

# print(type(kitab))



kitab = {
    "Ad": "Oyunbaz",
    "Muellif": "Vulf Dorn",
    "Sehife_sayi": 452,
    "Reytinq": 4.7,
    "Reyciler": ["Tom Hanks", "Chris Evans"], 
}


Film = {
    "Ad": "The Martian",
    "Reytinq": 8.1,
    "Rejissor": ["", ""],
    "Aktyorlar": ["Mat Damon", ""],
    "Sloqan": "jkjkj",
    "Muellif": {
        "Ad": "",
        "Soyad": ""
    }
}

# kitab.update(Film)
# print(kitab)


