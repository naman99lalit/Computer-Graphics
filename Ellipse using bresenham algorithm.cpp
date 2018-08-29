#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<graphics.h>
#include<dos.h>
#define round(a)(int(a+0.5))
void main()
{
double total=0.0,a=0.0;
double x2,y2;
int i,n;
int gd=DETECT,gm;
initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
cout<<"PIE CHART"<<endl;
cout<<"Enter the no. of regions"<<endl;
cin>>n;
double values[10];
double per[10];
double angle[10]={0,0,0,0,0,0,0,0,0,0};
double b[10];
cout<<"Enter the values of the regions"<<endl;
circle(300,300,100);
line(300,300,400,300);
for(i=0;i<n;i++)
{
cin>>values[i];
total=total+values[i];
}
for(i=0;i<n;i++)
{
per[i]=((values[i]/total)*100);
a=((per[i]/100)*360);
if(i==0)
b[i]=a;
else
b[i]=b[i-1]+a;
angle[i]=(3.14*b[i])/180;
x2=(300+100*cos(angle[i]));
y2=(300-100*sin(angle[i]));
line(300,300,round(x2),round(y2));
setfillstyle(1,i+1);
if(x2>300&&y2< 300)
floodfill(x2+2,y2+2,15);
else
floodfill(x2-2,y2-2,15);
}
getch();
closegraph();
}
