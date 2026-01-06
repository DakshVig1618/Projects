from writer import Writer
from turtle import Screen
from score import Score
from tkinter import messagebox
import time
import pandas

# screen setup
scr = Screen()
scr.title("Welcome to K.Y.C (Know Your Country)")
scr.setup(width=800, height=600)

# map setup
scr.bgpic("india.gif")

# track guessed states
guessed_states = set()

# track score
score = Score()

data = pandas.read_csv("States and UT.csv")
TOTAL = len(data["Name"])

# main game loop
is_game_on = True
while is_game_on:
    time.sleep(1.0)

    # take input from the user
    state = str.title(scr.textinput(title=f"Score: {score.ACTUAL_COUNT}/{TOTAL}",prompt="Guess the State: "))
    if " And " in state:
        state = state.replace(" And ", " and ")

    if state in data["Name"].values:
        x_cor = data.loc[data[data.Name == state].index[0], "X"]
        y_cor = data.loc[data[data.Name == state].index[0], "Y"]
        if state not in guessed_states:
            # update the guessed state
            guessed_states.add(state)

            # display the guessed state on the map
            pen = Writer(state=state,x=x_cor,y=y_cor)
            pen.display()

            # update score
            score.update_score()
        else:
            # display message when one state is guessed more than once
            messagebox.showinfo("K.Y.C (Know Your Country)",f"You have already guessed '{state}'")
    else:
        # display message when invalid state
        messagebox.showinfo("K.Y.C (Know Your Country)", f"You have guessed an invalid state '{state}'")

    # end the game if all states are guessed successfully
    if len(guessed_states) == len(data["Name"].values):
        messagebox.showinfo("K.Y.C (Know Your Country)","You Won the game🥳\nYou have guessed all the States and UT's of India")
        is_game_on = False

scr.exitonclick()