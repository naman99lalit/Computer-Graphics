from graphics import *
import time
win=GraphWin("MY PIE CHART USING BRESENHAM ALGORITHM",900,900)
def main(xc=450,yc=450,r=50):
    x=0
    y=r
    d=3-2*r
    x1=xc
    y1=yc
    x2=485
    y2=485
    x3=500
    y3=450
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    xm=x1
    ym=y1
    e=(dy-(dx/2))
    dx1=abs(x3-x1)
    dy1=abs(y3-y1)
    xn=x1
    yn=y1
    e1=(dy1-(dx1/2))
    put_pixel(xm,ym,"green")
    while(y>=x):
        draw_circle(xc,yc,x,y)
        x=x+1
        print(x,y)
        if(d>0):
            y=y-1
            d=d+4*(x-y)+10
        else :
            d=d+4*x+6
        print(x,y)
        draw_circle(xc,yc,x,y)
    line1(xm,ym,x2,e,dy,dx)
    line2(xn,yn,x3,e1,dy1,dx1)
    win.getMouse()
    win.close()

def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)

def draw_circle(xc,yc,x,y):
    put_pixel(xc+x,yc+y)
    put_pixel(xc-x,yc+y)
    put_pixel(xc+x,yc-y)
    put_pixel(xc-x,yc-y)
    put_pixel(xc+y,yc+x)
    put_pixel(xc-y,yc+x)
    put_pixel(xc+y,yc-x)
    put_pixel(xc-y,yc-x)
def line1(xm,ym,x2,e,dy,dx):
    while(xm<x2):
        xm=xm+1
        if(e<0):
            e=e+dy
        else :
            e=e+(dy-dx)
            ym=ym+1
        put_pixel(xm,ym,"green")
def line2(xn,yn,x3,e1,dy1,dx1):
    while(xn<x3):
        xn=xn+1
        if(e1<0):
            e1=e1+dy1
        else :
            e1=e1+(dy1-dx1)
            yn=yn+1
        put_pixel(xn,yn,"green")

main()
