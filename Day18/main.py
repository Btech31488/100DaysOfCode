from turtle import Turtle, Screen, right
from random import choice

tim = Turtle()
tim.shape("turtle")
colors = ["deep sky blue", "spring green", "orange red", "yellow", "blue", "magenta", "deep pink", "medium slate blue"]

# tim.color("deep sky blue")
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(choice(colors))
    draw_shape(shape_side_n)
    











screen = Screen()
screen.exitonclick()