from graphics import *
import time
win=GraphWin("A CIRCLE USING MIDPOINT LINE DRAWING ALGORITHM",900,900)
def main():
    circle(450,450,75)
    win.getMouse()
    win.close()
def circle(x1,y1,r):
    x=r
    y=0
    d=0
    while(x>=y):
        put_pixel(x1+x,y1+y,"red")
        put_pixel(x1+y,y1+x,"red")
        put_pixel(x1-y,y1+x,"red")
        put_pixel(x1-x,y1+y,"red")
        put_pixel(x1-x,y1-y,"red")
        put_pixel(x1-y,y1-x,"red");
        put_pixel(x1+y,y1-x,"red");
        put_pixel(x1+x,y1-y,"red");
        if(d<=0):
            y=y+1
            d=d+2*y+1
        if(d>0):
            x=x-1
            d=d-2*x+1
def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)
main()
