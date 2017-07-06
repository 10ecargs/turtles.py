from turtle import *
import math
# Name your Turtle.
t = Turtle()
t.pencolor("white")
# Set Up your screen and starting position.
penup()
setup(500,300)
x_pos =-250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:

t.goto(500,300)
pendown()
t.pencolor("aquamarine")
begin_fill()
fillcolor("aquamarine")

for sides in range(3):
    forward(100)
    left(120)

end_fill()
import sys
print (sys.argv)

input_var  = int(input("Enter a number: "))

t.goto(500,300)
pendown()
for shape in range(input_var):
    forward(100)
    left(360/input_var)

# Close window on click.
exitonclick()
