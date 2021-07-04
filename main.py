import turtle
import pandas
import random

FONT = ("Courier", 30, "bold")
FONT1 = ("Courier", 15, "bold")
colors = ["MidnightBlue", "red", "dark violet", "chartreuse", "royal blue", "dark slate blue", "turquoise", "dim gray"]

screen = turtle.Screen()
screen.title("Indian States :)")
screen.setup(width=600, height=800)
my_turtle = turtle.Turtle()
screen.addshape("map.gif")
my_turtle.shape("map.gif")
my_turtle.seth(270)
my_turtle.penup()
my_turtle.goto(0, -80)
screen.listen()

write_turtle = turtle.Turtle()
write_turtle.hideturtle()
write_turtle.penup()
write_turtle.color("red")


# def get_mouse_click_coor(x,y):
#    print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("states.csv")

score = 0
def display_score():
    write_turtle.goto(0,360)
    write_turtle.color(random.choice(colors))
    write_turtle.write(f"Your total score was {score}/29", align="center", font=FONT)

guessed =[]
states = data.states.to_list()

while len(guessed) < 29:
    choice = screen.textinput(f"{score}/29 states correct", "Guess any state ?")
    if choice == None or choice == "exit":
        display_score()
        missing_states = [state for state in states if state not in guessed]
        new_data_frame = pandas.DataFrame(missing_states)
        new_data_frame.to_csv("states_to_learn.csv")
        break

    if choice.title() in states:
        score += 1
        row = data[data.states == choice.title()]
        x = float(row.x)
        y = float(row.y)
        write_turtle.color(random.choice(colors))
        write_turtle.goto(x, y)
        write_turtle.write(f"{choice.title()}",align="center",font=FONT1)
        guessed.append(choice.title())


turtle.mainloop()  #an alternative to exit on click method // scrren.mainloop() is also same.

