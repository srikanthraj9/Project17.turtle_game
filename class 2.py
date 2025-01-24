from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def moving_forward():
    timmy.forward(10)
def moving_backward():
    timmy.backward(10)
def moving_right():
    timmy.right(10)
def moving_left():
    timmy.left(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()

screen = Screen()
screen.onkey(key="f",fun=moving_forward)
screen.onkey(key="b",fun=moving_backward)
screen.onkey(key="r",fun=moving_right)
screen.onkey(key="l",fun=moving_left)
screen.onkey(key="c",fun=clear)
screen.listen()
screen.exitonclick()