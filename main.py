from turtle import Turtle , Screen
import pandas
win = 0 
##working with csv
data = pandas.read_csv("50_states.csv")
States= data.state
State = States.to_list()
States = [i.lower() for i in State]
PositionX= data.x
PositionY = data.y
PositionX = PositionX.to_list()
PositionY = PositionY.to_list()

# working with turtle
Sc= Screen()
game_is_on= True

turtle1=Turtle()
Image = 'blank_states_img.gif'
Sc.addshape(Image)
turtle1.shape(Image)

Writer=Turtle()
Writer.hideturtle()
Writer.penup()
while game_is_on :
    Answer = Sc.textinput(title='next state' , prompt = "any other states ?").lower()
    for i in States :
        if i == Answer :
            Index = States.index(i)
            Writer.goto(x=PositionX[(Index) ], y = PositionY[Index])
            Writer.write(i , font = ("arial", 8 , "bold"))
            States.remove(i)
            PositionX.pop(Index)
            PositionY.pop(Index)
            win+=1
    if win == 50 :
        break
    if Answer == "exit" :
        Inknown = {"states" : States}
        Inknown=pandas.DataFrame(Inknown)
        Inknown.to_csv("you didn't know.csv")
        break




Sc.exitonclick()