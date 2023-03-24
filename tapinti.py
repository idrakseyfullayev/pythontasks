# matrix= []
# n = int(input())

# for i in range(n):
#     m = int(input())
#     List1 = []
#     for j in range(m):
#         c = int(input())
#         List1.append(c)
#     matrix.append(List1)

# print(matrix)



# matrix= []
# n = int(input())

# for i in range(n):
#     m = int(input())
#     List1 = []
#     for j in range(m):
#         List1.append(int(input()))
#     matrix.append(List1)

# print(matrix)



# matrix = []

# for i in range(int(input())):
#     list1 = [int(input()) for j in range(int(input()))]
#     matrix.append(list1)

# print(matrix)




# matrix = [int(input()) for i in range([int(input()) for j in range(int(input()))])]
# print(matrix)





# my_list = [12, 65, 54, 39, 102, 339, 221,]
# List1 = []

# for i in my_list:
#     if not i % 13:
#         List1.append(i)

# for i in range(len(List1)-1):
#     print(List1[i], end=", ")

# print(f"{List1[-1]} ededleri 13-e bolunur")



# my_list = [12, 65, 54, 39, 102, 339, 221]
# list1 = []

# for i in my_list:
#     if not i % 13:
#         list1.append(str(i))
# list1 = ", ".join(list1)        
# print(list1, "edeleri 13-e bolunur")




# def pyramid(n):
#     for i in range(1, n+1, 2):
#         print(("*" * i).center(n))

# num = int(input())
# pyramid(num)



# def pyramid(n):
#     for i in range(1, n+1, 2):
#         x = ("*" * i).center(n)
#         y =" ".join(x)
#         print(y)

# num = int(input())
# pyramid(num)



# n = 5
# for i in range(1,n+1):
#     print("{}{}{}".format((" ")*(n-i),"*"*i,("*")*(i-1)))


# n = 5    
# for i in range(1,n+1):
#     print(f"{(' ')*(n-i)}{'*'*i}{'*'*(i-1)}")




# list1 = [1, 2, 4 , 6]
# list2 = [2, 4, 5]

# list3 = list(filter(lambda x: x not in list2,list1))

# print(list3)



# def check_srting_is_num(string1):
#     try:
#         float(string1) or int(string1)
#     except ValueError:
#         return "isn't num"
#     return "is num"        

# string1 ="11.5"
# print(check_srting_is_num(string1))

# list1 = ['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
# list2 = list(map(lambda x: x[0:-2], list1 ))
# print(list2)
# print("\n".join(list2))


# list1 = ['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
# print(list1)
# print("".join(list1))

# list1 = ['honda 1948', 'mercedes 1926', 'ford 1903']
# print("\n".join(list1))

# list1 = ['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
# print(list1)
# list2 = "".join(list1).split("\n")
# print(list2)
# print("\n".join(list2))



# list1 = ['honda 1948', 'mercedes 1926', 'ford 1903']
# print(list1)

# list2 = [i.strip(" 1948 1926 1903") for i in list1]
# print(list2)



# list1 = ['honda 1948', 'mercedes 1926', 'ford 1903']
# print(list1)

# list2 = list(map(lambda x: x.strip(" hondamercedesford"), list1))
# print(list2)
# print("\n".join(list2))


# string1 = "xosgeldiniz"
# string2 = string1.removeprefix("xos")
# print(string2)

# string1 = "xosgeldiniz"
# string2 = string1.removesuffix("iz")
# print(string2)

# string1 = "xosgel dinizx"
# string2 = string1.replace(" ", "")
# print(string2)

# string3 = "izxosgeldiniz"
# string4 = string3.strip("iz")
# print(string4)






# txt = ",,,,,rrttgg.....banana....rrr"

# x = txt.strip(",.grt")

# print(x)

# txt1 = "idrak|the terminal"

# y = txt1.strip("idrak|")
# print(y)


# x = "selam"
# print(x.replace("e","eb"))


# x = sum(i for i in range(6))
# print(x)


# num_of_lines = sum(1  for l in "salamat")
# print(num_of_lines)


# print(*["salam", "dunya"])

# print("\n".join(["salam","dunya"]))



# array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
# array_nums.sort(key=lambda i: 0 if i == 0 else -1 / i)
# print(array_nums)



