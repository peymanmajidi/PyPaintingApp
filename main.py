from tkinter import *
from tkinter import ttk

fillcolor = 'red'
    
def draw(e):
    global pre
    canvas.create_line(pre.x-2, pre.y-2, e.x+2, e.y+2, width = 15, fill = fillcolor)
    pre = e

def setcolor(color):
    global fillcolor
    fillcolor = color
    print('fillcolor switch to: ' + fillcolor)

def setBackColor():
    canvas.config(background = fillcolor)


def eraser(e):
    global pre
    canvas.create_line(pre.x-3, pre.y-3, e.x+3, e.y+3, width = 30, fill = 'white')
    pre = e

def point(e):
    global pre
    pre = e

def command(e):
    if e.char == 'r':
        color = 'red'
    elif e.char == 'b':
        color = 'black'
    elif e.char == 'g':
        color = 'green'
    elif e.char == 'y':
        color = 'yellow'
    setcolor(color)


root = Tk()
col = 1
Button(root, text='قرمز',command= lambda: setcolor('red'), background = 'red').grid(row=0,column = col)
col +=1
Button(root, text='آبی',command= lambda: setcolor( 'blue'), background =  'blue').grid(row=0,column = col)
col +=1
Button(root, text='سبز',command= lambda: setcolor('green'), background = 'green').grid(row=0,column = col)
col +=1
Button(root, text='قهوه ای',command= lambda: setcolor('brown'), background = 'brown').grid(row=0,column = col)
col +=1
Button(root, text='زرد',command= lambda: setcolor('yellow'), background = 'yellow').grid(row=0,column = col)
col +=1
Button(root, text='بنفش',command= lambda: setcolor('violet'), background = 'violet').grid(row=0,column = col)
col +=1
Button(root, text='نارنجی',command= lambda: setcolor('orange'), background = 'orange').grid(row=0,column = col)
col +=1
Button(root, text='خاکستری',command= lambda: setcolor('gray'), background = 'gray').grid(row=0,column = col)
col +=1
Button(root, text='سفید',command= lambda: setcolor('white'), background = 'white').grid(row=0,column = col)
col +=1
Button(root, text='مشکی',command= lambda: setcolor('black'), background = 'black', foreground = 'white').grid(row=0,column = col)

canvas = Canvas(root, width= 800, height = 600 , background = 'white')
canvas.grid(row = 1, column = 0, columnspan = 11)
canvas.bind('<ButtonPress>', point)
canvas.bind('<B1-Motion>',draw)
canvas.bind('<B3-Motion>',eraser)
canvas.bind('<B2-Motion>', lambda e: setBackColor())
root.bind('<KeyPress>',command)
root.mainloop()
