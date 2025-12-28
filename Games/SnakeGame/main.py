from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

#Screen Setup
scr = Screen()
scr.tracer(0)
scr.title("Welcome to My Snake Game")
scr.bgcolor("black")
scr.setup(800,600)

#Create a snake
snake = Snake()
#Create Food
food = Food()
#Score Board
score = ScoreBoard()

#Controls
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")

#Game Loop
is_game_on = True
while is_game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 10:
        score.update_score()
        food.refresh()
        snake.grow(snake.segments[-1].position())
        if score.score > score.highscore:
            score.highscore = score.score
            # Open file
            file = open("highscore.txt", "w")
            file.write(f"{score.highscore}")
            file.close()
        score.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        is_game_on = False
        score.game_over()

    #Detect collision with the tail
    for i in range(1,len(snake.segments) - 1):
        if snake.head.distance(snake.segments[i]) < 2:
            is_game_on = False
            score.game_over()

scr.exitonclick()