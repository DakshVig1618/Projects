from turtle import Turtle
import random
NUM = [10,-10]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = random.choice(NUM)
        self.y_move = random.choice(NUM)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
