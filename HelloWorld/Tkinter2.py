from tkinter import  *

class open_new_window:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.label_1 = Label(frame,text = 'This is old window')
        self.button_1 = Button(frame,text = 'New Window',command = self.print_function)
        self.quit_button = Button(frame,text = 'Quit',command = frame.quit)

        self.label_1.grid(row = 0,column=1)
        self.button_1.grid(row= 1,column=1)
        self.quit_button.grid(row=2,column=1)

    def print_function(self):
        print("This is a new World!")

    # def new_Window(self,master):


root = Tk()
onw = open_new_window(root)

root.mainloop()
