from turtle import Turtle
import os
FILE = open("highscore.txt","r")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(FILE.read(os.path.getsize("highscore.txt")))
        FILE.close()
        self.goto(0,260)
        self.color("white")
        self.write(f"Score: {self.score}\tHighscore: {self.highscore}",align="center",font=("Arial",15,"bold"))
        self.hideturtle()

    def refresh(self):
        self.write(f"Score: {self.score}\tHighscore: {self.highscore}",align="center",font=("Arial",15,"bold"))

    def update_score(self):
        self.score += 1
        self.clear()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center",font=("Arial",15,"bold"))
