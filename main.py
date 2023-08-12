import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U S A States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
#To get x,y coordinates of different states in usa but
# it is already given in blank_states_img.gif so no need to write this function

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another states name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states["state"] == answer_state]
        t.goto(int(state_data["x"]),int(state_data["y"]))
        t.write(answer_state)
missing_state = []
for state in all_states:
    if state not in guessed_state:
        missing_state.append(state)
new_data = pandas.DataFrame(missing_state)
new_data.to_csv("states_to_learn.csv")