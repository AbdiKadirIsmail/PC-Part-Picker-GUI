import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import sqlite3
from tkinter import font
from tkinter import messagebox

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PC Builder")
    root.geometry("1200x800")
    text_label = Label(root, text = "Customise Your PC!")
    text_label.pack()
    #main = MainWindow(root)
    #main.pack(side="top", fill="both", expand=True)
    Pc = PhotoImage(file = "PC Part Picker.png")
    w1 = tk.Label(root, image = Pc)
    w1.grid(row=0, column = 1)
root.mainloop()
mainloop()
