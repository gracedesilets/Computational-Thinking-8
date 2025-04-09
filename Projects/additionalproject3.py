import turtle

t = turtle.Turtle()
t.penup()
t.goto( -200,100 )
t.pendown()
t.speed(10)
t.setheading(90)
t.color("purple")
for i in range(3):
    t.forward(40)
    t.right(20)

turtle.exitonclick()