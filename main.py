import turtle

def draw_colorful_spiral(speed, iterations, colors, angle, width_start, width_increment, length_increment, start_x, start_y, shape):
    # Create a turtle object
    t = turtle.Turtle()

    # Set the speed of the turtle
    t.speed(speed)

    # Set starting position
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    # Set the shape of the turtle
    t.shape(shape)

    # Draw a colorful spiral
    for i in range(iterations):
        t.pencolor(colors[i % len(colors)])
        t.width(width_start + i * width_increment)
        t.forward(i * length_increment)
        t.left(angle)

    # Hide the turtle and display the drawing
    t.hideturtle()
    turtle.done()

# Customize the drawing by changing these parameters
speed = 0            # Speed of the turtle 
iterations = 36000000     # Number of iterations to draw the spiral
colors = ['red', 'orange']  # List of colors to use
angle = 180           # Angle to turn
width_start = 1      # Starting width of the pen
width_increment = 0.1  # Increment of the pen width
length_increment = 1  # Increment of the length of each side
start_x = 0          # Starting x-coordinate
start_y = 0          # Starting y-coordinate
shape = "triangle"     # Shape of the turtle

# Call the draw_colorful_spiral function with the specified parameters
draw_colorful_spiral(speed, iterations, colors, angle, width_start, width_increment, length_increment, start_x, start_y, shape)
