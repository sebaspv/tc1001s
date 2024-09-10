"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = [[0,"🐏"],[1,"🤖"],[2,"🐳"],[3,"🥞"],[4,"🦭"],[5,"💖"],[6,"🪷"],[7,"🪐"],
         [8,"🫧"],[9,"🌝"],[10,"☃️"],[11,"🌞"],[12,"🌟"],[13,"🌮"],[14,"🧁"],[15,"🍨"],
         [16,"🦩"],[17,"🍭"],[18,"💐"],[19,"🌱"],[20,"🎄"],[21,"🎃"],[22,"🎨"],[23,"🏆"],
         [24,"🐧"],[25,"🎮"],[26,"🧬"],[27,"💸"],[28,"👩‍💻"],[29,"👨‍💻"],[30,"👨‍🎓"],[31,"👩‍🎓"]] * 2
state = {'mark': None}
hide = [True] * 64
game_won = False


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        if all(not hidden for hidden in hide):
            game_won = True

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 4, y + 4)
        color('#4086ff')
        write(tiles[mark][1], font=('Arial', 30, 'normal'))

    if game_won:
        up()
        goto(-120, 0)  # Posicionar el mensaje en el centro de la pantalla
        color('green')
        write("¡Felicidades! Juego completado.", font=('Arial', 20, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
