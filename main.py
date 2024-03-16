import turtle

def draw_colorful_spiral(speed, iterations, colors, angle):
    # Create a turtle object
    t = turtle.Turtle()

    # Set the speed of the turtle
    t.speed(speed)

    # Draw a colorful spiral
    for i in range(iterations):
        t.pencolor(colors[i % len(colors)])
        t.width(i/100 + 1)
        t.forward(i)
        t.left(angle)

    # Hide the turtle and display the drawing
    t.hideturtle()
    turtle.done()

# Customize the drawing by changing these parameters
speed = 10            # Speed of the turtle (Make it 100 times faster)
iterations = 36     # Number of iterations to draw the spiral (lets add more iterations )
colors = ['red', 'orange', 'yellow',  ]  # List of colors to use (Add the colors of the Rainbow)
angle = 360         # Angle to turn (Lets change the angle so it can be spiral)

# Call the draw_colorful_spiral function with the specified parameters
draw_colorful_spiral(speed, iterations, colors, angle)
