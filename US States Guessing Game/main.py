import turtle
import pandas

state_label=turtle.Turtle()
state_label.penup()
state_label.hideturtle()
state_label.speed("fastest")

screen=turtle.Screen()
screen.title("Guess the U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data=pandas.read_csv("50_states.csv")
state_names=states_data["state"].to_list()

guessed_states=[]

# Checking the Input:
switch=True
score=0
while switch==True:
    if(score==0):
        answer_state=screen.textinput(title="Guess the state", prompt="What is the state's name? / Type 'end' to quit")
    elif(score!=50):
        answer_state=screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name? / Type 'end' to quit")
        check=True
        while check:
            for guessed_state_name in guessed_states:
                if(answer_state.title()==guessed_state_name):
                    answer_state=screen.textinput(title=f"{score}/50 States Correct", prompt="Located input given, try something else instead / Type 'end' to quit")
                else:
                    check=False
    if(answer_state.title()=="End" or score==50):
        switch=False
    else:
        for state_name in state_names:
            if(answer_state.title()==state_name):
                state_row=(states_data[states_data["state"]==state_name])
                state_label.goto(state_row["x"].item(),state_row["y"].item())
                state_label.write(state_name)
                guessed_states.append(state_name)
                score+=1

missed_states=[state_name for state_name in state_names if state_name not in guessed_states]
missed_states_df=pandas.DataFrame(missed_states)
missed_states_df.to_csv("missed_states.csv", mode='w',index=False,header=False)

# * Old Logic without List Comprehension:
# missed_states=[]
# for state_name in state_names:
#     if state_name not in guessed_states:
#         missed_states.append(state_name)
            
# * Function to get the co-ordinates of the location on Terminal upon mouse-click on Screen:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
