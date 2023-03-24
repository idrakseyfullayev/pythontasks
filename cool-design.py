# from turtle import *

# bgcolor('black')

# speed(0)

# hideturtle()

# for i in range(120):

#     color("red")
#     circle(i)
#     color("orange")
#     circle(i*0.8)
#     right(3)
#     forward(3)
# done()    



# import turtle
# import colorsys
# t = turtle.Turtle()
# # turtle.tracer(1)
# turtle.Screen().bgcolor("black")
# t.pensize(2)
# t.speed(0)
# n =36
# h = 0
# for i in range(60):
#     c = colorsys.hsv_to_rgb(h,1,0.9)
#     h+=1/n
#     t.pencolor(c)
#     for i in range(4):
#         t.forward(i)
#         t.right(10*5)
#         t.left(10)
#     t.right(120)
# turtle.done() 








from turtle import*

import colorsys


bgcolor('black')

speed(0)
pensize(3)


hue = 0.0


for i in range(300):
    color = colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    hue +=0.005
    right(i)
    circle(50,i)
    forward(i)
    left(91)
done()    


# from turtle import*

# color = ['blue', 'red', 'green', 'blue', 'red', 'green']


# bgcolor('black')

# for x in range(720):
#     pencolor(color[x%6])
#     width(x//100 +1)
#     forward(x)
#     left(59)
#     speed(5000)
# done()    












