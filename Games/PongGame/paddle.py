from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()

    def up(self):
        new_y = self.ycor() + 20
        # upper boundary
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        # lower boundary
        if new_y > -250:
            self.goto(self.xcor(), new_y)
