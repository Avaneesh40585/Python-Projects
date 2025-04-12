from turtle import Turtle,Screen
turtle=Turtle()
screen=Screen()
screen.title("Etch-A-Sketch")

def move_forward():
    turtle.forward(10)
def move_backward():
    turtle.backward(10)
def rotate_clockwise():
    turtle.right(10)
def rotate_anti_clockwise():
    turtle.left(10)
def clear_sketch():
    turtle.reset()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=rotate_anti_clockwise)
screen.onkey(key="d",fun=rotate_clockwise)
screen.onkey(key="c",fun=clear_sketch)
screen.exitonclick()