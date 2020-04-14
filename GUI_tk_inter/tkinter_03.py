from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self,master):
        self.label=ttk.Label(master, text="Hello padme")
        self.label.grid(row=0, column =0, columnspace=2)

        ttk.Button(master,text='Gnanapriya', command=self.texas_hello).grid(row=1, column=0)
        ttk.Button(master,text='Anjana', command=self.hawaii_hello).grid(row=1,column=1)

def texas_hello(self):
    self.label.config(text='Padma, Hey brother')

def hawaii_hello(self):
    self.lbel.config(text='Aloha, Tkinter')

def main():
    root =Tk()
    app= HelloApp(root)
    root.mainloop()
