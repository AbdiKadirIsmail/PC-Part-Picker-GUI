import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import sqlite3
import backend

##########################################################################################################################################################################################################################################################################
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

##########################################################################################################################################################################################################################################################################
#Main window completed.

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button1 = ttk.Button(self, text= "All Builds",command=self.showAll)
        self.button2 = ttk.Button(self, text="Add Build",command=self.addNewWindow)
        self.button3 = ttk.Button(self, text="Edit",command=self.amend)
        self.button5 = ttk.Button(self, text = "Exit", command=self.quit)
        
        self.button1.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button2.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button3.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        self.button5.pack(side="top", fill="both", expand=True, padx=200, pady=10)
        
##########################################################################################################################################################################################################################################################################
        #Creating a new window for Add Build window

    def addNewWindow(self):

        t = tk.Toplevel(self)
        t.wm_title("Add New Build")
        global PriceEntry, CasesEntry, GPUEntry, CPUEntry, MotherboardEntry, PowerSupplyEntry, MemoryEntry, ActiveEntry

        myContainer = Frame(t)
        myContainer.pack(side=TOP)

        PriceEntry = Entry(myContainer)
        CasesEntry = Entry(myContainer)
        GPUEntry = Entry(myContainer)
        CPUEntry = Entry(myContainer)
        MotherboardEntry = Entry(myContainer)
        PowerSupplyEntry = Entry(myContainer)
        MemoryEntry = Entry(myContainer)
        ActiveEntry = Entry(myContainer)

        PriceEntry.grid(row = 1, column = 1)
        CasesEntry.grid(row = 2, column = 1)
        GPUEntry.grid(row = 3, column = 1)
        CPUEntry.grid(row = 4, column = 1)
        MotherboardEntry.grid(row = 5, column = 1)
        PowerSupplyEntry.grid(row = 6, column = 1)
        MemoryEntry.grid(row = 7, column = 1)
        ActiveEntry.grid(row = 8, column = 1)
        
#Define the fonts to be used for display
        BigFont=font.Font(family="Calibri(Body)", size=16, weight="bold") 
        HeaderFont = font.Font(family="Calibri(Body)", size=12, weight="bold")  

#Create the label to be used and show them
        HLabel1 = Label(myContainer, text = "Price", fg = "RoyalBlue", font=HeaderFont)
        HLabel2 = Label(myContainer, text = "Cases", font=HeaderFont)
        HLabel3 = Label(myContainer, text = "GPU", font=HeaderFont)
        HLabel4 = Label(myContainer, text = "CPU", font=HeaderFont)
        HLabel5 = Label(myContainer, text = "Motherboard", font=HeaderFont)
        HLabel6 = Label(myContainer, text = "PowerSupply", font=HeaderFont)
        HLabel7 = Label(myContainer, text = "Memory", font=HeaderFont)
        HLabel8 = Label(myContainer, text = "Active", font=HeaderFont)
        HLabelTop = Label(myContainer, text= "New build", font=BigFont) 

        HLabel1.grid(row = 1, column = 0)
        HLabel2.grid(row = 2, column = 0)
        HLabel3.grid(row = 3, column = 0)
        HLabel4.grid(row = 4, column = 0)
        HLabel5.grid(row = 5, column = 0)
        HLabel6.grid(row = 6, column = 0)
        HLabel7.grid(row = 7, column = 0)
        HLabel8.grid(row = 8, column = 0)
        HLabelTop.grid(row = 0, column = 0, columnspan = 5)

#Create a separate additional frame to hold the buttons, however button 3 is attached to first frame?
        myBtnContainer = Frame(t)
        myBtnContainer.pack(side=TOP)

        button1 = ttk.Button(myBtnContainer, text="Add Build", command=self.Add, width=15)
        button2 = ttk.Button(myBtnContainer, text="Clear Entries", command=self.ClearEntries, width=15)
        button3 = ttk.Button(myBtnContainer, text="Exit", command=t.destroy, width=15)
        button1.grid(row = 1, column = 1)
        button2.grid(row = 1, column = 2)
        button3.grid(row = 1, column = 3)


    def Add(self):
        #Check if any of the data is missing and create an alert - messagebox

        if PriceEntry.get() == "" or CasesEntry.get() == "" or GPUEntry.get() == "" or CPUEntry.get() == "" or \
		  MotherboardEntry.get() == "" or PowerSupplyEntry.get() == "" or MemoryEntry.get() == "" or ActiveEntry.get() == "" :
            messagebox.showerror("Bad Data", "Please fill in the blank fields") 
            return

        

        #Connecting to the database file (PC.db)

        
        db =  sqlite3.connect ("D:\Computer Science\Coursework\MODULE 3COSC002W.Y The Computer and Software Development\Semester 2\Final work\PC.db")
        s = "Select * from PC"
        cursor = db.cursor()
        cursor.execute(s)
        rows = cursor.fetchall()
        print (len(cursor.fetchall()))
        for row in rows:
            print("$$$: ",row)
        numrows =(len(rows)) 
        print (len(rows))

        s = "insert into PC (Price, Cases, GPU, CPU, Motherboard, PowerSupply, Memory, Active)" 
        s = s + "values ('" + PriceEntry.get() + "', '" + CasesEntry.get() + "', '" + GPUEntry.get() + "', '" + CPUEntry.get()+ "','" + MotherboardEntry.get()+ "','" + PowerSupplyEntry.get()+ "','" + MemoryEntry.get()+ "','" + ActiveEntry.get()+ "');"

        print(s)

        cursor = db.cursor()


        cursor.execute(s)
        cursor.close()
        db.commit()
        db.close()
    

    def ClearEntries(self):
        PriceEntry.delete(0, END)
        CasesEntry.delete(0,END)
        CPUEntry.delete(0,END)
        GPUEntry.delete(0,END)
        MotherboardEntry.delete(0,END)
        PowerSupplyEntry.delete(0,END)
        MemoryEntry.delete(0,END)
        ActiveEntry.delete(0,END)

##########################################################################################################################################################################################################################################################################

    def amend(self):
        t = tk.Toplevel(self)
        t.wm_title("PC Editor")
        t.geometry("1000x400")       

####################################################################
        #creates a menu tab at the top to the window
        menu = Menu(t)
        t.config(menu = menu)
        filemenu = Menu(menu)
        menu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New", command = NewFile)
        filemenu.add_command(label = "Open File", command = OpenFile)
        filemenu.add_command(label = "Save File", command = SaveFile)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = t.destroy)
    
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

####################################################################
        #creating the Edit window
        def get_selected_row(event):
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
            e5.delete(0,END)
            e5.insert(END,selected_tuple[5])
            e6.delete(0,END)
            e6.insert(END,selected_tuple[6])
            e7.delete(0,END)
            e7.insert(END,selected_tuple[7])
            e8.delete(0,END)
            e8.insert(END,selected_tuple[8])

        #defineing commands for buttons   
        def view_command():
            list1.delete(0,END)
            for row in backend.view():
                list1.insert(END,row) 
            
            
        def search_command():
            list1.delete(0,END)
            for row in backend.search(Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get()):
                list1.insert(END,row)

                
        def add_command():
            backend.insert(Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get())
            list1.delete(0,END)
            list1.insert(END,(Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get()))

            
        def delete_command():
            backend.delete(selected_tuple[0])
            
            
        def update_command():
            backend.update(selected_tuple[0],Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get())

        #creating label list
        
        l1=Label(t,text="Price")
        l1.grid(row=0,column=0)

        l2=Label(t,text="Cases")
        l2.grid(row=0,column=2)

        l3=Label(t,text="GPU")
        l3.grid(row=1,column=0)

        l4=Label(t,text="CPU")
        l4.grid(row=1,column=2)

        l5=Label(t,text="Motherboard")
        l5.grid(row=2,column=0)

        l6=Label(t,text="PowerSupply")
        l6.grid(row=2,column=2)

        l7=Label(t,text="Memory")
        l7.grid(row=3,column=0)

        l8=Label(t,text="Active")
        l8.grid(row=3,column=2)

        

        Price_text=StringVar()
        e1=Entry(t,textvariable=Price_text)
        e1.grid(row=0,column=1)

        Cases_text=StringVar()
        e2=Entry(t,textvariable=Cases_text)
        e2.grid(row=0,column=3)

        GPU_text=StringVar()
        e3=Entry(t,textvariable=GPU_text)
        e3.grid(row=1,column=1)

        CPU_text=StringVar()
        e4=Entry(t,textvariable=CPU_text)
        e4.grid(row=1,column=3)

        Motherboard_text=StringVar()
        e5=Entry(t,textvariable=Motherboard_text)
        e5.grid(row=2,column=1)

        PowerSupply_text=StringVar()
        e6=Entry(t,textvariable=PowerSupply_text)
        e6.grid(row=2,column=3)

        Memory_text=StringVar()
        e7=Entry(t,textvariable=Memory_text)
        e7.grid(row=3,column=1)

        Active_text=StringVar()
        e8=Entry(t,textvariable=Active_text)
        e8.grid(row=3,column=3)

        #creating a listbox and scrollbar

        list1=Listbox(t, height=15,width=120)
        list1.grid(row=5,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(t)
        sb1.grid(row=5,column=2,rowspan=8)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        list1.bind('<<ListboxSelect>>',get_selected_row)

        #creating the buttons

        b1=ttk.Button(t,text="View", width=12,command=view_command)
        b1.grid(row=5,column=3)

        b2=ttk.Button(t,text="Search", width=12,command=search_command)
        b2.grid(row=6,column=3)

        b3=ttk.Button(t,text="Add", width=12,command=add_command)
        b3.grid(row=7,column=3)

        b4=ttk.Button(t,text="Update", width=12,command=update_command)
        b4.grid(row=8,column=3)

        b5=ttk.Button(t,text="Delete", width=12,command=delete_command)
        b5.grid(row=9,column=3)

        b6=ttk.Button(t,text="Exit", width=12,command=t.destroy)
        b6.grid(row=10,column=3)

        t.mainloop()

##################################################################################################################################################  
    def showAll(self):
        t = tk.Toplevel(self)
        t.geometry("500x600")

        button = ttk.Button(t, text="Exit", command=t.destroy)
        button.pack(side="bottom", padx=200, pady=10)

        #Createing a frame 
        myContainer = Frame(t)
        myContainer.pack()


        #Connect to database
        
        db = sqlite3.connect ("D:\Computer Science\Coursework\MODULE 3COSC002W.Y The Computer and Software Development\Semester 2\Final work\PC.db")
        
        s = "Select * from PC"

        cursor = db.cursor()
        cursor.execute(s)
        rows = cursor.fetchall()
        print (len(cursor.fetchall()))
        for row in rows:
                print(row)
                
        numrows =(len(rows))
        print (len(rows))

        
        BigFont=font.Font(family="Calibri(Body)", size=10, weight="bold")
        HeaderFont = font.Font(family="Calibri(Body)", size=10, weight="bold") 

        #creating the header and label list 

        HLabel1 = Label(myContainer, text = "Price", font=HeaderFont)
        HLabel2 = Label(myContainer, text = "Cases", font=HeaderFont)
        HLabel3 = Label(myContainer, text = "GPU", font=HeaderFont)
        HLabel4 = Label(myContainer, text = "CPU", font=HeaderFont)
        HLabel5 = Label(myContainer, text = "Motherboard", font=HeaderFont)
        HLabel6 = Label(myContainer, text = "PowerSupply", font=HeaderFont)
        HLabel7 = Label(myContainer, text = "Memory", font=HeaderFont)
        HLabel8 = Label(myContainer, text = "Active", font=HeaderFont)
        HLabelTop = Label(myContainer, text= "List of Builds", font=BigFont, fg="royal blue")

        HLabelTop.grid(row = 0, column = 1, columnspan = 8)

        HLabel1.grid(row = 1, column = 1)
        HLabel2.grid(row = 1, column = 2)
        HLabel3.grid(row = 1, column = 3)
        HLabel4.grid(row = 1, column = 4)
        HLabel5.grid(row = 1, column = 5)
        HLabel6.grid(row = 1, column = 6)
        HLabel7.grid(row = 1, column = 7)
        HLabel8.grid(row = 1, column = 8)

        #set of lists to hold each field of data
        Price=[]
        Cases=[]
        GPU=[]
        CPU=[]
        Motherboard=[]
        Memory=[]
        PowerSupply=[]
        Active=[]
        for a in range(numrows):
            myLabel1 = Label(myContainer, text = rows[a][1]) 
            Price.append(myLabel1)
            myLabel2 = Label(myContainer, text = rows[a][2])
            Cases.append(myLabel2)
            myLabel3 = Label(myContainer, text = rows[a][3])
            GPU.append(myLabel3)

            myLabel4 = Label(myContainer, text = rows[a][4])
            CPU.append(myLabel4)
            myLabel5 = Label(myContainer, text = rows[a][5])
            Motherboard.append(myLabel5)
            myLabel6 = Label(myContainer, text = rows[a][6])
            PowerSupply.append(myLabel6)
            myLabel7 = Label(myContainer, text = rows[a][7])
            Memory.append(myLabel7)
            myLabel8 = Label(myContainer, text = str(rows[a][8]))
            Active.append(myLabel8)

            Price[a].grid(row=a+2, column=1, sticky=W)
            Cases[a].grid(row=a+2, column=2, sticky=W)
            GPU[a].grid(row=a+2, column=3, sticky=W)
            CPU[a].grid(row=a+2, column=4, sticky=W)
            Motherboard[a].grid(row=a+2,column=5, sticky=W)
            PowerSupply[a].grid(row=a+2, column=6, sticky=W)
            Memory[a].grid(row=a+2, column=7, sticky=W)
            Active[a].grid(row=a+2, column=8, sticky=W)

##########################################################################################################################################################################################################################################################################


    def quit(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
####################################################################
    #creates a menu tab at the top to the window
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
####################################################################
    
    root.title("PC Builder")
    root.geometry("600x400")
    text_label = Label(root, text = "Customise Your PC!")
    text_label.pack()
    Pc = PhotoImage(file = "PC Part Picker.png")
    w1 = Label(root, image = Pc).pack(side = "top")
    
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
    


