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
tiles = list(range(32)) * 2
state = {'mark': None, 'taps' : 0}
# Innovación: Usar letras en lugar de números para mejorar la memoria visua
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '1', '2', '3', '4', '5', '6',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '1', '2', '3', '4', '5', '6']
hide = [True] * 64


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
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    state['taps'] += 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    up()
    goto(0, 0)
    shape(car)
    stamp()

    # Variable para contar cuantas fichas siguen ocultas
    tiles_ocultos = sum(1 for h in hide if h)

    for count in range(64):
        x = xy(count)[0]
        y = xy(count)[1]

        if hide[count]:
            tiles_ocultos +=1
            up()
            goto(x, y)
            down()
            color('black', 'blue')
            begin_fill()
            for _ in range(4):
                forward(50)
                left(90)
            end_fill()
        else:
            #Si la ficha esta descubierta, dibuja su valor
            up()
            goto(x + 25, y + 10)  # Ajuste centrado aproximado
            color('black')
            write(tiles[count], align="center", font=('Arial', 30, 'normal'))


    # Dibujar la selección actual si hay un cuadro marcado
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()

        goto(x + 25, y + 2)
        color('black')
        write(tiles[mark], align = 'center', font=('Arial', 30, 'normal'))

        goto(x, y)
        down()
        color('black', 'blue')
        begin_fill()
        for _ in range(4):
            forward(50)
            left(90)
        end_fill()
        up()
        goto(x + 25, y + 5)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 25, 'normal'))


    if tiles_ocultos == 0:
        up()
        goto(0, 0)
        color('green')
        write("You win!", align= "center", font=('Arial', 24, 'bold'))

    up()
    goto(0, 210)
    color('black')
    write(f"Taps: {state['taps']}", align='center', font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 480, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
