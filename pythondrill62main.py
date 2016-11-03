from tkinter import *
import tkinter as tk

import pythondrill62func
import pythondrill62gui


class ParentWindow(Frame):
        def __init__(self, master, *args, **kwargs):
            Frame.__init__(self, master, *args, **kwargs)

            self.master= master
            self.master.minsize(450,400)
            self.master.maxsize(450,400)
            self.master.title("Move a File")
            self.master.configure(bg="#F0F0F0")
            self.master.protocol("WM_DELETE_WINDOW")
            arg=self.master
            pythondrill62gui.load_gui(self)

if __name__ == "__main__": 
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
