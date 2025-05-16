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
# Section 2: Setup
# TODO - create your player character
set_background("cornell")
s1 = create_sprite("Josh2", -250, 0)
s1.penup()
s1.goto(-250, 0)



# List of obstacles
obstacles = []

# Lives variable
lives = 3

# Obstacle creation


# Movement controls
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
    if timer % 30 == 0:
         y_position = random.randint(-250, 250)
         s2 = create_sprite("teacher", 300,y_position)
         s2.setheading(180)
         obstacles.append(s2)

    # Move obstacles and check collisions
    for s2 in obstacles[:]:
        s2.forward(10)
        if s1.distance(s2) < 50:
            lives -= 1
            print(f"💥 You lost a life! Lives left: {lives}")
            s2.hideturtle()
            obstacles.remove(s2)


            if lives <= 0:
                print("☠️ GAME OVER!")
                s1.hideturtle()
                for obs in obstacles:
                    obs.hideturtle()
                window.update()
                break

        elif s2.xcor() < -300:
            s2.hideturtle()
            obstacles.remove(s2)

    window.update()

    # Exit if no lives left
    if lives <= 0:
        break