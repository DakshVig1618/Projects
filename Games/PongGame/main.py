from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time

# screen setup
scr = Screen()
scr.bgcolor("black")
scr.setup(900,600)
scr.title("Welcome to PONG")

# paddle setup
scr.tracer(0)
paddle_r = Paddle()
paddle_r.goto(420,0)
paddle_l = Paddle()
paddle_l.goto(-420,0)

# scoreboard setup
scoreboard = Score()

# controls setup
scr.listen()
scr.onkeypress(paddle_r.up,"Up")
scr.onkeypress(paddle_r.down,"Down")
scr.onkeypress(paddle_l.up,"w")
scr.onkeypress(paddle_l.down,"s")

# ball setup
ball = Ball()

delay = 0.1
is_game_on = True
while is_game_on:
        time.sleep(delay)
        scr.update()

        # moving the ball
        ball.move()

        # detect collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        # detect collision with the right paddle
        if ball.x_move > 0 and ball.xcor() > 390:
            if paddle_r.ycor() - 50 < ball.ycor() < paddle_r.ycor() + 50:
                ball.setx(390)
                ball.paddle_bounce()
                delay = max(0.02, delay - 0.005)

        # detect collision with the left paddle
        if ball.x_move < 0 and ball.xcor() < -390:
            if paddle_l.ycor() - 50 < ball.ycor() < paddle_l.ycor() + 50:
                ball.setx(-390)
                ball.paddle_bounce()
                delay = max(0.02,delay - 0.005)

        # when ball surpasses any paddle
        if ball.xcor() > 450:
            scoreboard.l_point()
            ball.reset_ball()
            delay = 0.1
        if ball.xcor() < -450:
            scoreboard.r_point()
            ball.reset_ball()
            delay = 0.1


scr.exitonclick()
