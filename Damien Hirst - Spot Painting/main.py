# Run "source myenv/bin/activate" in terminal to activate the virtual environment.

# Code for extracting Color from an image.jpg :
# import colorgram
# colors=colorgram.extract('image.jpg',30)
# rgb_colors=[]
# for color in colors: 
#     red=color.rgb.r
#     green=color.rgb.g
#     blue=color.rgb.b
#     color_tuple=(red,green,blue)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)

color_list=[ (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

# Creating the art:
import random
from turtle import Turtle,Screen
turtle=Turtle()
screen=Screen()
screen.title("Damien Hirst Spot Painting")
screen.colormode(255)
turtle.shape("arrow")
turtle.hideturtle()
for i in range(1,11):
    turtle.penup()
    turtle.setpos(-200,-200+50*(i))
    print(turtle.pos())
    turtle.pendown()
    for j in range(10):
        turtle.dot(20,random.choice(color_list))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
screen.exitonclick()

