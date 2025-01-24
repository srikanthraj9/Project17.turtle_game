from turtle import  Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def move_forward():
    timmy.forward(10)
screen = Screen()
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()