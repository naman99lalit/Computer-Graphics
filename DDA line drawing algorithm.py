from graphics import *
import time
win=GraphWin("A STRAIGHT LINE USING DDA LINE DRAWING ALGORITHM",900,900)
def main():
    line(100,100,100,300)
    line(100,300,150,300)
    line(150,300,150,200)
    line(150,200,200,300)
    line(200,300,250,300)
    line(250,300,250,100)
    line(250,100,200,100)
    line(200,100,200,200)
    line(200,200,150,100)
    line(150,100,100,100)

    line(400,100,400,300)
    line(400,300,550,300)
    line(550,300,550,250)
    line(550,250,450,250)
    line(450,250,450,100)
    line(450,100,400,100)
    win.getMouse()
    win.close()
def abs(n):
    if(n>0):
        return n
    else:
        return n*(-1)
def line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if(abs(dx)>abs(dy)):
        steps=abs(dx)
    else:
        steps=abs(dy)
    (xin)= dx/(steps)
    (yin)= dy/(steps)
    (x)= x1
    (y)=y1
    for i in range(steps+1):
        put_pixel(x,y,"red")
        x=x+xin
        y=y+yin
def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)
main()
