'''
Hannah Soria
Lab 2
CS 151 F21
Create compound shapes
'''

import turtle

def triangle(scale):
    '''
    This function draw a triangle
    parameters: scale, variable that controls the size of the triangle
    '''
    turtle.forward(scale)
    turtle.left(120)
    turtle.forward(scale)
    turtle.left(120)
    turtle.forward(scale)
    turtle.left(120)

#triangle(100)
'''
penup (pu) and pendown (pd) are used to move the turtle without draw a line
'''

def goto(x,y):
    print('goto(): going to',x,y)
    print('goto():before move, turtle at',turtle.position())
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    print('goto():after move, turtle now at',turtle.position())

#goto(0,0)
#triangle(100)
#goto(0,0)
#triangle(100)
#goto(0,0)
#triangle(100)

def triangle2(x,y,scale):
    '''
    Draws a triangle at any ('x','y') position and scale('scale")
    By default, the side lengths are 100 (when "scale" = 1)
    '''
    goto(x,y)
    triangle(100*scale)

#triangle2(0,0,100)
#triangle2(-50,-25,200)
#triangle2(-100,-50,300)

def triangleStack(x,y,scale):
    '''
    Draw three triangles on top of each other.
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

triangleStack(-200,0,1)
triangleStack(0,0,(1*.5))
triangleStack(100,0,1*(1/3))



   


turtle.exitonclick()