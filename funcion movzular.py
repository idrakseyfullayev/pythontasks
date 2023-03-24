#                                            ###     Funksiyalar    ####  

# def funksiyasinin parametr goturme ardicilligi: # 

# def topla():        # def topla():
# positional:         # mövqeli:
#      required       # tələb olunan
#      optional       # isteğe bağlıdır
# none-positional     # mövqesiz
#      *args          # *args
#      **kwargs       # **kwargs    




a = 5
b = 10

def topla(a, b):
    c = a + b
    return c

x = topla(a, b)
print(x)



a = 5
b = 10

def topla(a,b):
    a += 1
    c = a + b
    print(c)

x = topla(a, b)    
print(x)



a = 5
b = 10

def topla(a,b):
    a += 1
    c = a + b
    return a, b, c

x = topla(a, b)
print(x)



a = int(input())
b = int(input())
c = int(input())

def kvadrat_tenlik(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D ==0:
        x = (-b) / (2*a) 
        return x  
    else:
        return "Helli yocdur"

print(kvadrat_tenlik(a, b, c))



def kvadrat_tenlik(a=1, b=1, c=1):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D ==0:
        x = (-b) / (2*a) 
        return x  
    else:
        return "Helli yocdur"

print(kvadrat_tenlik())



c =5

def kvadrat_tenlik(c, a=1, b=1):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D ==0:
        x = (-b) / (2*a) 
        return x  
    else:
        return "Helli yocdur"

print(kvadrat_tenlik(c))




# a = int(input())
# b = int(input())
# c = int(input())

# def kvadrat_tenlik(a=1, c, b=1,):  #  bele yazmaq olmaz !!!!!!!!!!!!!!!!!
#     D = b**2 - 4*a*c

#     if D > 0:
#         x1 = (-b + D**0.5) / (2*a)
#         x2 = (-b - D**0.5) / (2*a)
#         return x1, x2
#     elif D ==0:
#         x = (-b) / (2*a) 
#         return x  
#     else:
#         return "Helli yocdur"

# print(kvadrat_tenlik(a, c, b))




def kvadrat_tenlik(c, a=1, b=1):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D ==0:
        x = (-b) / (2*a) 
        return x  
    else:
        return "Helli yocdur"


print(kvadrat_tenlik(3,5))




c = float(input())

def kvadrat_tenlik(c, a=1, b=1,):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D ==0:
        x = (-b) / (2*a) 
        return x  
    else:
        return "Helli yocdur"

print(kvadrat_tenlik(c))



def topla(*args):
    a = 0
    for i in args:
        a += i
    return(a)  
       
print(topla(3, 5, 8, 9))




def topla(*args):
    a = 0
    for i in args:
        a += i
        return(a)  # burda niye 3 cap olundu
       
print(topla(3, 5, 8, 9))



def topla(*args):
    a = 0
    for i in args:
        a += i
        print(a)
       
print(topla(3, 5, 8, 9))



def topla(*args):
    a = 0
    for i in args:
        a += i
    print(a)
       
print(topla(3, 5, 8, 9))




def topla(**kwargs):
    a = 0
    for i in kwargs:
        a += kwargs[i] 
    return a    

print(topla(a=3, b=5, c=8,))




def topla(**kwargs):
    a = 0
    for i in kwargs:
        a += kwargs[i] 
        return a    

print(topla(a=3, b=5, c=8,))



def topla(**kwargs):
    a = 0
    for i in kwargs:
        a += kwargs[i] 
        print(a)   

print(topla(a=3, b=5, c=8,))



def topla(**kwargs):
    a = 0
    for i in kwargs:
        a += kwargs[i] 
    print(a)   

print(topla(a=3, b=5, c=8,))

