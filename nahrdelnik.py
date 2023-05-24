import tkinter
import random

def click(e):
    global processed,moveable
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz) != 0 and zoz[0] in zoz:
        if len(processed)==0:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            print("stalo sa")

root = tkinter.Tk()
canvas = tkinter.Canvas()
w = 700
h = 500
canvas.configure(width=w,height=h,bg="white")
canvas.pack()
colours = ["hot pink","yellow","spring green","blue"]

moveable = []
processed = []
size = 30

def setup():
    global gulicka
    for i in range(4):
        for o in range(10):
            x = random.randrange(0,670)
            y = random.randrange(0,400)
            moveable.append(canvas.create_oval(x,y,x+size,y+size,fill=colours[i],width=0))

def moveit():
    global processed
    if len(processed):
        coord = canvas.coords(processed[0])
        finalpos = (600,452)
        if finalpos[0]>coord[0]:
            dx = finalpos[0]/coord[0]
            dy = finalpos[1]-coord[1]
            canvas.move(processed[0],dx,dy)
        elif finalpos[0]<coord[0]:
            dx = coord[0]-finalpos[0]
            dy = coord[1]/finalpos[1]
            canvas.move(processed[0],dx,dy)
    canvas.after(5,moveit)

hlavicka = canvas.create_oval(20,460,35,475,fill="black")
nit = canvas.create_line(20,467,600,467)

moveit()
setup()
root.bind("<Button-1>",click)
root.mainloop()
