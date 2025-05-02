import turtle, time, random, os

def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def create_sprite(image_filename, x=0, y=0):
    image_path = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    if not os.path.exists(image_path):
        print(f"Error: Image '{image_filename}.gif' not found!")
        return None  # Return None if the file isn't found
    
    screen = turtle.Screen()
    screen.register_shape(image_path)
    sprite = turtle.Turtle()
    sprite.shape(image_path)
    sprite.penup()
    sprite.goto(x, y)
    return sprite


# Section 2 - Variables
x1 = -250
y1 = 200
x2 = -250
y2 = 50
x3 = -250
y3 = -80
x4 = -250
y4 = -210

# Section 3 - Setup
set_background("coding wallpaper")
t1 = create_sprite("hamster", x1, y1)
t2 = create_sprite("capybara", x2, y2)
t3 = create_sprite("snail", x3, y3)
t4 = create_sprite("bunny", x4, y4)


# Section 4 - Racing 
for i in range(120):
    x1 += random.randint(1, 5)  
    x2 += random.randint(2, 6)
    x3 += random.randint(1, 4)  # slowest because its the snail lol see what i did there
    x4 += random.randint(3, 6)  # fastest because you know bunnies are fast so
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)    
    time.sleep(0.1)

# Section 5 - Winner yayayaya they should get a prize or something
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")

print("The race is done! Yay!")

# Finish the turtle graphics by saying it's done
#help this took me like 2 hours to do i had to resize every image using a photo editor and other stuff lol
turtle.done()