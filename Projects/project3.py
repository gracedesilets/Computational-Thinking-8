import turtle

#figuring out how to move the pen/getting started on code

t = turtle.Turtle()
t.color( "green" )
turtle.Screen().bgcolor( "pink" )
t.penup()
t.goto( 0,0 )
t.pendown()
t.speed(10)
for i in range(100):
    t.forward(38)
    t.left(23)

t.color( "yellow" )

t.penup()
t.goto( 0,0 )
t.pendown()
for i in range(100):
    t.forward(38)
    t.left(23)

t.color( "blue" )

#now making circles and looping them as well

t.penup()
t.goto( 0,0 )
t.pendown()

for i in range(100):
    t.forward(38)
    t.left(23)

t.color( "purple" )

t.penup()
t.goto( -50,50 )
t.pendown()

for i in range(100):
    t.forward(38)
    t.left(23)

t.color( "black" )

t.penup()
t.goto( 50,-50 )
t.pendown()

for i in range(100):
    t.forward(38)
    t.left(23)

#finally done yaayayay going to tell it how to end the program



turtle.exitonclick()