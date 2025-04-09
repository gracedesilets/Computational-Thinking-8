# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()
t.speed(10)
# repeat these next two lines  times
for i in range(10000):
    t.left(1)
    t.forward(1)




# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################

