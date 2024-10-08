"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
         # Aumenta la velocidad del proyectil para que se mueva más rápido.
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball and targets."""
    clear()
    
    # Cambiar el color y la figura de los balones.
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'purple') # Cambiar el color de los balones.

    if inside(ball):
        goto(ball.x, ball.y)
        color('green') # Cambiar el color del proyectil.
        shape('turtle')  # Cambiar la figura del proyectil.
        stamp()

    update()

def update_targets_positions():
    """Actualizar las posiciones de los objetivos."""

    new_targets = []
    for target in targets:
        # Mueve el balón al lado derecho de la pantalla.
        target.x -= 0.5
        if inside(target):
            new_targets.append(target)

    for target in targets:
        if abs(target - ball) < 13:
            new_targets.remove(target)

    return new_targets

def move():
    """Move ball and targets."""
    global targets
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    targets = update_targets_positions()

    draw()
    ontimer(move, 10) # Aumenta la frecuencia de actualización del juego.

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
