from turtle import Turtle

class Writer(Turtle):
    def __init__(self,state,x,y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state = state
        self.x_cor = x
        self.y_cor = y

    # displays user input on the map
    def display(self):
        self.goto(self.x_cor,self.y_cor)
        self.write(self.state,align="center",font=("Arial",10,"normal"))