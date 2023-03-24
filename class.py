
#                                  ########  Class  ############        
                
class Person:
    ### Property ve ya Variable ### -  deyisenler bu cur adlanir adlanir
    # 1. static variable, class variable # - umumi xususiyyetli deyisenlerdir ve deyeri butun obyeklere eynidir.
    num_ears = 2
    has_eyes = True

    ### Method ve ya Behavior ####   funksiyalar bele adlanir

    # 2. dynamic varibale ve ya instance varibale ve ya object variable # - xususi xususiyyetli deyisenlerdir ve bu 
    # deyisenlerin her biri  her bir obyekte verilmis ayri-ayri deyeri ozunde saxlayir.
    
    # consttruction method ve ya init metod
    def __init__(self, id, name, surname, height, weight):  # dynamic deyisenlere qiymet vermek ucun yaradilir.
        self.id = id
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight

        print("obyekt yaradildi")

    def get_full_name(self, sep):
        return self.name.capitalize() + " " + sep +" " + self.surname.capitalize()

    def count_ears(self):
        return self.num_ears    

idrak = Person(1, "Idrak", "Seyfullayev", 1.70, 63 )        
adem = Person(2, "Adem", "Orucov", 1.70, 70)

print(f"{idrak.id} - {idrak.name} - {idrak.height} - {idrak.weight} - {idrak.num_ears} - {idrak.has_eyes} - {idrak.get_full_name('/')} - {idrak.count_ears()}")
print(f"{adem.id} - {adem.name} - {adem.surname} - {adem.height} - {adem.weight} - {adem.num_ears} - {adem.has_eyes} - {adem.get_full_name('/')}")



#####################################################################################################################

### Inhertance ### -  class-dan child class-larin torenmesi
#  1.Single Inheritance  (ana - child)
#  2 MUltilevel Inheritance (ana-child-childd-child......)
#  3 Hierarchic  Inheritance (ana
#                                 child 1
#                                       child 1.1
#                                       child 1.1...
#                                 child 2
#                                       child21......)
# 1.4 Multiple  Inheritance (ana   ana    ana)
#                                 child

### Polymorphism ###
# 1. method ve ya property overriding
#    ana class-da olan metod  ve ya property-nin child class-da adini saxlayib  statement ve ya deyerinin  deyisdirilmesi
# 2. metod overloading
#    ana ve child class-da metodun adi eyni, parametr sayi ferqli olur     

#######################################################################################


#### Abstraction ###

from abc import ABC, abstractmethod

class AbstractPerson(ABC):
    num_ears: int
    _num_hands: int
    __has_eyes: bool

    @abstractmethod
    def __init__(self): None
    @abstractmethod
    def __init__(self): None

class Person:
    num_ears = 2
    has_hands = True

    def __init__(self, id, name, surname,sex, age, nationality, education):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.education = education

        print("Person obyekti yaradildi")

    def get_fullname(self):
        return self.name +" " + self.surname

    def get_fullinfo(self):
        return f"{self.id}  - {self.name} - { self.surname} _ {self.age} _ {self.nationality} - {self.education}"


class Teacher(Person):
    has_bag = False
    def __init__(self, id, name, surname,sex, age, nationality, education, num_lesson=0):
        super().__init__(id, name, surname,sex, age, nationality, education)
        self.num_lesson = num_lesson

        print("Teacher obyekti yaradildi")

    def get_education(self):
        return self.education.title()

adem = Person(1, "Adem", "Orucov", "Kisi", 24, "azerbaycanli", "ali")
idrak = Teacher(2, "Idrak", "Seyfullayev", "Kisi",35, "azerbaycanli", "ali")

print(idrak.get_education())
print(idrak.get_fullname())


### Encapsulation ###

class Person:
    num_ears = 2      # public property - (her yerde cagirilir)
    _num_hands = 2    # protected property - (yalniz klassda ve child class-larda cagirilir)
    __has_eyes = True # private property - (yalniz ozunun aid oldugu class-da cagirilir)

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # def __get_fullname(self):
    #     return self.name + " " + self.surname + " " + self.num_ears + " " + self._num_hands
    @property
    def get_fullname(self):
        return self.name + " " + self.surname + " " + self.num_ears + " " + self._num_hands


    def get_fullinfo(self):
        return self.name + " " + self.surname + " " + self.age + " " + self.num_ears + " " + self._num_hands  + " " + self.__has_eyes

class Teacher(Person):
    def __init__(self, name, surname, age, num_lesson):
        super().__init__(name, surname, age)
        self.num_lesson = num_lesson

    def get_num_lesson(self):
        return self.num_lesson


idrak = Person("Idrak", "Seyfullayev", 35)
print(idrak._Person__has_eyes)
# print(idrak._Person__get_fullname)

print(idrak.get_fullname)




##### Decorators #####

## funksiya icinde funksiya teyin olunmasi ###
def topla (x,y):
    def pr():
        print("cem")
    return pr

a = topla(3,5)
a()


def topla (x,y):
    def pr():
        print("cem")
    return pr

a = topla
b = a(3,5)
b()    


def topla (x,y):
    def pr():
        print("cem")
    return pr

a = topla
a(3,5)()              


def topla (x,y):
    def pr():
        print("cem")
    return pr

a = topla(3,5)() 



## funksiya icinde funksiya cagirilmasi ###
def topla(func, x, y):
    print(func("Cem"), end="")
    return x+y

def my_f(a):
    return a+ ":"

print(topla(my_f, 15, 20))



def topla(func, x, y):
    print(func, end="")
    return x+y

def my_f(a):
    return a+ ":"

print(topla(my_f("Cem"), 15, 20))


def topla(func, x, y):
    return f"{func('Cem')}{x+y}"

def my_f(a):
    return a+ ":"

print(topla(my_f, 15, 20))


def topla(func, x, y):
    return func('Cem'), x+y

def my_f(a):
    return a+ ":"

print(topla(my_f, 15, 20))



## Decorators yaradilmasi ###
def dec(func):

    def inner_func():
        print("Funksiya cagirildi")
        print(func(5, 10))
        print("Funksiya icra olundu")
    return inner_func    

@dec
def topla(x, y):
    return x+y

topla()

print()

@dec
def cix(x, y):
    return x-y

cix()



def dec(func):

    def inner_func(x, y):
        print("Funksiya cagirildi")
        print(func(x, y))
        print("Funksiya icra olundu")
    return inner_func    

@dec
def topla(x, y):
    return x+y

topla(5, 10)

print()

@dec
def cix(x, y):
    return x-y

cix(5, 10)


### Generators ######

def my_generator():
    yield 1
    yield 2
    yield 3

for i in my_generator():
    print(i)    


def my_generator():
    for i in range(5):
        yield i

x = my_generator()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


def my_generator():
    for i in range(5):
        yield i

x = my_generator()

for i in range(5):
    print(next(x))





class Math:
    pi = 3.14
    e = 2.71

    def __init__(self, name, n):
        self.name = name
        self.n = n

    def __str__(self):
        return self.name    

    def topla(self, m):
        return self.n + m

    # method overloaded 
    # def topla(self, m, l):
    #     return self.n + m + l


    def bolenlerin_sayi(self):
        count = 0
        for i in range(1, self.n +1):
            if not self.n % i:
                count += 1
        return count

    def ebob(self):
        return None

    def __str__(self):
        return self.name


y = Math("y", 10)

a = y.topla(15)  # 25
b = y.bolenlerin_sayi()
print(a)
print(b)
print(y)
print(y.n)




    












