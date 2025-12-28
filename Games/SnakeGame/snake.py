from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE = 10
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.grow(position)

    def grow(self, position):
        new_segment = Turtle(shape="circle")
        new_segment.penup()
        new_segment.shapesize(0.8, 0.8)
        new_segment.color("green")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)