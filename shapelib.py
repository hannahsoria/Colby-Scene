'''
Hannah Soria
Lab 2
CS 151 F21
Create compound shapes
'''

import turtle
#window = turtle.getscreen()
#turtle = turtle.Turtle()

def triangle(x,y,scale):
    '''
    This function turtle a triangle
    parameters: scale, variable that controls the size of the triangle
    '''
    goto(x,y)
    turtle.forward(25*scale)
    turtle.left(120)
    turtle.forward(25*scale)
    turtle.left(120)
    turtle.forward(25*scale)
    turtle.left(120)

#triangle(100)
'''
penup (pu) and pendown (pd) are used to move the turtle without turtle a line
'''

def goto(x,y):
    print('goto(): going to',x,y)
    print('goto():before move, turtle at',turtle.position())
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.setheading(0)
    print('goto():after move, turtle now at',turtle.position())

#goto(0,0)
#triangle(100)
#goto(0,0)
#triangle(100)
#goto(0,0)
#triangle(100)

def triangle2(x,y,scale):
    '''
    turtles a triangle at any ('x','y') position and scale('scale")
    By default, the side lengths are 100 (when "scale" = 1)
    '''
    goto(x,y)
    triangle(100*scale)

#triangle2(0,0,100)
#triangle2(-50,-25,200)
#triangle2(-100,-50,300)

def triangleStack(x,y,scale):
    '''
    turtle three triangles on top of each other.
    Smaller triangle are places on top of larger ones
    '''
    #largest triangle
    #triangle2(x*scale,y*scale,2*scale)
    triangle2(x,y, 2*scale)
    #medium triangle in middle
    triangle2(x+50*scale,y+173.2*scale,1*scale)
    #small triangle on top of stack)
    triangle2(x+75*scale,y+259.81*scale,0.5*scale)

#triangleStack(0,0,1)

#triangleStack(-200,0,1)
#triangleStack(0,0,(1*.5))
#triangleStack(100,0,1*(1/3))

def tallRectangle(x,y,scale):
    goto(x,y)
    turtle.forward(25*scale)
    turtle.left(90)
    turtle.forward(50*scale)
    turtle.left(90)
    turtle.forward(25*scale)
    turtle.left(90)
    turtle.forward(50*scale)
    '''This draw a rectangle that is taller than it is long.'''
def longRectangle(x,y,scale):
    goto(x,y)
    turtle.forward(50*scale)
    turtle.left(90)
    turtle.forward(25*scale)
    turtle.left(90)
    turtle.forward(50*scale)
    turtle.left(90)
    turtle.forward(25*scale)
    '''This draw a rectangle that is longer than it is tall.'''
def background(x,y,scale):
    longRectangle(x,y,scale)
    '''This calls the longRectangle so that it can be used for the sky and grass'''
def trapezoid(x,y,scale):
    goto(x,y)
    turtle.forward(100*scale)
    turtle.left(120)
    turtle.forward(27*scale)
    turtle.left(60)
    turtle.forward(73*scale)
    turtle.left(60)
    turtle.forward(27*scale)
    '''This draw a trapezoid'''
def smallRectangle(x,y,scale):
    goto(x,y)
    turtle.forward(50*scale)
    turtle.left(90)
    turtle.forward(20*scale)
    turtle.left(90)
    turtle.forward(50*scale)
    turtle.left(90)
    turtle.forward(20*scale)
    turtle.left(90)
    '''This draws a small rectangle'''
def tallTriangle(x,y,scale):
    goto(x,y)
    turtle.forward(25*scale)
    turtle.left(100)
    turtle.forward(75*scale)
    turtle.left(161)
    turtle.forward(75*scale)
    '''This draws a triangle that is taller than it is wide'''
def angledTrap(x,y,scale):
    goto(x,y)
    turtle.forward(10*scale)
    turtle.left(90)
    turtle.forward(25*scale)
    turtle.left(120)
    turtle.forward(11.5*scale)
    turtle.left(60)
    turtle.forward(19*scale)
    '''This draw a trapezoid where the top line is slanted down to the left'''
def angledTrapReverse(x,y,scale):
    goto(x,y)
    turtle.forward(10*scale)
    turtle.left(90)
    turtle.forward(19*scale)
    turtle.left(60)
    turtle.forward(11.5*scale)
    turtle.left(120)
    turtle.forward(25*scale)
    '''This mirrors angledTrap'''
def triangleNew(x,y,scale):
    goto(x,y)
    turtle.forward(43.5*scale)
    turtle.left(138)
    turtle.forward(30*scale)
    turtle.left(85)
    turtle.forward(29*scale)
    '''This draw a triangle'''
def column(x,y,scale):
    goto(x,y)
    turtle.forward(5*scale)
    turtle.left(90)
    turtle.forward(50*scale)
    turtle.left(90)
    turtle.forward(5*scale)
    turtle.left(90)
    turtle.forward(50*scale)
    '''This draw a column'''
def square(x,y,scale):
    goto(x,y)
    turtle.forward(20*scale)
    turtle.left(90)
    turtle.forward(20*scale)
    turtle.left(90)
    turtle.forward(20*scale)
    turtle.left(90)
    turtle.forward(20*scale)
    '''This draw a square'''
def compoundShape1(x,y,scale):
    goto(x,y)
    tallRectangle(x,y,scale)
    goto(0,0)
    tallTriangle(x,y+50*scale,scale)
    '''This draws a tallRectangle with a tallTriangle sitting on top of it'''
def compoundShape2(x,y,scale):
    goto(0,0)
    turtle.color("black","darkorange4")
    turtle.begin_fill()
    longRectangle(x,y,2*scale)
    turtle.end_fill()
    turtle.begin_fill()
    trapezoid(x,y+50*scale,scale)
    turtle.end_fill()
    '''This draws a longRectangle with a trapezoid on top of it. It is given a color here because the color would not fill correctly in main.py'''
def compoundShape3(x,y,scale):
    longRectangle(x,y,scale)
    goto(x,y)
    angledTrap(x-10*scale,y,scale)
    goto(x,y)
    angledTrapReverse(x+50*scale,y,scale)
    '''This draws a longRectangle with opposite angledTrap functions on either side'''
def circle1(x,y,radius):
    goto(x,y)
    turtle.circle(radius)
    '''This draws a circle.'''
def cloud(x,y,scale):
    turtle.color("azure3")
    turtle.begin_fill()
    circle1(x,y,10)
    turtle.end_fill()
    turtle.begin_fill()
    circle1(x+10,y+10,10)
    turtle.end_fill()
    turtle.begin_fill()
    circle1(x+20,y+5,10)
    turtle.end_fill()
    turtle.begin_fill()
    circle1(x+35,y,10)
    turtle.end_fill()
    turtle.begin_fill()
    circle1(x-10,y+5,10)
    turtle.end_fill()
    '''This draw multiple circles in different places to become a cloud.'''

#turtle.exitonclick()
