from turtle import Turtle, Screen
import random

is_race_on =False
screen = Screen()
user_bet = screen.textinput(title='Make you bet', prompt="Which turtle will win the race? Enter a color")
colors=['red','orange','yellow','green','blue','purple']
y_positions = [-250, -220, -190,-160,-130,-100]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-320, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:
    

    for turtle in all_turtles:
        if turtle.xcor() > 300:
            is_race_on=False
            winning_color =turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} won")
            else:
                print("you lost")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()