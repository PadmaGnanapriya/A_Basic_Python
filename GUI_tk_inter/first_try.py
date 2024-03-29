import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def addApp():
    filename =filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"),("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label= tk.Label(frame, text=app, bg="gray")
        lable.pack()


canvas =tk.Canvas(root,height=600,width=600, bg='#263D42')
canvas.pack()
frame=tk.Frame(root,bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile=tk.Button(root,text='Open File', padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()
runApps=tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42")
runApps.pack()
root.mainloop()
