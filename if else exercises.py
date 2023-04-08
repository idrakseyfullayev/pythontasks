
#  if # elif # esle    sert operatorlari

# a = 7



# if a > 5:
#     print("a 5-den boyukdur")
#     a = 6
# else:
#     print("a 5-den boyuk deyil")  

# print(a)






# a = 5

# if a == 5:
#     print("a 5-den boyukdur")
#     a = 6
# else:
#     print("a 5-den boyuk deyil")    


# print(a)






# a = 5


# if a < 5:
#     print("a 5-den boyukdur")
#     a = 6
# else:
#     print("a 5-den boyuk deyil")    


# print(a)







# a = 5

# if a < 5:
#     print("a 5-den boyukdur")
#     a = 6  


# print(a)







# and  # or    #not

# a = 5

# b = 15

# if a > 6 and b > 12:
#     print("a 5-den boyukdur")
#     a = 1



# print(a)







# a = 5

# b = 15

# if a < 5 and b > 15:
#     print("a 5-den kicikdir")
#     a = 6 
# elif a == 5 and b < 17:
#     print(" a = 5")
# else:
#     print( "beraberlik yoxdur")




# a = 5

# b = 15

# if a < 5 and b > 15:
#     print("a 5-den kicikdir")
#     a = 6 
# elif a == 3 and b < 12:
#     print(" a = 3")





# a = 5

# b = 15


# if a:
#     print(a)






# a = 5

# b = 15


# if b:
#     print(a)






# a = 5

# b = 15


# if print(b):
#     print(a)




# a = 0

# b = 15

# if a:
#     print(a)








# a = 0

# b = 15


# if a and b:
#     print(a)
# elif not a:
#     print(b)  






# a = 0

# b = 15


# if a == 0 and b:
#     print(a)
# elif not a:
#     print(b) 




# a = 0

# b = 15


# if a and b:
#     print(a)
# elif not a:
#     print(b)





# a = 0

# b = 15

# if a and b:
#     print(a)
# elif b ==16:
#     print(b)
# elif b == 18:
#     print(a+b)
# else:
#     print(a, b)        








# a = 0

# b = 15


# if not (not a > b and b ==15):
#     print("geldim")




# a = 0

# b = 15

# if not (not a < b and b ==15):
#     pass






# a = 0

# b = 15

# if not (not a > b and b ==15):
#     pass   






# a = 0

# b = 15

# if not (not a > b or b ==15):
#     pass   


# a = 0

# b = 15

# if (not a > b or b == 15):
#     print("salam")



# a = 0

# b = 15

# if not (not a < b or b <15):
#     print("getdik") 



####   ax*2 + bx + c

# a = int(input())

# b = int(input())

# c = int(input())

# D = b**2 - 4*a*c

# if D < 0:
#     print(" tenliyin heqiqi koku yoxdur")
# elif D == 0:
#     x = (-b + D**0.5) / (2*a)    #
#     print(x)
# else:
#     x1 = (-b+D**0.5)/(2*a)
#     x2 = (-b-D**0.5)/(2*a)
#     print(x1, x2)   




# list1 = [3, 4, 5]

# list2 = list1.copy()   #bu eyni   seydi???????????????

# # list2 = list

# print(list2)

# if a > 4:
#     if a < 2:     # niye error vermir?????
#         print(8)
    



#####  x**2 - 7x + 10 = 0   

# a = 1

# b = -7

# c = 10

# D = b**2 - 4*a*c

# if D > 0:
#     x1 = (-b + D**0.5) / (2*a)
#     x2 = (-b - D**0.5) / (2*a)
#     print("x1=", x1, "x2=", x2,)
# elif D == 0:
#     x1 = x2 = -b/(2*a)
#     print("%s=%s= %s" % ("x1", "x2",-b/(2*a)) )
# else:
#     print("tenliyin heqiqi koku yoxdur")






#####  x**2 + 4x + 4 = 0 

# a = 1

# b = 4

# c = 4

# D = b**2 - 4*a*c

# if D > 0:
#     x1 = (-b + D**0.5) / (2*a)
#     x2 = (-b - D**0.5) / (2*a)
#     print(x1, x2)
# elif D == 0:
#     x1 = x2 = -b/(2*a)  #  bu artiqdirmi???????????????????????
#     print("%s=%s=%s" % ("x1", "x2",-b/(2*a)) )
# else:
#     print("tenliyin heqiqi koku yoxdur")    





# a = int(input())

# b = int(input())

# c = int(input())


# D = b**2 - 4*a*c

# if D > 0:
#     x1 = (-b + D**0.5) / (2*a)
#     x2 = (-b - D**0.5) / (2*a)
#     print(x1, x2)
# elif D == 0:
#     x1 = x2 = -b/(2*a)  # bu artiqdirmi???????????????????????
#     print("%s=%s=%s" % ("x1", "x2",-b/(2*a)) )
# else:
#     print("tenliyin heqiqi koku yoxdur")  








#                        # Dərs 7. Sert operatorlari. Ev tapşırıqları.

# 9. int tipli a, b, c dəyişəni götürün. İf elif else operatorlarından istifadə edərək
# bunlardan ən kiçiyini k dəyişəninə yazaraq çapa verin.

# a = -42
# b = -78
# c = 65

# if a < b and a < c:
#     k = a
# elif b < c and b < a:
#     k = b 
# else:
#     k = c
    
# print(k)





# 10. int tipli a və b dəyişəni götürün. Əgər a b-dən böyükdürsə, a+b, a b-dən kiçikdirsə, a-
# b, a b-yə bərabərdirsə, a-nı çapa verin.

# a = 1001
# b = 2002

# if a > b:
#     print(a+b)
# elif a < b:
#     print(a-b)
# else:
#     print(a)        





