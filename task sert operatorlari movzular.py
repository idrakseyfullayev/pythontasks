#                                       ### Sert operatorlari ###

# if    - qabaqinda muqayise operatorlu ifade ve ya deyisen olamalidir. if odenirse diger sertlere baxilmir!!!
# Kombinasiyada bir eded if ola biler. Amma if-n daxiline if ola biler. Teze setirdeki if yeni kombinasiyadi.

# elif  - qabaqinda muqayise operatorlu ifade ve ya deyisen olamalidir . elif odenirse diger sertlere baxilmir!!!
# Kombinasiyada istenilen sayda  elif ola biler.

# else  - qabaqinda hec bir ifade olmur. Diger sertlerin hec biri odenmirse else odenir!!!!
# Kombinasiyada bir eded else ola biler. Amma if ve ya elif-in daxilinde if ve ya elif-in ozunun else-si ola biler!

#                                       ### Mentiq operatorlari ###

# and   - her hansi bir teref odenmirse ifade  False olur. 
# or    - her hansi teref odenirse ifade  True olur.
# not   - True-nu False-a, False-i True-ya cevirir.


a = 7                                      
if a > 5:
    print("a 5-den boyukdur")
    a = 6
else: 
    print("a 5-den boyuk deyil")  

print(a)


a = 5                                      
if a > 5:
    print("a 5-den boyukdur")
    a = 6
else:
    print("a 5-den boyuk deyil")  

print(a)


a = 5
if a == 5:
    print("a 5-e bearberdir")
    a = 6
else:
    print("a 5-den boyuk deyil")    

print(a)


a = 5
if a < 5:
    print("a 5-den kicikdir")
    a = 3  

print(a)


a = 5
b = 15
if a > 4 and b > 12:
    print("a 5-den boyukdur")
    a = 1

print(a)


a = 5
b = 15
if a < 5 and b > 15:
    print("a 5-den kicikdir")
    a = 6 
elif a > 5 and b < 15:
    print(" a b-den boyukdur")
else:
    print( "beraberlik yoxdur")


a = 5
b = 15
if a < 5 and b > 15:
    print("a 5-den kicikdir")
    a = 6 
elif a == 5 and b < 17:
    print(" a = 5")
else:
    print( "beraberlik yoxdur") 


a = 5
b = 15
if a < 5 and b > 15:
    print("a 5-den kicikdir")
    a = 6 
elif a == 3 and b < 12:
    print(" a = 3")


a = 5
b = 15
if a < 5 and b > 15:
    print("a 5-den kicikdir")
    a = 6 
elif a == 3 and b < 12:
    print(" a = 3")
elif a == 5:
    print("5")


a = 5
b = 15
if a:
    print(a)


a = 5
b = 15
if b:
    print(a)


a = 5
b = 15
if print(a):
    print(a)


a = 0
b = 15
if a:
    print(a)


a = 0    # 0 = False oldugundan
b = 15
if a:  # burda if=False oldu
    print(a)  
# ve hecne cap olunmadi


a = 0  #  0 = False oldugundan
b = 15
if a and b:
    print(a)
elif not a: # not False-u True-ya cevirdi
    print(b) 
# 15 cap olunacaq


a = 0
b = 15
if a == 0 and b:
    print(a)
elif not a:
    print(b) 


a = 0
b = 15
if a and b:
    print(a)
elif b ==16:
    print(b)
elif b == 18:
    print(a+b)
else:
    print(a, b) 


a = 0
b = 15
if not (not a > b and b ==15):
    print("geldim")    


a = 0
b = 15
if not (not a > b or b ==15):
    pass  


a = 0
b = 15
if (not a > b or b ==15):
    print('salam')  


a = 0
b = 15
if not (not a < b or b <15):
    print("getdik")



###### ax*2 + bx + c

a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c

if D < 0:
    print(" tenliyin heqiqi koku yoxdur")
elif D == 0:
    x = (-b + D**0.5) / (2*a)
    print(x)
else:
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print(x1, x2)       




    