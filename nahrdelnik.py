import tkinter
import random

def click(e):
    global processed,moveable
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz) != 0 and zoz[0] in zoz and len(processed)==0 and counter<10:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            moveit()

root = tkinter.Tk()
canvas = tkinter.Canvas()
w = 700
h = 500
canvas.configure(width=w,height=h,bg="white")
canvas.pack()
colours = ["hot pink","yellow","spring green","blue"]

moveable = []
processed = []
size = 45
counter = 0

def setup():
    global gulicka
    for i in range(4):
        for o in range(10):
            x = random.randrange(0,650)
            y = random.randrange(0,400)
            moveable.append(canvas.create_oval(x,y,x+size,y+size,fill=colours[i],width=0))

def moveit():
    global processed
    coord = canvas.coords(processed[0])
    finalpos = (600,444)
    dx = finalpos[0] - coord[0]
    dy = finalpos[1] - coord[1]
    mx = 0
    my = 0
    if dx != 0 and dy != 0:
        if dx > 0:
            if dx >= dy:
                mx = dx//dy
                my = 1
            else:
                mx = 1
                my = dy//dx
        elif dx < 0:
            mx = -1
            my = dy//abs(dx)

    canvas.move(processed[0], mx, my)
    if dy == 0 and dx == 0:
        nit_move()
    else:
        canvas.after(2,moveit)

def nit_move():
    global processed, counter, x
    if len(processed)!=0:
        ballm = canvas.coords(processed[0])
        if ballm[0] > x:
            canvas.move(processed[0], -5, 0)
        else:
            counter+=1
            processed=[]
            x+=size
        canvas.after(2, nit_move)

#nit
hlavicka = canvas.create_oval(20,460,35,475,fill="black")
nit = canvas.create_line(20,467,600,467)
x = 35

setup()
root.bind("<Button-1>",click)
root.mainloop()
