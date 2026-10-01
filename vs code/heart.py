import turtle
import colorsys

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
heart = turtle.Turtle()
heart.speed(0)
heart.pensize(2)
heart.hideturtle()

# Number of colors in the rainbow
colors = 100
hue = 0

# Draw multiple hearts to create glowing effect
for i in range(colors):
    heart.penup()
    heart.goto(0, 0)
    heart.pendown()
    
    # Convert HSV to RGB
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    heart.color(col)
    
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

    hue += 0.01
    heart.right(2)  # rotate a bit for spiral effect

# Keep window open
turtle.done()
