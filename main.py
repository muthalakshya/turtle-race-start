from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
color = ["red", "orange", "purple", "blue", "pink", "green", "grey"]
y_postion = [-150, -100, -50, 0, 50, 100, 150]

all_turtle = []

for index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[index])
    new_turtle.goto(x=-230, y=y_postion[index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        distance = random.randint(1,10)
        turtle.forward(distance)
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


screen.exitonclick()