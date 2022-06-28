from numpy import array
from turtle import *

resizemode(rmode="auto")
setup( width = 50, height = 50, startx = None, starty = None) 


hideturtle()
def repere():
        speed(0)
        k=0
        for i in range(41):
            penup()
            goto(342,k)
            pendown()
            goto(-342,k)
            k+=18
            p=0
        for i in range(10):
            penup()
            goto(-342,-p)
            pendown()
            goto(342,-p)
            p+=18
        s=0
        for i in range(20):
            penup()
            goto(s,720)
            pendown()
            goto(s,-162)
            s+=18
        u=0
        for i in range(20):
            penup()
            goto(-u,720)
            pendown()
            goto(-u,-162)
            u+=18
        penup()
        pencolor("red")
        width(3)
        goto(0,720)
        pendown()
        goto(0,-162)
    
        penup()
        pencolor("blue")
        width(3)
        goto(342,18*15)
        pendown()
        goto(-342,18*15)
        penup()
        pencolor("black")
        goto(4,18*15)
        write("0",move=True,font=('Arial', 4, 'normal'))
        goto(4+(18*5),18*15)
        write("5",move=True,font=('Arial', 4, 'normal'))
        goto(2+(18*10),18*15)
        write("10",move=True,font=('Arial', 4, 'normal'))
        goto(2+(18*15),18*15)
        write("15",move=True,font=('Arial', 4, 'normal'))
        
        goto(2+(18*-5),18*15)
        write("-5",move=True,font=('Arial', 4, 'normal'))
        goto(1+(18*-10),18*15)
        write("-10",move=True,font=('Arial', 3, 'normal'))
        goto(1+(18*-15),15*18)
        write("-15",move=True,font=('Arial', 3, 'normal'))
        
        
        goto(4,(18*15)+18*5)
        write("5",move=True,font=('Arial', 4, 'normal'))
        goto(2,(18*15)+18*10)
        write("10",move=True,font=('Arial', 4, 'normal'))
        goto(2,(18*15)+18*15)
        write("15",move=True,font=('Arial', 4, 'normal'))
        goto(2,(18*15)+18*20)
        write("20",move=True,font=('Arial', 4, 'normal'))
        
        goto(2,(18*15)+18*-5)
        write("-5",move=True,font=('Arial', 4, 'normal'))
        goto(1,(18*15)+18*-10)
        write("-10",move=True,font=('Arial', 3, 'normal'))
        goto(1,(18*15)+18*-15)
        write("-15",move=True,font=('Arial', 3, 'normal'))
        goto(1,(18*15)+18*-20)
        write("-20",move=True,font=('Arial', 3, 'normal'))
tracer(0)
penup()
goto(-342,-700)
write("by rayenbenyoussef")
pendown()
update()
   
v=False
while v==False:
    type=textinput("choose type prbl / hyprbl :","")
    v=type=="prbl"or type=="hyprbl"
n=1000

x=array([float()]*n)
y=array([str]*n)
x1=array([float()]*n)
y1=array([str]*n)

if type=="prbl":
    penup()
    goto(-342,360)
    write("For ax**2+bx+c :")
    goto(-342,320)
    write("You can replace the a or the b or the c with <0>:")
    goto(-342,280)
    write("For a=0: Draw becomes a straight line not a parable anymore")
    goto(-342,240)
    write("For b=0: the parable will not be able to move ")
    goto(-342,200)
    write("in axis of symmetry")
    goto(-342,160)
    write("For c=0: the parable will not be able to move ")
    goto(-342,120)
    write("in directrix")
    f=str(textinput("ax**2+bx+c for prbl: ",""))
    tracer(0)
    goto(0,500)
    pendown()
    pencolor("white")
    width(1000)
    goto(0,-500)
    width(0.05)
    pencolor("black")
    a=f[0:f.find("x**2")]
    b=f[f.find("**2")+3:f.find("x",len(f[0:f.find("x")+1]))]
    c=f[f.find("x",len(f[0:f.find("x")+1]))+1:len(f)]

    if eval(a)!=0 :
        x=array([float()]*n)
        y=array([str]*n)
        x1=array([float()]*n)
        y1=array([str]*n)
        a=eval(a)
        b=eval(b)
        c=eval(c)
        sx=(-b)/(2*a)
        i=0
        cx=sx
    
        while i<n:
            x[i]=cx
            h=eval(str(a)+"*(("+str(cx)+")**2)"+"+("+str(b)+"*"+str(cx)+")+"+str(c))
            y[i]=h
            cx+=0.1
            i+=1
        i1=0
        cy=sx
    
        while i1<n:
            x1[i1]=cy
            h1=eval(str(a)+"*(("+str(cy)+")**2)"+"+("+str(b)+"*"+str(cy)+")+"+str(c))
            y1[i1]=h1
            cy-=0.1
            i1+=1
        
    elif eval(a)==0:
        n=40
        x=array([float()]*n)
        y=array([str]*n)
        x1=array([float()]*n)
        y1=array([str]*n)
        b=eval(b)
        c=eval(c)
        sx=0
    
        i=0
        cx=sx
        while i<(n):
            x[i]=cx
            h=eval(str(a)+"*(("+str(cx)+")**2)"+"+("+str(b)+"*"+str(cx)+")+"+str(c))
            y[i]=h
            cx+=10
            i+=1
        
        i1=0
        cy=sx
        while i1<(n):
            x1[i1]=cy
            h1=eval(str(a)+"*(("+str(cy)+")**2)"+"+("+str(b)+"*"+str(cy)+")+"+str(c))
            y1[i1]=h1
            cy-=1
            i1+=1
    repere()
    penup()
    pencolor("green")
    goto(x[0]*18,y[0]*18+(18*15))
    pendown()
    for i in range(n):
        goto(x[i]*18,y[i]*18+(18*15))
    penup()

    penup()
    pencolor("green")
    goto(x1[0]*18,y1[0]*18+(18*15))
    pendown()
    for i in range(n):
        goto(x1[i]*18,y1[i]*18+(18*15))
        
    penup()
    pencolor("white")
    goto(400,727)
    width(12)
    pendown()
    goto(-400,727)
    
    penup()
    pencolor("white")
    goto(396,-495)
    width(666)
    pendown()
    goto(-396,-495)
    
    penup()
    pencolor("white")
    goto(-360,-792)
    width(36)
    pendown()
    goto(-360,792)
    
    penup()
    pencolor("white")
    goto(360,-792)
    width(36)
    pendown()
    goto(360,792)
    penup()
    width(3)
    pencolor("black")
    goto(-342,-200)
    write("S("+str(x[0])+" ; "+str(y[0])+")")
    goto(0,-210)
    pendown()
    goto(0,-610)
    penup()
    goto(-342,-250)
    pendown()
    goto(342,-250)
    penup()
    goto(-342,-450)
    pendown()
    goto(342,-450)
    penup()
    goto(-342,-410)
    pendown()
    goto(342,-410)
    penup()
    goto(-342,-210)
    pendown()
    goto(342,-210)
    penup()
    goto(-342,-610)
    pendown()
    goto(342,-610)
    penup()
    
    goto(-171,-250)
    write("X")
    goto(-342,-290)
    write(x[0])
    goto(-342,-330)
    write(x[10])
    goto(-342,-370)
    write(x[20])
    goto(-342,-410)
    write(x[30])
    
    goto(-171,-450)
    write("-X")
    goto(-342,-490)
    write(x1[0])
    goto(-342,-530)
    write(x1[10])
    goto(-342,-570)
    write(x1[20])
    goto(-342,-610)
    write(x1[30])
    
    goto(171,-250)
    write("Y")
    goto(10,-290)
    write(y[0])
    goto(10,-330)
    write(y[10])
    goto(10,-370)
    write(y[20])
    goto(10,-410)
    write(y[30])
    
    goto(171,-450)
    write("-Y")
    goto(10,-490)
    write(y1[0])
    goto(10,-530)
    write(y1[10])
    goto(10,-570)
    write(y1[20])
    goto(10,-610)
    write(y1[30])
    
    goto(-90,-650)
    write("f(x)= "+f)
    
    goto(x[0],720)
    n=715
    for i in range(88):
        goto(x[0]*18,n)
        penup()
        n-=5
        goto(x[0]*18,n)
        pendown()
        n-=5
    penup()
    goto(-342,(y[0])*18)
    n=337
    for i in range(69):
        goto(n,y[0]*18+(18*15))
        penup()
        n-=5
        goto(n,y[0]*18+(18*15))
        pendown()
        n-=5
    
    update()
elif type=="hyprbl":
    penup()
    goto(-342,360)
    write("For ax+b/cx+d:")
    goto(-342,320)
    write("You can replace the a or the b or the c or the d with  ")
    goto(-342,280)
    write("<0> but you can't replace the c and the d in ")
    goto(-342,240)
    write("the same time with 0 it causes zero division ERROR")
    f=str(textinput("ax+b/cx+d for hyprbl: ",""))
    tracer(0)
    goto(0,500)
    pendown()
    pencolor("white")
    width(1000)
    goto(0,-500)
    width(1)
    pencolor("black")
    
    a=f[0:f.find("x")]
    b=f[f.find("x")+1:f.find("/")]
    c=f[f.find("/")+1:f.find("x",len(f[0:f.find("/")]))]
    d=f[f.find("x",len(f[0:f.find("x")+1]))+1:len(f)]
    
    if a==a:
        n=15000
        x=array([float()]*n)
        y=array([str]*n)
        x1=array([float()]*n)
        y1=array([str]*n)
        a=eval(a)
        b=eval(b)
        c=eval(c)
        d=eval(d)
        sx=(-d/c)
        i=0
        cx=sx
    
        while i<n:
            x[i]=cx
            try:
                h=eval("("+str(a)+"*"+str(cx)+"+"+str(b)+")/("+str(c)+"*"+str(cx)+"+"+str(d)+")")
            except:
                h=None
            y[i]=h
            cx+=0.01
            i+=1
        i1=0
        cy=sx
    
        while i1<n:
            x1[i1]=cy
            try:
                h1=eval("("+str(a)+"*"+str(cy)+"+"+str(b)+")/("+str(c)+"*"+str(cy)+"+"+str(d)+")")
            except:
                h1=None
            y1[i1]=h1
            cy-=0.01
            i1+=1
    repere()
    penup()
    pencolor("green")
    goto(x[1]*18,y[1]*18+(18*15))
    pendown()
    for i in range(1,n):
        goto(x[i]*18,y[i]*18+(18*15))
    penup()

    penup()
    pencolor("green")
    goto(x1[1]*18,y1[1]*18+(18*15))
    pendown()
    for i in range(1,n):
        goto(x1[i]*18,y1[i]*18+(18*15))
    penup()
    penup()
    pencolor("white")
    goto(400,727)
    width(12)
    pendown()
    goto(-400,727)
    
    penup()
    pencolor("white")
    goto(396,-495)
    width(666)
    pendown()
    goto(-396,-495)
    
    penup()
    pencolor("white")
    goto(-360,-792)
    width(36)
    pendown()
    goto(-360,792)
    
    penup()
    pencolor("white")
    goto(360,-792)
    width(36)
    pendown()
    goto(360,792)
    
    penup()
    width(3)
    pencolor("black")
    goto(-342,-200)
    write("W("+str(x[0])+" ; "+str(a/c)+")")
    goto(0,-210)
    pendown()
    goto(0,-610)
    penup()
    goto(-342,-250)
    pendown()
    goto(342,-250)
    penup()
    goto(-342,-450)
    pendown()
    goto(342,-450)
    penup()
    goto(-342,-410)
    pendown()
    goto(342,-410)
    penup()
    goto(-342,-210)
    pendown()
    goto(342,-210)
    penup()
    goto(-342,-610)
    pendown()
    goto(342,-610)
    penup()
    
    goto(-171,-250)
    write("X")
    goto(-342,-290)
    write(x[0])
    goto(-342,-330)
    write(x[10])
    goto(-342,-370)
    write(x[20])
    goto(-342,-410)
    write(x[30])
    
    goto(-171,-450)
    write("-X")
    goto(-342,-490)
    write(x1[0])
    goto(-342,-530)
    write(x1[10])
    goto(-342,-570)
    write(x1[20])
    goto(-342,-610)
    write(x1[30])
    
    goto(171,-250)
    write("Y")
    goto(10,-290)
    write(y[0])
    goto(10,-330)
    write(y[10])
    goto(10,-370)
    write(y[20])
    goto(10,-410)
    write(y[30])
    
    goto(171,-450)
    write("-Y")
    goto(10,-490)
    write(y1[0])
    goto(10,-530)
    write(y1[10])
    goto(10,-570)
    write(y1[20])
    goto(10,-610)
    write(y1[30])
    
    goto(-90,-650)
    write("f(x)= "+f)
  
    goto(x[0],720)
    n=715
    for i in range(88):
        goto(x[0]*18,n)
        penup()
        n-=5
        goto(x[0]*18,n)
        pendown()
        n-=5
    penup()
    goto(-342,(a/c)*18)
    n=337
    for i in range(69):
        goto(n,(a/c)*18+(18*15))
        penup()
        n-=5
        goto(n,(a/c)*18+(18*15))
        pendown()
        n-=5
    
    update()
mainloop()