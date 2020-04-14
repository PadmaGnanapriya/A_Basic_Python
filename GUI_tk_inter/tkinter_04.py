from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text='Hey Padme')
label.pack()
label.config(text="PISSUNE")
label.config(text="This is the Sri Lanka")
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 18, 'bold'))
