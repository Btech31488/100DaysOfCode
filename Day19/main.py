from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backwards():
    tim.back(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    #or new_heading = tim.left(10)
    #tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    #or new_heading = tim.right(10)
    #tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(clear, "c")
screen.exitonclick()