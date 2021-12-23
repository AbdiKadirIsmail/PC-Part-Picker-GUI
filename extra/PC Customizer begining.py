import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import font
from tkinter import messagebox

      
  # Constructor
def __init__(self, master):
    frame = Frame(master)
    frame.pack()    

root = Tk()
root.title("PC Builder")
text_label = Label(root, text = "Customise your PC!")
text_label.pack()

Pc = PhotoImage(file = "PC Part Picker.png")
w1 = Label(root, image = Pc).pack(side = "top")


