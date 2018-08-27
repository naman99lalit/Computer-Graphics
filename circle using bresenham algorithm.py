from graphics import *
import time
win = GraphWin("my circle", 900, 900)
def main(xc=0,yc=0,r=5):
    x=0
    y=r
    d=3-2*r
    while(y>=x):
        draw_circle(xc,yc,x,y)
        x=x+1
        print(x,y,d)
        if(d>0):
            y=y-1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(xc,yc,x,y)
    win.getMouse()
    win.close()

def put_pixel(x,y,color="red"):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.10)

def draw_circle(xc,yc,x,y):
    put_pixel(xc+x,yc+y,"blue")
    put_pixel(xc-x,yc+y,"blue")
    put_pixel(xc+x,yc-y,"blue")
    put_pixel(xc-x,yc-y,"blue")
    put_pixel(xc+y,yc+x)
    put_pixel(xc-y,yc+x)
    put_pixel(xc+y,yc-x)
    put_pixel(xc-y,yc-x)
main()
