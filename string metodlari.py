#                              #### Bool deyisenler ####
#
True (1), False (0)



#                              #### String metodlari ####
string1= "salam"
string1.capitalize()   # Birinci simvolu böyük hərflərə çevirir
string1.casefold()     # Sətri kiçik hərflərə çevirir
string1.center()       # Mərkəzləşdirilmiş sətri qaytarır
string1.count()        # Müəyyən edilmiş dəyərin sətirdə neçə dəfə baş verdiyini qaytarır
string1.encode()       # Sətirin kodlanmış versiyasını qaytarır
string1.endswith()     # Sətir müəyyən edilmiş dəyərlə bitərsə, doğru qaytarır
string1.expandtabs()   # Sətirin tab ölçüsünü təyin edir
string1.find()         # Müəyyən edilmiş dəyər üçün sətri axtarır və tapıldığı yeri qaytarır
string1.format()       # Sətirdə müəyyən edilmiş dəyərləri formatlayır
string1.format_map()   # Sətirdə müəyyən edilmiş dəyərləri formatlayır
string1.index()        # Müəyyən edilmiş dəyər üçün sətri axtarır və tapıldığı yeri qaytarır
string1.isalnum()      # Sətirdəki bütün simvollar alfasayısaldırsa, True qaytarır
string1.isalpha()      # Sətirdəki bütün simvollar əlifbadadırsa, True qaytarır
string1.isascii()      # Sətirdəki bütün simvollar ascii simvollarıdırsa, True qaytarır
string1.isdecimal()    # Sətirdəki bütün simvollar ondalıqdırsa, True qaytarır
string1.isdigit()      # Sətirdəki bütün simvollar rəqəmdirsə, True qaytarır
string1.isidentifier() # Sətir identifikatordursa, True qaytarır
string1.islower()      # Sətirdəki bütün simvollar kiçik hərfdirsə True qaytarır
string1.isnumeric()    # Sətirdəki bütün simvollar rəqəmlidirsə, True qaytarır
string1.isprintable()  # Sətirdəki bütün simvollar çap edilə bilərsə, True qaytarır
string1.isspace()      # Sətirdəki bütün simvollar boşluqdursa, True qaytarır
string1.istitle()      # Sətir başlığın qaydalarına əməl edirsə, True qaytarır
string1.isupper()      # Sətirdəki bütün simvollar böyük hərfdirsə, True qaytarır
string1.join()         # Təkrarlanan elementləri sətirə çevirir
string1.ljust()        # Sətirin sola əsaslandırılmış versiyasını qaytarır
string1.lower()        # Sətri kiçik hərflərə çevirir
string1.lstrip()       # Sətin sol trim versiyasını qaytarır
string1.maketrans()    # Tərcümələrdə istifadə ediləcək tərcümə cədvəlini qaytarır
string1.partition()    # Sətin üç hissəyə bölündüyü bir dəzgahı qaytarır
string1.replace()      # Müəyyən edilmiş dəyərin müəyyən edilmiş dəyərlə əvəz edildiyi sətri qaytarır
string1.rfind()        # Müəyyən edilmiş dəyər üçün sətri axtarır və tapıldığı yerin son mövqeyini qaytarır
string1.rindex()       # Müəyyən edilmiş dəyər üçün sətri axtarır və tapıldığı yerin son mövqeyini qaytarır
string1.rjust()        # Sətirin sağa əsaslanan versiyasını qaytarır
string1.rpartition()   # Sətin üç hissəyə bölündüyü bir dəzgahı qaytarır
string1.rsplit()       # Göstərilən ayırıcıda sətri bölür və siyahını qaytarır  
string1.rstrip()       # Sətin sağ trim versiyasını qaytarır
string1.split()        # Göstərilən ayırıcıda sətri bölür və siyahını qaytarır
string1.splitlines()   # Sətir fasilələrində sətri bölür və siyahı qaytarır
string1.startswith()   # Sətir müəyyən edilmiş dəyərlə başlayırsa, doğru qaytarır
string1.strip()        # Sətin kəsilmiş versiyasını qaytarır
string1.swapcase()     # Rəqəmləri dəyişdirir, kiçik hərf böyük hərf olur və əksinə
string1.title()        # Hər sözün ilk simvolunu böyük hərfə çevirir
string1.translate()    # Tərcümə edilmiş sətri qaytarır
string1.upper()        # Sətri böyük hərflərə çevirir
string1.zfill()        # Sətri əvvəlində müəyyən edilmiş 0 dəyəri ilə doldurur

# Note: All string methods returns new values. They do not change the original string.
# Qeyd: Bütün sətir metodları yeni dəyərləri qaytarır. Orijinal simli dəyişdirmirlər.

string1 = "xosgeldiniz"
string2 = (string1.removeprefix("xos"))
print(string2)

string1 = "xosgeldiniz"
string2 = (string1.removesuffix("iz"))
print(string2)

string1 = "xosgeldiniz"
string2 = (string1.replace("gel", ""))
print(string2)





