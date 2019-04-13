#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t

t.speed(10000000)
t.begin_fill()
t.penup()
t.goto(-200, 200)
t.pendown()
a = abs(t.pos())
t.color('red', 'yellow')
while True:
    t.forward(150)
    t.left(150)
    b = abs(t.pos())
    if a - 1 < b < a + 1:
        break
t.end_fill()
t.penup()


def draw_square(color, x=0, y=0, size=70):
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()

def draw_flower(x, y, size=60):
    draw_square("purple", x - size, y - size,size)
    draw_square("orange", x - size, y + size,size)
    draw_square("yellow", x + size, y + size,size)
    draw_square("blue", x + size, y - size,size)
    draw_square("pink", x , y,size)

draw_flower(200,-200,15)
draw_flower(-100,0,20)
draw_flower(-210,-200,30)

t.speed(30)

t.exitonclick()
