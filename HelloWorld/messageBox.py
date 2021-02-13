from tkinter import *
from tkinter import messagebox


# messagebox.showinfo('Info Window','You are into a new window!')

answer = messagebox.askquestion('Question 1','Do you really want to open a new window?')

if answer == 'yes':
    messagebox.showinfo('New Window','You opened a new Window')
if answer == 'no':
    messagebox.showinfo('No Window','You closed a window')