import tkinter as tk
from tkinter import *
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 180)
entry = tk.Entry(root) 
canvas1.create_window(200, 100, window=entry)


#functie


def jaar():
    getal = entry.get()
    getal = int(getal)
    jaar = 2022 - getal
    naam["text"] = jaar

def restart():
        entry.delete(0,END)  


#button


aButton = tk.Button(
    root,
    text="submit",
    fg='blue',
    bg='white',
    pady='6px',
    padx='6px',
    command=jaar
)

bButton = tk.Button(
    root,
    text="delete",
    fg='blue',
    bg='white',
    pady='6px',
    padx='6px',
    command=restart
)

naam = tk.Label()


#pack


aButton.pack()
bButton.pack()
naam.pack()
canvas1.pack()
root.mainloop()