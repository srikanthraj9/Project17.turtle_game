import random
from turtle import Turtle,Screen

game_on = False
screen = Screen()
screen.setup(500,400)
use_bet = screen.textinput(title="make your bet",
                           prompt="which color turtle is win the race 'red', 'green', 'blue', 'yellow', 'orange', 'purple' ")
color =['red', 'green', 'blue', 'yellow', 'orange', 'purple']
distance = [-100,-60,-20,20,60,100]
all_turtle = []


for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y=distance[turtle_index])
    all_turtle.append(new_turtle)

if use_bet:
    game_on = True

while game_on:
    for turtle in all_turtle:
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
        if turtle.xcor() > 230:
            game_on = False
            winner_color = turtle.pencolor()
            if winner_color == use_bet:
                print(f"you won the game,the winner is: {winner_color}",)
            else:
                print(f"you lose the game,the winner is: {winner_color}",)


screen.exitonclick()