import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Number of gradient steps
steps = 90
hue = 0

# Draw heart-shaped curves forming a triangle
for i in range(steps):
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    
    # Rainbow color effect
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.color(col)
    
    pen.begin_fill()
    
    # Draw one side of the heart triangle
    pen.left(120)
    pen.forward(150)
    pen.circle(-50, 200)
    
    pen.left(140)
    pen.circle(-50, 200)
    pen.forward(150)
    
    pen.end_fill()
    hue += 1/steps
    pen.right(4)  # slight turn to spiral hearts inside triangle

# Hold the screen
turtle.done()
