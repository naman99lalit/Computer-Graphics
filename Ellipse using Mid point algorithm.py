from graphics import *
import time
win=GraphWin("A STRAIGHT LINE USING DDA LINE DRAWING ALGORITHM",900,900)
def main():
    xc=int(input())
    yc=int(input())
    rx=int(input())
    ry=int(input())
    ellipse(xc,yc,rx,ry)
    win.getMouse()
    win.close()
def ellipse(xc,yc,rx,ry):
    p=ry*ry-rx*rx*ry+rx*rx/4
    x=0
    y=ry
    while(2.0*ry*ry*x <= 2.0*rx*rx*y):
        if(p < 0):
            x=x+1
            p=p+2*ry*ry*x+ry*ry
        else:
            x=x+1
            y=y-1
            p=p+2(ry*ry*x)-2*rx*rx*y-ry*ry
	put_pixel(xc+x,yc+y,"red")
	put_pixel(xc+x,yc-y,"red")
	put_pixel(xc-x,yc+y,"red")
	put_pixel(xc-x,yc-y,"red")
    
    p=ry*ry*(x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
    while(y > 0):
        if(p <= 0):
            x=x+1
            y=y-1
            p=p+2*ry*ry*x-2*rx*rx*y+rx*rx
        else:
	    y=y-1
	    p=p-2*rx*rx*y+rx*rx
	
	put_pixel(xc+x,yc+y,"red")
	put_pixel(xc+x,yc-y,"red")
	put_pixel(xc-x,yc+y,"red")
	put_pixel(xc-x,yc-y,"red")
def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)
main()
