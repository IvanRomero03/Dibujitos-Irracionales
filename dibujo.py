from math import floor, pi
import turtle
from pi import *
from phi import phi


def drawIrrational(irrational: float, n: int) -> None:
    count = 0
    while irrational > 0 and count < n:
        print(irrational)
        num = irrational
        turtle.left(360/num)
        num = floor(irrational)
        irrational -= num
        irrational *= 10
        turtle.forward(25)
        count += 1
    turtle.done()


def drawIrrationalBase10(irrational: float, n: int) -> None:
    count = 0
    while irrational > 0 and count < n:
        print(irrational)
        num = floor(irrational)
        if(num != 0):
            turtle.left(360/num)
        irrational -= num
        irrational *= 10
        turtle.forward(25)
        count += 1
    turtle.done()


def drawIrrationalBase3(irrational: float, n: int) -> None:
    count = 0
    while irrational > 0 and count < n:
        print(irrational)
        num = floor(irrational)
        if(num != 0):
            turtle.left(360/num)
        irrational -= num
        irrational *= 4
        turtle.forward(25)
        count += 1
    turtle.done()


def drawIrrationalBaseN(irrational: float, n: int, base: int) -> None:
    count = 0
    while irrational > 0 and count < n:
        print(irrational)
        num = floor(irrational)
        if(num != 0):
            turtle.left(360/num)
        irrational -= num
        irrational *= base + 1
        turtle.forward(25)
        count += 1
    turtle.done()


drawIrrationalBaseN(phi(), 100, 3)
