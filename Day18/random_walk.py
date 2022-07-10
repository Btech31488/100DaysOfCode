import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
t.colormode(255)
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.pensize(10)
tim.speed("fastest")
for x in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))












screen = t.Screen()
screen.exitonclick()