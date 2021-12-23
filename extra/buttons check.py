import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import font
from tkinter import messagebox

class MainWindow(tk.Frame):
  counter:0
  def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button1 = tk.Button(self, text="Show All",command=self.showAll)
        self.button2 = tk.Button(self, text="Add New",command=self.addNewWindow, fg = "green")
        self.button3 = tk.Button(self, text="Amend",command=self.amend, fg = "blue")
        self.button4 = tk.Button(self, text="Delete",command=self.delete, fg = "orange")
        self.button5 = tk.Button(self, text = "QUIT", fg = "black", command = root.destroy)

        self.button1.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button2.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button3.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button4.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button5.pack()
