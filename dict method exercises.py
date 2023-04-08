# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }

# print(kitab["Sehife_sayi"])

# print(kitab["Reyciler"])


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




# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }





# Ad1 = kitab.get("Ad")
# Ad2 = kitab["Ad"]

# Ad1 = kitab.get("A1")     # hansi usul daha yaxsidir??????????
# Ad2 = kitab["A1"]

# print(Ad1)
# print(Ad2)







# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }



# kitab1 = kitab.items()

# print(kitab1)







# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }



# kitab1 = kitab.values()

# print(kitab1)






# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }


# kitab1 = kitab.keys()

# print(kitab1)









# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }


# print(kitab.pop("Ad"))

# print(kitab)







# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }


# kitab1 = kitab.pop("Ad")

# print(kitab)










# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }



# kitab1 = kitab.popitem()

# print(kitab1)

# print(kitab)








# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }


# kitab1 = kitab.setdefault("Qiymet", 5)

# kitab.setdefault("Qiymet", 5)

# print(kitab.setdefault("Sehife_sayi", 5))     # bu usul  key-in deyerini deyismir?

# # print(kitab1)

# print(kitab)

# print(kitab1)


# kitab = {
#     "Ad": "Oyunbaz",
#     "Muellif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }



# kitab["Qiymet"] = 5        # esasen bu istifade olunur!!!! 

# kitab1 = kitab["Qiymet"] = 5     
# 
# kitab["Reytinq"] = 5.5

# print(kitab["Qiymet"] = 5)      # niye error verir?????????
                               



# print(kitab1)

# print(kitab)

# print(kitab["Qiymet"])









# kitab = {
#     "Ad1": "Oyunbaz",
#     "Muellif": "Vulf Dorn",
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




# print(kitab.update(Film))      #   hem de yenileyir  dictinary-ni????????????


# print(kitab)
# print(Film)



# Dict = {}

# Dict1 = Dict.fromkeys("Salam", 5)

# print(Dict1)




# kitab = {
#     "Ad1": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }


# print(kitab.clear())

# print(kitab)



# kitab = {
#     "Ad1": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }


# kitab1 = kitab.copy()

# print(kitab1)

# print(kitab)






# kitab = {
#     "Ad1": "Oyunbaz",
#     "Muellfif": "Vulf Dorn",
#     "Sehife_sayi": 452,
#     "Reytinq": 4.7,
#     "Reyciler": ["Tom Hanks", "Chris Evans"]
# }



#                              #Dərs 6. Dictionary. Dictionary metodları. Ev tapşırıqları.

# 1. Bir dict dəyişəni götürün. Bu dəyişənə yeni elementlər əlavə edərək çapa verin.

Qarabag_fc = {
    "Mesqci": "Qurban Qurabanov",
    "Sponsor": "Azersun Holdinq",
    "Olke": "Azerbaycan",
    "UEFA reytinq pillsi": 66,
}


Qarabag_fc["Olke retinqi"] = 1

Qarabag_fc["Budcesi"] = 525000


print(Qarabag_fc)

print(f"{Qarabag_fc['Budcesi']} euro")






# 2. İki dict dəyişəni götürün. İkinci dicti birinci dictə əlavə edərək çapa verin.


Sirket = {
    "Ad": "CBS",
    "Teyinat":"Tikinti",
    "Temir_qiymeti": 10000 
}

Sirket_xidmeti = {
    "Temir_qiymeti": "Razilasma yolu ile",
    "Xidmet_qiymeti": 5000
}


Sirket.update(Sirket_xidmeti)

print(Sirket)






# 3. Bir dict dəyişəni götürün. Bu dəyişənin açarlarını (keys), qiymətlərini (values), və
# elementlərini (items) çapa verin.


Ev = {
    "Esyalar":[
        "televizor",
        "tozsoran",
        "soyuducu"
    ],
    "kitablar":(
        "Ana dili",
        "Riyaziyyat",
        "Cografiya"
    ),
    "Divar kagizinin rengi": "goy",
    "Mertebe sayi": 2
}

print(Ev.keys())
print(Ev.values())
print(Ev.items())







# 4. Bir dict dəyişəni götürün. Bu dəyişənin elementlərininin qiymətini get() metodundan
# istifadə edərək çapa verin.



Magaza_satis = {
    "Nokia": 120,
    "Sumsung": 1000,
    "Xiaomi": 1400
}

print(Magaza_satis.get("Nokia",))

print(Magaza_satis.get("Sumsung"))

print(Magaza_satis.get("Xiaomi"))






# 5. İki dict dəyişəni götürün. İkinci dicti təmizləyərək birinci dictə kopyalayın. Hər iki dicti
# çapa verin.


Futbol = {
    "Qapi": "tor",
    "Meydanca": "suni ot",
    "Uzunluq": 90,
    "Penalti": 11
}

Basketbol = {
    "Meydanca": "parket",
    "Sebet_hundurluk": 3.05,
    "Oyuncu_sayi": 5
}

Futbol = Basketbol.copy()

Basketbol.clear()


print(Futbol)

print(Basketbol)




# # 6. Bir dict dəyişəni götürün. Bu dəyişənin bütün elementlərini bir-bir silin.


Mekteb = {
    "Olke": "Azerbaycan",
    "Seher": "Sumqayit",
    "Nomre": 25,
    "Istiqamet": "Pilot"
}

Mekteb.pop("Olke")
Mekteb.pop("Seher")
Mekteb.pop("Nomre")
Mekteb.pop("Istiqamet")

print(Mekteb)




# 7. Bir dict dəyişəni götürün və dəyişənə setdefault() metodundan istifadə edərək
# elementlər əlavə edin.

Universitet = {
    "Ad": "AzDIU"
}

Universitet.setdefault("Seher", "Baki")
Universitet.setdefault("Yerlesme_yaxinligi", "Ganclik metrosu")
Universitet.setdefault("Yaranma_tarixi", 1930)


print(Universitet)






# 8. Bir dict dəyişəni götürün və fromkeys() metodundan istifadə edərək bu dictə
# elementlər əlavə edin.


Herfler_oyunu = {}

Herfler_oyunu = Herfler_oyunu.fromkeys("Alifba", 99)

print(Herfler_oyunu)

















