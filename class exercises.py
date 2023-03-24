class Car:
    number_wheel = 2
    number_steering_wheel = 1
    number_mirror =  2
    number_motor = 1

    def __init__(self, brand, color, category, salon_material, last_price): 
        self.brand = brand
        self.color = color
        self.category = category
        self.salon_material = salon_material
        self.last_price = last_price
        # self.superiority = superiority

    def summer_price_of_cars(self):
        return self.last_price    


car_1_mercedes_1 = Car("Mercedes 600", "black", "sedan", "skin", 9500)
car_2_toyota = Car("Toyota Prado", "white", "Hatchback", "cloth", 32500)
car3_prius = Car("Prius XW30", "Blue", "Liftback", "Skin", 14559)

print(f"brand:{car_1_mercedes_1.brand}, color:{car_1_mercedes_1.color}, category:{car_1_mercedes_1.category}, salon_material:{car_1_mercedes_1.salon_material}, last_price:{car_1_mercedes_1.last_price} ")
print(f"Brand:{car_2_toyota.brand}, Color:{car_2_toyota.color}, Category:{car_2_toyota.category}, Salon_material:{car_2_toyota.salon_material}, Last_price:{car_2_toyota.last_price}" )
print(f"Brand:{car3_prius.brand}, Color:{car3_prius.color}, Category:{car3_prius.category}, Salon_material:{car3_prius.salon_material}, Last_price:{car3_prius.last_price}")
print(f"Number of wheels Car1_Mercedes:{car_1_mercedes_1.number_wheel}")
print(f"Number of steering_wheel Car_2_Toyota:{car_2_toyota.number_steering_wheel}")
print(f"Number of motor Car_3_Prius:{car3_prius.number_motor}")
print(str(car_1_mercedes_1.summer_price_of_cars() + car_2_toyota.summer_price_of_cars() + car3_prius.summer_price_of_cars()) + " $")

###########################################################################################################################

class House:
    toilet = "have"
    bathroom = "have"
    kitchen = "have"
    gas = "have"
    water = "have"
    electric = "have"

    def __init__(self, type, category, area, land_area, number_rooms, extract, mortgage, address):
        self.type = type
        self.category = category
        self.area = area
        self.land_area = land_area 
        self.number_rooms = number_rooms
        self.extract = extract
        self.mortgage = mortgage 
        self.address = address


    def all_house_address(self, which_metro):
        return "Near "+ self.address + which_metro             
#                                                               

house_1 = House("Yard House", "Villa", 650, 6, 6, "Have not", "Have", "Narimanov street")
house_2 = House("Skyascaper", "Fifth floor", 400, 4, 3, "have", "have", "Nizami street")

print(f"House_1 - Type:{house_1.type}, Category: {house_1.category}, Area:{house_1.area} sq, Land_area:{house_1.land_area} sot")
print(f"House_2 - Type:{house_2.type}, Number_rooms:{house_2.number_rooms}, Extract:{house_2.extract}, Mortgage:{house_2.mortgage}, Address:{house_2.address}")
print(f"House_1 - Tolet:{house_1.toilet}, Bathroom:{house_1.bathroom}, Kitchen:{house_1.kitchen}")
print(f"House_2- Gas:{house_2.gas}, Water:{house_2.water}, Electric:{house_2.electric}")
print(f"All_House_address: {house_1.all_house_address('(Metro_Narimanov)')}, {house_2.all_house_address('(Metro_Iceri_Seher)')}")



##############################################################################################################################



class Woker:
    cambinzon_in_year = 2
    helmet_in_year = 1
    helmet_color = "blue"
    safety_glass_in_year = 1
    boot_in_year = 2
    jacet_in_year = 1
    canteen_entrance = "junior"
    vacation = "own expence"

    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname 
        self.position = position
        self.salary = salary

    def get_full_name(self):
        return f"{self.name.capitalize()} {self.surname.capitalize()}"


class ITW(Woker):
    vacation = "Company's expense"
    canteen_entrance = "Senior"
    helmet_color =  "White"

    def __init__(self, name, surname, position, salary, period_work):
        super().__init__(name, surname, position, salary)
        self.period_work = period_work

    def get_general_info_salary(self):
        return f"{self.name} {self.surname} : {self.position}, {self.salary}"

    def get_vacation_days(self):
        for i in range(1,11):
            if i == self.period_work:   
                return 22 + i*2

class Bonus_salary(ITW):  # bu qaydada child class yaradilmir toreme eyni tipden toremelidir
    
    # def __init__(self, name, surname, position, salary, vacation_days):
    #     super().__init__(name, surname, position, salary, vacation_days)

    days = int(input())   
    def salary_with_bonus(self, days):
        bonus = days*30
        return f"{self.get_full_name()}: Salary with bonus:{self.salary + bonus}"   


alik = Woker("Alik", "Yolcuyev", "Usta", 500)
zulfuqar = Woker("Zulfuqar", "Aliyev", "Fehle", 450)
nurlan = Woker("Nurlan", "Kazimov", "Bagban", 600)
idrak = Bonus_salary("Idrak", "Seyfullayev", "Foreman", 800, int(input()))
sahbaz = Bonus_salary("Sahbaz", "Xelilov", "Engineer", 1200, int(input()))
nebi = Bonus_salary("Nebi", "Seyfullayev","Junior Engineer", 700, int(input()))

print(f"{alik.get_full_name()} - Helmet color:{alik.helmet_color} - Boot in year:{alik.boot_in_year} - Canteen_entrance:{alik.canteen_entrance} - Vacation:{alik.vacation}")
print(f"{nebi.get_full_name()} - Cambinzon_in_year:{nebi.cambinzon_in_year} - Jacet_in_year:{nebi.jacet_in_year} - Helmet_color:{nebi.helmet_color} - Canteen_entrance:{nebi.canteen_entrance} - Vacation:{nebi.vacation}")
print(nebi.get_general_info_salary())
print(f"{nebi.get_full_name()} - Vacation_days:{nebi.get_vacation_days()}")
print(f"{idrak.get_full_name()} - Vacation_days:{idrak.get_vacation_days()}")
print(idrak.salary_with_bonus(int(input())))


#######################################################################################################################


# 1. Python Program to Get the Class Name of an Instance

# Nümunənin Sinif Adını Almaq üçün Python Proqramı
# Bu nümunədə siz nümunənin sinif adını almağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python Obyekt yönümlü proqramlaşdırma
# Python obyektləri və sinifləri


########### class adini  almaq??????????????

# Example 1: Using __class__.__name__

# class Vehicle:
#     def name(self, name):
#         return name

# v = Vehicle()
# print(v.__class__.__name__, end="")

# print(v.__class__.__dict__)


# __class__ əlaqəli olduğu sinfin atributudur və __name__ Python-da xüsusi dəyişəndir. Onun funksionallığı
# istifadə olunduğu yerdən asılıdır.
# Vehicle() sinifinin v obyekti yaradın.
# __class__.__name__ istifadə edərək sinfin adını çap edin.


# Example 2: Using type() and __name__ attribute

# class Vehicle:
#     def name(self,name):
#         return name

# v = Vehicle()
# print(v.__class__.__name__)





# 2. Python Program to Differentiate Between type() and isinstance()

# Type() və isinstance() arasında fərq qoymaq üçün Python proqramı
# Bu nümunədə siz type() və isinstance() arasında fərq qoymağı öyrənəcəksiniz.

# Bu nümunəni başa düşmək üçün aşağıdakı Python proqramlaşdırma mövzularını bilməlisiniz:

# Python obyektləri və sinifləri
# Python Obyekt yönümlü proqramlaşdırma
# Type() və instance() arasındakı fərq
# Aşağıdakı nümunə kodu ilə type() və instance() arasındakı fərqi anlayaq.


#  bu nedir bes   ?????????????????????????????????????????????????????????????????/

# class Polygon:
#     def sides_no(self):
#         pass

# class Triangle(Polygon):
#     def area(self):
#         pass

# obj_polygon = Polygon()
# obj_triangle = Triangle()

# print(type(obj_triangle) == Triangle)   	# true
# print(type(obj_triangle) == Polygon)    	# false

# print(isinstance(obj_polygon, Polygon)) 	# true
# print(isinstance(obj_triangle, Polygon))	# true

# print("Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


######################################################################################################################


class Vehicle_rent:
    __number_wheel = 10
    _material_wheel = "rubber"
    number_steering_wheel = 1
    number_mirror = 4
    _material = "metal"
    motor = True

    def __init__(self, type, num_passenger, price, brand, color, salon_material):
        self.type = type
        self.num_passenger = num_passenger
        self.price = price
        self.brand = brand
        self.color =  color
        self.salon_material = salon_material

    def get_brand_and_type_vehicle(self):
        return f"{self.brand} {self.type}"

    def get_info_vehicle(self, a="", b=","):
        return f"{a}Num_passenger:{self.num_passenger}{b} {a}Price:{self.price} azn{b} {a}Color:{self.color}{b} {a}Salon_material:{self.salon_material}"
    
    def rent_money(self, day):
        return day * self.price
    

class Car_rent(Vehicle_rent):
    __number_wheel = 4
    number_mirror = 2

    def __init__(self, type, num_passenger, price, brand, color, salon_material, category, transmission_guide):
        super().__init__(type, num_passenger, price, brand, color, salon_material)
        self.category = category
        self.transmission_guide = transmission_guide
    
    def get_info_vehicle(self, a="", b=","):
        return f"{a}Num_passenger:{self.num_passenger}{b} {a}Price:{self.price} azn{b} {a}Color:{self.color}{b} {a}Salon_material:{self.salon_material}{b} {a}Category:{self.category}{b} {a}Transmission_guide:{self.transmission_guide}"

    def rent_money(self, day):
        if self.category == "Sedan":
            return (day - (day*10/100) ) * self.price
        else:
            return day * self.price   
      

class Electric_Car_rent(Car_rent):
    motor = False
    def __init__(self, type, num_passenger, price, brand, color, salon_material, category, battery_capacity):
        super().__init__(type, num_passenger, price, brand, color, salon_material, category, None)
        self.battery_capacity = battery_capacity

    def get_info_vehicle(self, a="", b=","):
        return f"{a}Num_passenger:{self.num_passenger}{b} {a}Price:{self.price} azn{b} {a}Color:{self.color}{b} {a}Salon_material:{self.salon_material}{b} {a}Category:{self.category}{b} {a}Battery_capacity:{self.battery_capacity}{b} {a}Transmission_guide:{self.transmission_guide}"


class Motorbike(Vehicle_rent):
    __number_wheel = 2
    __number_steering_wheel = None
    number_mirror = 2               

    def __init__(self, type, price, brand, color, salon_material = False, num_passenger = None):
        super().__init__(type, num_passenger, price, brand, color, salon_material)               

bus_1 = Vehicle_rent("Bus", 30, 150, "Mitsubishi", "Red", "Cloth")
bus_2 = Vehicle_rent("Bus", 22, 100, "Ford", "Yellow", "Leather")
mercedes_1 = Car_rent("Car", 4, 130, "Mercedes 600", "Black", "Leather", "Sedan", "Automatic")
toyota_1 = Car_rent("Car", 4, 190, "Toyota Prado", "White", "Leather", "Hatchback", "Automatic")
pruis_1 = Electric_Car_rent("Car", 4, 70, "Prius XW30", "Blue", "Clothe", "Liftback", "18 Hours")
pruis_2 = Electric_Car_rent("Car", 4, 90, "Toyota Prius Review", "Bronze", "Leather", "Liftback", "24 Hours")
motorbike_1 = Motorbike("Motorbike", 60, "Suzuki", "Black")       
motorbike_2 = Motorbike("Motorbike", 85, "Isuzu", "Blue")

print(bus_1.get_brand_and_type_vehicle(), bus_1.get_info_vehicle("\n",""))     
print("%s %s" % (bus_2.get_brand_and_type_vehicle(), bus_2.get_info_vehicle('\n','')))
print(f"{mercedes_1.get_brand_and_type_vehicle()}- {mercedes_1.get_info_vehicle()}")
print(f"{pruis_2.get_brand_and_type_vehicle()}- {pruis_2.get_info_vehicle()}")
print(f"{motorbike_1.get_brand_and_type_vehicle()}- {motorbike_1.get_info_vehicle()}")

print(bus_1._Vehicle_rent__number_wheel)
print(motorbike_1._material_wheel)
print(bus_1.rent_money(10))
print(mercedes_1.rent_money(5))
print(toyota_1.rent_money(2))
print(pruis_2.rent_money(2))
print(motorbike_1.rent_money(20))


####################################################################################################################


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

    def bolenlerin_sayi(self):
        count = 0
        for i in range(1, self.n +1):
            if not self.n % i:
                count += 1
        return count

    def bolenleri_(self):
        str1 = ""
        for i in range(1, self.n+1):
            if not self.n % i:
                str1 += str(i) + ", "
        return (str1)       # burda print(i,end= " ")  verende qarisdi printe verdiyim netice
                
        
    # def ebob(self, m):
    #     while self.n != m:
    #         if self.n > m:
    #             self.n = self.n - m
    #         else:
    #             m = m - self.n
    #     return self.n             #  return self.n verende  asagida print(eded_10.n) = 5 olur eslinde 10 olmalidi idi??? 


    def ebob(self, m):
        x = self.n  #   burda deyisene yazdim duzeldi
        while x != m:
            if x > m:
                x = x - m
            else:
                m = m - x
        return x

    def ekob(self, t):
        return (self.n * t) / Math.ebob(self, t)  # eger bu class-da da coxlu obyekt olsa  idi onda nece taniyir self???
        # return (self.n * t) / self.ebob(t) 2-ci forma 
        

    def factorial(self):
        fact = 1
        for i in range(2, self.n+1):
            fact *= i
        return fact    

    def check_prime_composite_number(self):
        if self.n <= 0:
            return "isn't natural number"
        elif self.n ==1:
            return "neither a prime nor a composite number"    
        for i in range(2, self.n):
            if not self.n % i:
                return "a composite number"
        else:
            return "a prime number"        


    def check_perfect_number(self):
        sum_divisor = 0
        for i in range(1, self.n):
            if not self.n % i:
                sum_divisor += i           
        if sum_divisor == self.n:
            return "a perfect number"
        else:
            return "isn't a perfect number"            


    def check_square_number(self):
        if self.n**0.5 == int(self.n**0.5):
            return "a square number"
        else:
            return "isnt' a square number"  


    def calculate_circle_area_by_radius(self):
        return self.pi * self.n**2 
    
    def calculate_radius_by_circle_area(self):
        return (self.n / self.pi)**0.5   


    def calculate_arranged(self, z):
        arranged = 1
        for i in range(self.n-z+1, self.n+1):
            arranged *= i
        return arranged    


eded_10 = Math("10", 10)

print(f"""Eded_{eded_10} - 
Bolenlerin_sayi:{eded_10.bolenlerin_sayi()}
Bolenleri:{eded_10.bolenleri_()}
EBOB({eded_10.n},{35})={eded_10.ebob(35)}
EKOB({eded_10.name},{45})={eded_10.ekob(45)} 
Factorial_{eded_10}={eded_10.factorial()}
Eded_{eded_10}:{eded_10.check_prime_composite_number()} 
Eded_{eded_10}:{eded_10.check_perfect_number()}
Eded_{eded_10}:{eded_10.check_square_number()} 
Arranged({eded_10},{5})={eded_10.calculate_arranged(5)}""")

eded_10 = Math("10", 10)

print(f"Eded_{eded_10} - "
f"Bolenlerin_sayi:{eded_10.bolenlerin_sayi()}, "
f"Bolenleri:{eded_10.bolenleri_()} "
f"EBOB({eded_10.n},{35})={eded_10.ebob(35)}, " 
f"EKOB({eded_10.name},{45})={eded_10.ekob(45)} "
f"Factorial_{eded_10}={eded_10.factorial()}, "
f"Eded_{eded_10}:{eded_10.check_prime_composite_number()}, " 
f"Eded_{eded_10}:{eded_10.check_perfect_number()}, "
f"Eded_{eded_10}:{eded_10.check_square_number()}, "
f"Arranged({eded_10},{5})={eded_10.calculate_arranged(5)}")

print(eded_10.n)
print(eded_10.name)
print(eded_10)
print(eded_10.check_perfect_number())
print(eded_10.calculate_circle_area_by_radius())
print(eded_10.calculate_radius_by_circle_area())
print(eded_10.calculate_arranged(5))

Math.bolenlerin_sayi(eded_10)
print(Math.bolenlerin_sayi(eded_10))



####################################################################################################################



class Math:

    def __init__(self, name, n):
        self.name = name
        self.n = n

    def __str__(self):
        return self.name

    def bolenlerin_sayi(self):
        count = 0
        for i in range(1, self.n +1):
            if not self.n % i:
                count += 1
        return count

eded_10 = Math("eded_10", 10)
print(Math.bolenlerin_sayi(eded_10))
print(Math("eded_100", 100).bolenlerin_sayi())


################################################################################################



class Math:

    def __init__(self, name, n):
        self.name = name
        self.n = n

    def __str__(self):
        return self.name

    def bolenler(self):
        sum = 0
        for i in range(1, self.n):
            if not self.n % i:
                sum += i
                print(i)
        return sum

class Math_1(Math):

    def __init__(self, name, n):
        super().__init__(name, n)

    def perfect_num(self):
        if self.n == Math.bolenler(self):
            return "perfect number"
        else:
            return "is'nt perfect number"


eded_6 = Math_1("eded_6", 6)
print(eded_6.perfect_num())
print(Math_1("eded_50", 50).perfect_num())

##################################################################################################################




