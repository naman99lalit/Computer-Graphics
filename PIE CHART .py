from graphics import *
import math
import time
win = GraphWin("MY PIE CHART USING BRESENHAM ALGORITHM", 900, 900)
def main(xc=450,yc=450,r=50):
    x=0
    y=r
    d=3-2*r
    x1=xc
    y1=yc
    sumt = 0
    n = int(input())
    p1=list(map(int, input().split()))
    th = []
    for i in range(len(p1)):
        sumt += ((p1[i]/100)*360)
        theta = sumt
        th.append(theta)
    th = [x*(math.pi/180) for x in th]
    print(th)
    x2 = [int((r*math.cos(x))+xc) for x in th]
    y2 = [int(yc+(r*math.sin(x))) for x in th]
    coor = []
    for _ in range(len(x2)):
        coor.append((x2[_],y2[_]))
    print(coor)
    x3=int(r*math.cos(0)+xc)
    y3=int(yc-r*math.sin(0))
    while(y>=x):
        draw_circle(xc,yc,x,y)
        x=x+1
        if(d>0):
            y=y-1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(xc,yc,x,y)
    for (x2,y2) in coor:
        aLine = Line(Point(x1,y1), Point(x2,y2))
        aLine.setFill("green")
        aLine.draw(win)
    win.getMouse()
    win.close()

def put_pixel(x,y,color="red"):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.002)

def draw_circle(xc,yc,x,y):
    put_pixel(xc+x,yc+y)
    put_pixel(xc-x,yc+y)
    put_pixel(xc+x,yc-y)
    put_pixel(xc-x,yc-y)
    put_pixel(xc+y,yc+x)
    put_pixel(xc-y,yc+x)
    put_pixel(xc+y,yc-x)
    put_pixel(xc-y,yc-x)
def line(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    xm=x1
    ym=y1
    put_pixel(xm,ym,"green")
    e=dy-(dx/2)
    while(xm<=x2):
        xm=xm+1
        if(e<0):
            e=e+dy
        else:
            e=e+(dy-dx)
            ym=ym+1
        put_pixel(xm,ym,"green")
main()
