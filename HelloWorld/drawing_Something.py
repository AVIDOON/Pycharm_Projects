from tkinter import *

root = Tk()
canvas = Canvas(root,width = 200,height = 100)
canvas.pack()

redline = canvas.create_line(0,0,200,100,fill = 'red')
yellow_rectangle = canvas.create_rectangle(50,20,150,70,fill='yellow')
# text_draw = canvas.create_text(30,30,text='This')
oval_draw = canvas.create_oval(20,20,50,70)

canvas.delete(redline)

root.mainloop()