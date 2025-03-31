from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN


def calculate(*args):
    pass

root = Tk()
root.title("RGB to CMY")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Red = StringVar()
Red_label = ttk.Label(mainframe, width=7, text="Red")
Red_label.grid(column=1, row=1)
Red_entry = ttk.Entry(mainframe, width=7, textvariable=Red)
Red_entry.grid(column=2, row=1)

Green = StringVar()
Green_label = ttk.Label(mainframe, width=7, text="Green")
Green_label.grid(column=1, row=2)
Green_entry = ttk.Entry(mainframe, width=7, textvariable=Green)
Green_entry.grid(column=2, row=2)

Blue = StringVar()
Blue_label = ttk.Label(mainframe, width=7, text="Blue")
Blue_label.grid(column=1, row=3)
Blue_entry = ttk.Entry(mainframe, width=7, textvariable=Blue)
Blue_entry.grid(column=2, row=3)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

Red_entry.focus()

root.mainloop()