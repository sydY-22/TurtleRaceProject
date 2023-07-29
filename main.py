import turtle as turt
from turtle import Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color(blue, red, "
                                                           "purple, yellow, green or orange): ")
colors = ["red", "purple", "blue", "yellow", "green", "orange"]
print(f"Your bet: {user_bet}")
finish_line = 230
all_turtles = []


def create_turtles():
    """Creates the turtles object instances."""
    y_axis = -100
    for index in range(0, 6):
        random_turtle = turt.Turtle(shape="turtle")
        random_turtle.color(colors[index])
        random_turtle.penup()
        random_turtle.goto(x=-225, y=y_axis)
        y_axis = y_axis + 30
        all_turtles.append(random_turtle)


create_turtles()

if user_bet:
    is_race_on = True

# Begins the race.
while is_race_on:
    for turtle in all_turtles:
        # ends the race if the turtle has reached the finishline.
        if turtle.xcor() > finish_line:
            is_race_on = False
            winning_color = turtle.pencolor()
            # display if the user won or lost the bet.
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
