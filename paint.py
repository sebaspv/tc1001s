"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import math

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(30):
        forward(3.1416* ((math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2))) / 30)
        right(12)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x) * 2)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()


def pentagon(start, end):
    """Draw pentagon from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    side_length = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5

    angle = 72 
    
    for _ in range(5):
        forward(side_length)
        left(angle)
    
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state["start"]

    if start is None:
        state["start"] = vector(x, y)
    else:
        shape = state["shape"]
        end = vector(x, y)
        shape(start, end)
        state["start"] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {"start": None, "shape": line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, "u")
onkey(lambda: color("black"), "K")
onkey(lambda: color("white"), "W")
onkey(lambda: color("green"), "G")
onkey(lambda: color("blue"), "B")
onkey(lambda: color("red"), "R")
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color("#D206FF"), 'P')
onkey(lambda: store("shape", line), "l")
onkey(lambda: store("shape", square), "s") # Keybind to draw square
onkey(lambda: store("shape", circle), "c")
onkey(lambda: store("shape", rectangle), "r") # Keybind to draw rectangle
onkey(lambda: store("shape", triangle), "t") # Keybind to draw triangle
onkey(lambda: store("shape", pentagon), "t")
done()
