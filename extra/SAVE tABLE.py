import sqlite3

conn = sqlite3.connect('PC.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE PC("Price" integer NOT NULL,
"Case" varchar(225) NOT NULL,
"GPU" varchar(225) NOT NULL,
"CPU" varchar(225) NOT NULL,
"Motherboard" varchar(255) NOT NULL,
"PowerSupply" varchar(255) NOT NULL,
"Active" tinyint(1) NOT NULL DEFAULT '1');''')
print ("Table created successfully");

conn.close()
