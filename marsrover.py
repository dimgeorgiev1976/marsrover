import turtle

# SETUP ROVER 1  (please do not change)
rover1 = turtle.Turtle()
rover1.color("pink")
rover1.penup()
rover1.goto(-150,-300)
rover1.pendown()
rover1.speed('slow')
rover1.left(90)

# SETUP ROVER 2  (please do not change)
rover2 = turtle.Turtle()
rover2.color("blue")
rover2.penup()
rover2.goto(0,-300)
rover2.pendown()
rover2.speed('slow')
rover2.left(90)

# Setup background (please do not change)
screen = rover1.getscreen()
screen.setup(1200,800)
screen.bgpic('craters.gif')
screen.update()

# ROVER POWER IS LIMITED VISIT ALL THE POINTS
# IN THE LEAST POSSIBLE DISTANCE BY UPDATING
# THE BELOW CODE

# ROVER ONE (pink) INSTRUCTIONS
# LEFT RIGHT and FORWARDS


rover1.forward(20)
rover1.right(20)
rover1.forward(30)
rover1.left(20)
rover1.forward(10)

# -----------------------

# ROVER TWO (blue) INSTRUCTIONS
# LEFT RIGHT and FORWARDS

rover2.forward(10)
rover2.right(30)
rover2.forward(20)
rover2.left(40)
rover2.forward(10)


# -----------------------


# Close when clicked
screen.exitonclick()
