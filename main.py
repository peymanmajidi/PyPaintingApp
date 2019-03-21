from tkinter import *
from tkinter import ttk

fillcolor = 'black'
    
def draw(e):
    global pre
    canvas.create_line(pre.x, pre.y, e.x, e.y, width = 10, fill = fillcolor)
    pre = e

def point(e):
    global pre
    pre = e

def command(e):
    if e.char == 'r':
        fillcolor = 'red'
    elif e.char == 'b':
        fillcolor = 'black'
    elif e.char == 'g':
        fillcolor = 'green'
    elif e.char == 'y':
        fillcolor = 'yellow'



root = Tk()
canvas = Canvas(root, width= 800, height = 600 , background = 'white')
canvas.pack()
canvas.bind('<ButtonPress>', point)
canvas.bind('<B1-Motion>',draw)
root.bind('<Keypress>',command)
root.mainloop()
