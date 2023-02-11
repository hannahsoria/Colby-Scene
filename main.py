'''
Hannah Soria
Project 2
CS 151 F21
A Shape Collection
'''

import turtle
import shapelib as s

turtle.speed(20)
'''This combine the shapes from shapelib.py and adds color to creat Lorimer Chapel'''
def colby1(x,y,scale):
    turtle.color("darkolivegreen4"),'''The bottom of the picture is made green like grass'''
    turtle.begin_fill()
    s.background(-400,-600,20)
    turtle.end_fill()
    turtle.color("cadetblue4"),'''The top of the background is draw blue'''
    turtle.begin_fill()
    s.background(-400,-100,20)
    turtle.end_fill()
    turtle.width(5),'''change the width of the pen'''
    s.compoundShape2(x,y,scale),'''The shape with color written in shapelib.py is drawn first'''
    turtle.color("black","darkorange4"),'''The color of the shapes is changed to border=black and fill=dark orange'''
    turtle.begin_fill()
    s.smallRectangle(x+23.5*scale,y+73.5*scale,scale),'''The rest of the building is drawn'''
    turtle.end_fill()
    turtle.begin_fill()
    s.compoundShape3(x+32*scale,y+93.5*scale,scale*.65)
    turtle.end_fill()
    turtle.begin_fill()
    s.compoundShape3(x+37*scale,y+109.5*scale,scale*.45)
    turtle.end_fill()
    turtle.begin_fill()
    s.compoundShape3(x+41*scale,y+120.5*scale,scale*.3)
    turtle.end_fill()
    turtle.color("black","darkgrey"),'''The pen color is changed to draw the border in black and the fill in dark grey.'''
    turtle.begin_fill()
    s.tallTriangle(x+41.5*scale,y+128*scale,scale*.55),'''The topmost point is drawn.'''
    turtle.end_fill()
    turtle.color("black","beige"),'''The pen color is changed to draw the border in black and the fill in beige'''
    turtle.begin_fill()
    s.triangleNew(x+30*scale,y+50*scale,scale),'''Details of the building are drawn'''
    turtle.end_fill()
    turtle.begin_fill()
    s.column(x+12.5*scale,y,scale)
    turtle.end_fill()
    turtle.begin_fill()
    s.column(x+35*scale,y,scale)
    turtle.end_fill()
    turtle.begin_fill()
    s.column(x+65*scale,y,scale)
    turtle.end_fill()
    turtle.begin_fill()
    s.column(x+87.5*scale,y,scale)
    turtle.end_fill()
    turtle.begin_fill()
    s.tallRectangle(x+45*scale,y,scale*.5)
    turtle.end_fill()
    turtle.begin_fill()
    s.square(x+20*scale,y+10*scale,scale*.5)
    turtle.end_fill()
    turtle.begin_fill()
    s.square(x+20*scale,y+30*scale,scale*.5)
    turtle.end_fill()
    turtle.begin_fill()
    s.square(x+47.5*scale,y+30*scale,scale*.5)
    turtle.end_fill()
    turtle.begin_fill()
    s.square(x+75*scale,y+10*scale,scale*.5)
    turtle.end_fill()
    turtle.begin_fill()
    s.square(x+75*scale,y+30*scale,scale*.5)
    turtle.end_fill()
    s.cloud(x-50,y+100,10),'''The clouds are drawn and the color was programmed in shapelib because other wise it fills incorrectly'''
    s.cloud(x-100,y+300,40)
    s.cloud(x+400,y+200,50)
    s.cloud(x+200,y+150,30)
'''Function is run and the colby1 appears'''
colby1(-100,-100,2)

s.turtle.exitonclick()

