import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import sqlite3
from tkinter import font
from tkinter import messagebox
###################################################

##Main page(GUI)    

def __init__(self, master):
    frame = Frame(master)
    frame.pack()


##################################################

def NewFile():
    print("New File!")
    

def OpenFile():
    name = filedialog.askopenfilename()
    print(name)
    

def About():
   print("This is a simple example of a menu")
    

def SaveFile():
   bat = filedialog.asksaveasfilename()
   print (bat)
    

def doNothing():
   print("nothing has happened")

##################################################################
##filemenu Section


#####################################################################

#buttons section
   
class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
##Create buttons for the  app  main window

        self.button1 = ttk.Button(self, text= "All Builds",command=self.showAll)
        self.button2 = ttk.Button(self, text="Add Build",command=self.addNewWindow)
        self.button3 = ttk.Button(self, text="Edit",command=self.amend)
        self.button4 = ttk.Button(self, text="Delete",command=self.delete)
        self.button5 = ttk.Button(self, text = "Exit", command=self.quit)
        
##Show the buttons created
        self.button1.grid(row=6, column=10)
        self.button2.grid(row=7, column=10)
        self.button3.grid(row=8, column=10)
        self.button4.grid(row=9, column=10)
        self.button5.grid(row=10, column=10)
## Main window completed.

def addNewWindow(self):
t = tk.Toplevel(self)
t.wm_title(" New BuildData Entry")
global IDentry, NameEntry, WHOEntry, GradeEntry, ActiveEntry

myContainer = Frame(t)
myContainer.pack(side=TOP, expand=YES, fill=BOTH)

##Create the entry boxes for data input and show them
PriceEntry = Entry(myContainer)
CaseEntry = Entry(myContainer)
GPUEntry = Entry(myContainer)
CPUEntry = Entry(myContainer)
MotherboardEntry = Entry(myContainer)
PowerSupplyEntry = Entry(myContainer)
ActiveEntry = Entry(myContainer)

PriceEntry.grid(row = 1, column = 1)
CaseEntry.grid(row = 2, column = 1)
GPUEntry.grid(row = 3, column = 1)
CPUEntry.grid(row = 4, column = 1)
MotherboardEntry.grid(row = 5, column = 1)
PowerSupplyEntry.grid(row = 6, column = 1)
ActiveEntry.grid(row = 7, column = 1)


##Define the fonts to be used for display
BigFont=font.Font(family="Arial", size=14, weight="bold") # Font for Big Labels
HeaderFont = font.Font(family="Arial", size=12, weight="bold") #Font for header

##Create the label to be used and show them
HLabel1 = Label(myContainer, text = "Price", fg = "green", font=HeaderFont)
HLabel2 = Label(myContainer, text = "Case", font=HeaderFont)
HLabel3 = Label(myContainer, text = "GPU", font=HeaderFont)
HLabel4 = Label(myContainer, text = "CPU", font=HeaderFont)
HLabel5 = Label(myContainer, text = "Motherboard", font=HeaderFont)
HLabel6 = Label(myContainer, text = "PowerSupply", font=HeaderFont)
HLabel7 = Label(myContainer, text = "Active", font=HeaderFont)
HLabelTop = Label(myContainer, text= "New build", font=BigFont) #fg="red")

HLabel1.grid(row = 1, column = 0)
HLabel2.grid(row = 2, column = 0)
HLabel3.grid(row = 3, column = 0)
HLabel4.grid(row = 4, column = 0)
HLabel5.grid(row = 5, column = 0)
HLabel6.grid(row = 6, column = 0)
HLabel7.grid(row = 7, column = 0)
HLabelTop.grid(row = 0, column = 0, columnspan = 5)

##Create a separate additional frame to hold the buttons, however button 3 is attached to first frame?
myBtnContainer = Frame(t)
myBtnContainer.pack(side=TOP, expand=YES, fill=BOTH)

button1 = ttk.Button(myBtnContainer, text="Add Build", command=self.Add, width=15)
button2 = ttk.Button(myBtnContainer, text="Clear Entries", command=self.ClearEntries, width=15)
button3 = ttk.Button(myContainer, text="Exit", command=t.destroy, width=15)
button1.grid(row = 1, column = 1)
button2.grid(row = 1, column = 2)
button3.grid(row = 3, column = 2)


def Add(self):
    ##Check if any of the data is missing and create an alert - messagebox
    if PriceEntry.get() == "" or CaseEntry == "" or GPUEntry.get() == "" or CPUEntry.get() == "" or MotherboardEntry.get() == "" or PowerSupplyentry.get() == "" or  ActiveEntry.get() == "" :
        messagebox.showerror("Bad Data", "Some Or All Required\nFields Are Blank")
        return
    ##Connect to database - path set for demo in the lecture
    ##Make sure to change this to where you create the student database
    db =  sqlite3.connect("F:\Computer Science\Coursework\MODULE 3COSC002W.Y The Computer and Software Development\Semester 2\PC.db")

    ##Good idea to display ALL records from the table in the console:
    s = "Select * from PC"
    cursor = db.cursor()
    cursor.execute(s)
    rows = cursor.fetchall()

    print (len(cursor.fetchall()))
    for row in rows:
        print("$$$: ",row)

        ##Let's find out how many rows are in our result set
        numrows =(len(rows)) ##cursor.rowcount
        print (len(rows))


##Get the new data and formulate the sql string to add the record:
        s = "insert into student(Price, Case, GPU, CPU, Motherboard, PowerSupply, Active) "
        s = s + "values ('" + PriceEntry.get() + "', '" + CaseEntry.get() + "', '" + GPUEntry.get() + "', '" + CPUEntry.get()+ "','" + MotherboardEntry.get()+ "','" + ActiveEntry.get()+ "');"

        print(s)

        cursor = db.cursor()


        cursor.execute(s)
        cursor.close()
        db.commit()
        db.close()


def ClearEntries(self):
    print("clear addnew Info")
    PriceEntry.delete(0, END)
    CaseEntry.delete(0,END)
    GPUEntry.delete(0,END)
    GPUEntry.delete(0,END)
    MotherboardEntry.delete(0,END)
    PowerSupplyEntry.delete(0,END)
    ActiveEntry.delete(0,END)
        

def amend(self):
    t = tk.Toplevel(self)
    t.wm_title("Edit Exiting Build")
    t.geometry("500x100")
    myContainer = Frame(t)
    myContainer.pack(side=TOP, expand=YES, fill=BOTH)

    BigFont=font.Font(family="Arial", size=10, weight="bold") ##Font for Big Labels
    HeaderFont = font.Font(family="Arial", size=10, weight="bold") ##Font for header
    HLabelTop = Label(myContainer, text= "Amend Existing Build - To be done", font=BigFont) #fg="red")
    HLabelTop.grid(row = 1, column = 1, columnspan = 5)



def delete(self):
    t = tk.Toplevel(self)
    t.wm_title("Delete Exiting Student")
    t.geometry("500x100")
    myContainer = Frame(t)
    myContainer.pack(side=TOP, expand=YES, fill=BOTH)

    BigFont=font.Font(family="Arial", size=10, weight="bold") ##Font for Big Labels
    HeaderFont = font.Font(family="Arial", size=10, weight="bold") ##Font for header
    HLabelTop = Label(myContainer, text= "Delete Existing Build - To be done", font=BigFont) #fg="red")
    HLabelTop.grid(row = 1, column = 1, columnspan = 5)

        ##Connect to database - path set for demo in the lecture
        ##Make sure to change this to where you create the student database
        
    db = sqlite3.connect ("F:\Computer Science\Coursework\MODULE 3COSC002W.Y The Computer and Software Development\Semester 2\PC.db")
        
    s = "Select * from PC"

    cursor = db.cursor()
    cursor.execute(s)
    rows = cursor.fetchall()
    print (len(cursor.fetchall()))
    for row in rows:
        print(row)
        ##Let's find out how many rows are in our result set
        numrows =(len(rows)) ##cursor.rowcount
        print (len(rows))

        ##Put the Header Information on the Page
        BigFont=font.Font(family="Arial", size=14, weight="bold") ##Font for Big Labels
        HeaderFont = font.Font(family="Arial", size=12, weight="bold") ##Font for header

        ##Create column headings for data display


        HLabel1 = Label(myContainer, text = "Price", font=HeaderFont)
        HLabel2 = Label(myContainer, text = "Case", font=HeaderFont)
        HLabel3 = Label(myContainer, text = "GPU", font=HeaderFont)
        HLabel4 = Label(myContainer, text = "CPU", font=HeaderFont)
        HLabel5 = Label(myContainer, text = "Motherboard", font=HeaderFont)
        HLabel6 = Label(myContainer, text = "PowerSupply", font=HeaderFont)
        HLabel7 = Label(myContainer, text = "Active", font=HeaderFont)
        HLabelTop = Label(myContainer, text= "All Builds", font=BigFont) #fg="red")


        HLabelTop.grid(row = 0, column = 0, columnspan = 5)
        HLabel1.grid(row = 1, column = 0)
        HLabel2.grid(row = 1, column = 1)
        HLabel3.grid(row = 1, column = 2)
        HLabel4.grid(row = 1, column = 3)
        HLabel5.grid(row = 1, column = 4)
        HLabel6.grid(row = 1, column = 5)
        HLabel7.grid(row = 1, column = 6)

        ##Use a set of lists to hold each field of data
        Price=[]
        Case=[]
        GPU=[]
        CPU=[]
        Motherboard=[]
        PowerSupply=[]
        Active=[]
        
        for a in range(numrows):
            data = rows[a][0]
            myLabel1 = Label(myContainer, text = data)
            Price.append(myLabel1)
            myLabel2 = Label(myContainer, text = rows[a][1])
            Case.append(myLabel2)
            myLabel3 = Label(myContainer, text = rows[a][2])
            GPU.append(myLabel3)
            myLabel4 = Label(myContainer, text = rows[a][3])
            CPU.append(myLabel4)
            myLabel5 = Label(myContainer, text = rows[a][3])
            Motherboard.append(myLabel4)
            myLabel6 = Label(myContainer, text = rows[a][3])
            PowerSupply.append(myLabel4)
            myLabel7 = Label(myContainer, text = str(rows[a][4]))
            Active.append(myLabel5)

            Price[a].grid(row=a+2, column=0, sticky=W)
            Case[a].grid(row=a+2, column=1, sticky=W)
            GPU[a].grid(row=a+2, column=2, sticky=W)
            CPU[a].grid(row=a+2, column=3, sticky=W)
            Motherboard[a].grid(row=a+2, column=4, sticky=W)
            PowerSupply[a].grid(row=a+2, column=5, sticky=W)
            Active[a].grid(row=a+2, column=6, sticky=W)



def quit(self):
    root.destroy()

        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("PC Builder")
    root.geometry("1200x800")

    menu = Menu(root)
    root.config(menu = menu)
    filemenu = Menu(menu)
    menu.add_cascade(label = "File", menu = filemenu)

    filemenu.add_command(label = "New", command = NewFile)
    filemenu.add_command(label = "Open File", command = OpenFile)
    filemenu.add_command(label = "Save File", command = SaveFile)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = root.destroy)

    editmenu = Menu(menu)
    menu.add_cascade(label = "Edit", menu=editmenu)

    editmenu.add_command(label = "Undo", command = doNothing)
    editmenu.add_command(label = "Redo", command = doNothing)
    editmenu.add_separator()
    editmenu.add_command(label = "Cut", command = doNothing)
    editmenu.add_command(label = "Copy", command = doNothing)
    editmenu.add_command(label = "Paste", command = doNothing)
    editmenu.add_command(label = "Select all", command = doNothing)

    helpmenu = Menu(menu)
    menu.add_cascade(label = "Help", menu=helpmenu)
    helpmenu.add_command(label = "About", command = About)
    
    text_label = Label(root, text = "Customise Your PC!")
    text_label.pack()
    Pc = PhotoImage(file = "PC Part Picker.png")
    w1 = Label(root, image = Pc).pack(side = "top")

    
##root.title("Menu")

main = MainWindow(root)
main.pack()#side="top", fill="both", expand=True
    
root.mainloop()


mainloop()

