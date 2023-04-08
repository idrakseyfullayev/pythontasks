#### Input/Output ####

# input() ==> Konsoldan (terminaldan) qiymet almaq ucun istifade edilir
# input() funksiyasinin qiymeti str tipinde olur.
# meselen

# a1 = input()

# print(a1)


# print() ==> Konsola (terminala) qiymet capa vermek ucun istifade edilir.
# print() funksiyasinda stringler 3 formada formatlanir.
# 1. format() funksiyasindan istifade ederek:
# meselen

# ad = input()
# soyad = input()

# ve ya

# ad, soyad = input().split(" ")

# print("{} {}".format(ad, soyad)) # ve ya
# print("{0} {1}".format(ad, soyad))

# 2. % simvolundan istifade ederek
# meselen

# print("%s %s" % (ad, soyad)) 

# print("%d %d" % (ad, soyad)) 

# print("%f %f" % (ad, soyad)) 

# 3. f simvolundan istifade ederek
# meselen

# print(f"{ad} {soyad}")

# print funksiyasinin end ve sep parametrleri var.
# meselen

# print(ad, end=" ") # sonda bosluq qoyur
# print(soyad, end=",") # sonda vergul qoyur

# print(ad, soyad, sep=", ") # deyisenler arasinda vergul ve bosluq qoyur

