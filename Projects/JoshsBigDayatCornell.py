# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

window = turtle.Screen()
window.bgcolor("black")
window.title("JoshsBigDayAtCornell")

# intro message
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("Welcome to Josh's Big Day at Cornell! He's going to school now",
              align="center", font=("Courier", 13, "bold"))

#updating window 
window.update()

# clear the message before the game starts
time.sleep(5)
message.clear()
#i had to look online on how to do this on reddit but i guess it worked lol
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("Oh no! Looks like good ol Josh forgot his homework",
			  align="center", font=("Courier", 16, "bold"))
window.update()
time.sleep(3)
message.clear()

message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("Son of a biscuit!",
              align="center", font=("Courier", 16, "bold"))
window.update()
time.sleep(3)
message.clear()
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("Josh arrived to Cornell and felt the disapproving eyes of his peers",
              align="center", font=("Courier", 13, "bold"))
window.update()
time.sleep(5)
message.clear()
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("His stomach dropped. His GPA trembled",
              align="center", font=("Courier", 13, "bold"))
window.update()
time.sleep(3)
message.clear()
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("He laughed nervously. His professor did not",
			  align="center", font=("Courier", 13, "bold"))
window.update()
time.sleep(3)
message.clear()
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("Josh LEAPT out the window! Run Josh run!!!!",
              align="center", font=("Courier", 13, "bold"))
window.update()
time.sleep(5)
message.clear()
message = turtle.Turtle()
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("use W, A, S, D to move",
			  align="center", font=("courier", 13, "bold"))
window.update()
time.sleep(3)
message.clear()
set_background("download (1)")

#creating the sprite
s1 = create_sprite("Josh2", -250, 0)

s1.penup()
s1.goto(-250, 0)



#obstacles
obstacles = []

# my variable (i wanted to name it something creative like 'pencils' yk cuz of the school theme but i couldn't figure out how)
lives = 3

# movement
def move_right():
    s1.setheading(0)
    s1.forward(5)

def move_left():
    s1.setheading(180)
    s1.forward(5)

def move_up():
    s1.setheading(90)
    s1.forward(5)

def move_down():
    s1.setheading(270)
    s1.forward(5)

window.listen()
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

# Game loop
timer = 0
while True:
    time.sleep(0.05)
    timer += 1

    # 
    if timer % 20 == 0:
         y_position = random.randint(-250, 250)
         s2 = create_sprite("teacher", 300,y_position)
         s2.setheading(180)
         obstacles.append(s2)

    # checking for collisions (bc i'm a responsible coder)
    for s2 in obstacles[:]:
        s2.forward(10)
        if s1.distance(s2) < 50:
            lives -= 1
            print(f"you lost a life! noooo. lives left: {lives}")
            s2.hideturtle()
            obstacles.remove(s2)


            if lives <= 0:
                print("Ugh u lost! Shucks")
                s1.hideturtle()
                for obs in obstacles:
                    obs.hideturtle()
                window.update()
                break
#this makes the teacher disappear if it goes past the -300 point on the grid
#i also looked on reddit how to do this, i hope that's ok since at least i didn't use AI
        elif s2.xcor() < -300:
            s2.hideturtle()
            obstacles.remove(s2)

    window.update()

    # exit if no lives left ahhh all done yay!
    if lives <= 0:
        break