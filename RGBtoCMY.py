import tkinter
from tkinter import *
from tkinter import ttk


def calculate(*args):
    R = Red.get()
    G = Green.get()
    B = Blue.get()

root = Tk()
root.title("RGB to CMY")
photo = tkinter.PhotoImage(file="Media/Images/TBL.png")
root.wm_iconphoto(False, photo)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#RGB
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

#CMY
Cyan = StringVar()
Cyan_label = ttk.Label(mainframe, width=7, text="Cyan")
Cyan_label.grid(column=4, row=1)
Cyan_entry = ttk.Entry(mainframe, width=7, textvariable=Cyan)
Cyan_entry.grid(column=5, row=1)

Magenta = StringVar()
Magenta_label = ttk.Label(mainframe, width=7, text="Magenta")
Magenta_label.grid(column=4, row=2)
Magenta_entry = ttk.Entry(mainframe, width=7, textvariable=Magenta)
Magenta_entry.grid(column=5, row=2)

Yellow = StringVar()
Yellow_label = ttk.Label(mainframe, width=7, text="Yellow")
Yellow_label.grid(column=4, row=3)
Yellow_entry = ttk.Entry(mainframe, width=7, textvariable=Yellow)
Yellow_entry.grid(column=5, row=3)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

Red_entry.focus()

root.mainloop()