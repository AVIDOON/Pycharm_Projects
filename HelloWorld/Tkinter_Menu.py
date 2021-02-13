from tkinter import  *

def printHello():
    print("Hello World")

def shyProject():
    print("It's a new Project")

def openProject():
    print("Project Opened")


# Main Menu
root = Tk()
frame = Frame(root)
menu = Menu(frame)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label='File',menu = submenu)
submenu.add_command(label='New Project',command=shyProject)
submenu.add_command(label='New',command=openProject)
submenu.add_separator()
submenu.add_command(label='Open',command=printHello)
submenu.add_command(label='Quit',command=root.quit)

# ToolBar
toolbar = Frame(root,bg='blue')

insert_Button = Button(toolbar,text = 'Insert Image',command=openProject)
insert_Button.pack(side=LEFT,padx=2,pady=2)

add_Button = Button(toolbar,text = 'Add Image',command=openProject)
add_Button.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill = X)

# Status Bar

status_bar = Label(root,text='This is my status bar',bg='green',bd =1,relief=SUNKEN,anchor=W)
status_bar.pack(side=BOTTOM,fill = X)

root.mainloop()