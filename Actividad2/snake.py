"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores disponibles para la serpiente y la comida"
colors = ['blue', 'yellow', 'purple', 'pink', 'orange']
color = choice(colors) # Selección aleatoria del color de la serpiente
food_color = choice(colors) # Selección aleatoria del color de la comida

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        # Reubica la comida aleatoriamente dentro de los límites.
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Dibuja cada segmento del cuerpo de la serpiente con el color seleccionado aleatoriamente.
    for body in snake:
        square(body.x, body.y, 9, color) 

    # Dibuja la comida en la pantalla con el color seleccionado aleatoriamente.
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

def move_food():
    """Mueve la comida aleatoriamente dentro de los límites de la ventana"""
    # Reubica la comida en una posición aleatoria dentro de la ventana.
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    ontimer(move_food, 2000)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()
