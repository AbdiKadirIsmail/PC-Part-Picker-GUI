import sqlite3

def connect():
    conn=sqlite3.connect("PC.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS PC (id INTEGER PRIMARY KEY, Price integer, Cases text, GPU text, CPU text, Motherboard text, PowerSupply text, Memory text, Active integer)") 
    conn.commit()
    conn.close()

def insert(Price,Cases,GPU,CPU,Motherboard,PowerSupply,Memory,Active): 
	conn=sqlite3.connect("PC.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO PC VALUES (NULL,?,?,?,?,?,?,?,?)",(Price,Cases,GPU,CPU,Motherboard,PowerSupply,Memory,Active)) 
	conn.commit()
	conn.close()
	view()

def view():
    conn=sqlite3.connect("PC.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM PC")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Price="",Cases="",GPU="",CPU="",Motherboard="",PowerSupply="",Memory="",Active=""):
    conn=sqlite3.connect("PC.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM PC WHERE Price=? OR Cases=? OR GPU=? OR CPU=? OR Motherboard=? OR PowerSupply=? OR Memory=? OR Active=?", (Price,Cases,GPU,CPU,Motherboard,PowerSupply,Memory,Active))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("PC.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM PC WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,Price,Cases,GPU,CPU,Motherboard,PowerSupply,Memory,Active):
    conn=sqlite3.connect("PC.db")
    cur=conn.cursor()
    cur.execute("UPDATE PC SET Price=?, Cases=?, GPU=?, CPU=?, Motherboard=?, PowerSupply=?,Memory=?, Active=? WHERE id=?",(Price,Cases,GPU,CPU,Motherboard,PowerSupply,Memory,Active,id))
    conn.commit()
    conn.close()

connect()
