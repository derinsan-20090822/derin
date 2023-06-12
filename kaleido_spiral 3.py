import turtle
from itertools import cycle
def draw_shape(size,angle,shift,shape):
   turtle.pencolor(next(colors))
   next_shape=''
   if shape=='circle':
      turtle.circle(size)
      next_shape='square'
    elif shape ='square':
         for i inrange(4):
            turtle.forword(size=2)
            turtle.left(90)
        next_shape='circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size+5,angle+1,shift+1,next_shape)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(0,0,1'circle')
