#                                             ##### File handlig #####

# read - "r"
# write _ "w"
# append - "a"

# read and write - r+
# write and read - w+
# append and read - a+


## open file  for read ##

file = open("Python\Program\myfile.txt", "r")
data = file.read()
print(data)
file.close()


## open file for write ##

file = open("Python\Program\myfile.txt", "w")
data = file.write("ekwekkw")
print(data)
file.close()


## open file for append

file = open("Python\Program\myfile.txt", "a")
data = file.write(": I am a developr")
file.close()

file = open("Python\Program\myfile.txt", "r")
data = file.read()
print(data)



file = open("Python\Program\myfile.txt", "a+")
data = file.write("\ni am learing programming")
x = file.read()
print(x)
file.close()



file = open("Python\Program\myfile.txt", "r")
x = file.readlines(40)
print(x)
file.close()



### esasen bu qaydada istifade olunur ###
with open("Python\Program\myfile.txt", "a+") as file:
    data = file.write("\nalso")
    
with open("Python\Program\myfile.txt", "r") as file:
    data = file.read()    

print(data)



with open("Python\Program\myfile.txt", "w") as file:
    data = file.write("dunya")

with open("Python\Program\myfile.txt", "r") as file:
    data = file.read()

if data == "dunya":
    with open("Python\Program\myfile.txt", "a") as file:
        data = file.write(" salam")
    
with open("Python\Program\myfile.txt", "r") as file:
    data = file.read()    

print(data)

