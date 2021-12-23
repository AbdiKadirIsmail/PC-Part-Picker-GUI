import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sqlite3
from tkinter import font
from tkinter import messagebox

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

self.button1 = tk.Button(self, text="Show All",command=self.showAll)
self.button2 = tk.Button(self, text="Add New",command=self.addNewWindow)
self.button3 = tk.Button(self, text="Amend",command=self.amend)
self.button4 = tk.Button(self, text="Delete",command=self.delete)
self.button5 = tk.Button(self, text = 'Quit Application', command=self.quit)
#Show the buttons created
self.button1.pack(side="top", fill="both", expand=True, padx=200, pady=10)
self.button2.pack(side="top", fill="both", expand=True, padx=200, pady=10)
self.button3.pack(side="top", fill="both", expand=True, padx=200, pady=10)
self.button4.pack(side="top", fill="both", expand=True, padx=200, pady=10)
self.button5.pack()

# Main window completed.
def addNewWindow(self):
    t = tk.Toplevel(self)
    t.wm_title(" New Student - Data Entry")
    global IDentry, NameEntry, WHOEntry, GradeEntry, ActiveEntry

myContainer = Frame(t)
myContainer.pack(side=TOP, expand=YES, fill=BOTH)

#Create the entry boxes for data input and show them
IDentry = Entry(myContainer)
NameEntry = Entry(myContainer)
WHOEntry = Entry(myContainer)
GradeEntry = Entry(myContainer)
ActiveEntry = Entry(myContainer)

IDentry.grid(row = 1, column = 1)
NameEntry.grid(row = 2, column = 1)
WHOEntry.grid(row = 3, column = 1)
GradeEntry.grid(row = 4, column = 1)
ActiveEntry.grid(row = 5, column = 1)

#Define the fonts to be used for display
BigFont=font.Font(family="Arial", size=14, weight="bold") # Font for Big Labels
HeaderFont = font.Font(family="Arial", size=12, weight="bold") #Font for header

#Create the label to be used and show them
HLabel1 = Label(myContainer, text = "ID", fg = "blue", font=HeaderFont)
HLabel2 = Label(myContainer, text = "Name", fg = "blue", font=HeaderFont)
HLabel3 = Label(myContainer, text = "WHO", fg = "blue", font=HeaderFont)
HLabel4 = Label(myContainer, text = "Grade", fg = "blue", font=HeaderFont)
HLabel5 = Label(myContainer, text = "Active", fg = "blue", font=HeaderFont)
HLabelTop = Label(myContainer, text= "New Student", font=BigFont, fg="red")

HLabel1.grid(row = 1, column = 0)
HLabel2.grid(row = 2, column = 0)
HLabel3.grid(row = 3, column = 0)
HLabel4.grid(row = 4, column = 0)
HLabel5.grid(row = 5, column = 0)
HLabelTop.grid(row = 0, column = 0, columnspan = 5)

#Create a separate additional frame to hold the buttons, however button 3 is attached to first frame?
myBtnContainer = Frame(t)
myBtnContainer.pack(side=TOP, expand=YES, fill=BOTH)

button1 = tk.Button(myBtnContainer, text="Add Student", command=self.Add, width=15)
button2 = tk.Button(myBtnContainer, text="Clear Entries", command=self.ClearEntries, width=15)
button3 = tk.Button(myContainer, text="Exit", command=t.destroy, width=15)
button1.grid(row = 1, column = 1)
button2.grid(row = 1, column = 2)
button3.grid(row = 3, column = 2)


def Add(self):
    #Check if any of the data is missing and create an alert - messagebox
    if IDentry.get() == "" or NameEntry.get() == "" or WHOEntry == "" or \
       GradeEntry.get() == "" or ActiveEntry.get() == "" :
        messagebox.showerror("Bad Data", "Some Or All Required\nFields Are Blank")
        return
#db =  sqlite3.connect ("C:\\Users\lukkag\Desktop\week 8\MWPy\databaseLabs\student.db")

        ##Good idea to display ALL records from the table in the console:
s = "Select * from student"
cursor = db.cursor()
cursor.execute(s)
rows = cursor.fetchall()
print (len(cursor.fetchall()))
for row in rows:
    print("$$$: ",row)
    ## Let's find out how many rows are in our result set
    numrows =(len(rows)) # cursor.rowcount
    print (len(rows))


##Get the new data and formulate the sql string to add the record:
s = "insert into student(id, Fname, Lname, mark) "
s = s + "values ('" + IDentry.get() + "', '" + NameEntry.get() + "', '" + WHOEntry.get() + "', '" + GradeEntry.get()+ "');"

print(s)

cursor = db.cursor()


cursor.execute(s)
cursor.close()
db.commit()
db.close()


def ClearEntries(self):
    print("clear addnew data")
    IDentry.delete(0, END)
    NameEntry.delete(0,END)
    WHOEntry.delete(0,END)
    GradeEntry.delete(0,END)
    ActiveEntry.delete(0,END)

def amend(self):
    t = tk.Toplevel(self)
    t.wm_title("Amend Exiting Student")
    t.geometry("500x100")
    myContainer = Frame(t)
    myContainer.pack(side=TOP, expand=YES, fill=BOTH)


BigFont=font.Font(family="Arial", size=14, weight="bold") # Font for Big Labels
HeaderFont = font.Font(family="Arial", size=12, weight="bold") #Font for header
HLabelTop = Label(myContainer, text= "Amend Existing Student - To be written", font=BigFont, fg="red")
HLabelTop.grid(row = 1, column = 1, columnspan = 5)



def delete(self):
    t = tk.Toplevel(self)
    t.wm_title("Delete Exiting Student")
    t.geometry("500x100")
    myContainer = Frame(t)
    myContainer.pack(side=TOP, expand=YES, fill=BOTH)


BigFont=font.Font(family="Arial", size=14, weight="bold") # Font for Big Labels
HeaderFont = font.Font(family="Arial", size=12, weight="bold") #Font for header
HLabelTop = Label(myContainer, text= "Delete Existing Student - To be written", font=BigFont, fg="red")
HLabelTop.grid(row = 1, column = 1, columnspan = 5)


def showAll(self):
    t = tk.Toplevel(self)
    l = tk.Label(t, text="All students past and present who have taken this module" )
    l.pack(side="top", fill="both", expand=True, padx=100, pady=10)

button = tk.Button(t, text="Exit", command=t.destroy)
button.pack()

        # Create a frame to hold the controls with a fixed height & width
myContainer = Frame(t)
myContainer.pack(side=TOP, expand=YES, fill=BOTH)
        
        ##Connect to database - path set for demo in the lecture
        ##Make sure to change this to where you create the student database
        
        #db = sqlite3.connect ("C:\\Users\lukkag\Desktop\week 8\MWPy\databaseLabs\student.db")
        
s = "Select * from student"

cursor = db.cursor()
cursor.execute(s)
rows = cursor.fetchall()
print (len(cursor.fetchall()))
for row in rows:
    print(row)
        ## Let's find out how many rows are in our result set
numrows =(len(rows)) ##cursor.rowcount
print (len(rows))

        # Put the Header Information on the Page
BigFont=font.Font(family="Arial", size=14, weight="bold") # Font for Big Labels
HeaderFont = font.Font(family="Arial", size=12, weight="bold") #Font for header

        #Create column headings for data display

HLabel1 = Label(myContainer, text = "ID", fg = "blue", font=HeaderFont)
HLabel2 = Label(myContainer, text = "Name", fg = "blue", font=HeaderFont)
HLabel3 = Label(myContainer, text = "WHO", fg = "blue", font=HeaderFont)
HLabel4 = Label(myContainer, text = "Grade", fg = "blue", font=HeaderFont)
HLabel5 = Label(myContainer, text = "Active", fg = "blue", font=HeaderFont)
HLabelTop = Label(myContainer, text= "All Students", font=BigFont, fg="red")

HLabelTop.grid(row = 0, column = 0, columnspan = 5)
HLabel1.grid(row = 1, column = 0)
HLabel2.grid(row = 1, column = 1)
HLabel3.grid(row = 1, column = 2)
HLabel4.grid(row = 1, column = 3)
HLabel5.grid(row = 1, column = 4)

        # Use a set of lists to hold each field of data
ID = []
Name=[]
Who=[]
Grade=[]
Active=[]

for a in range(numrows):
    data = rows[a][0]
    myLabel1 = Label(myContainer, text = data)
    ID.append(myLabel1)
    myLabel2 = Label(myContainer, text = rows[a][1])
    Name.append(myLabel2)

myLabel3 = Label(myContainer, text = rows[a][2])
Who.append(myLabel3)
myLabel4 = Label(myContainer, text = rows[a][3])
Grade.append(myLabel4)
myLabel5 = Label(myContainer, text = str(rows[a][4]))
Active.append(myLabel5)

ID[a].grid(row=a+2, column=0, sticky=W)
Name[a].grid(row=a+2, column=1, sticky=W)
Who[a].grid(row=a+2, column=2, sticky=W)
Grade[a].grid(row=a+2, column=3, sticky=W)
Active[a].grid(row=a+2, column=4, sticky=W)


def quit(self):
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Records")
    root.geometry("500x400")
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)

root.mainloop()


