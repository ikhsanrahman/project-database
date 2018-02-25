import sqlite3
import os


conn=sqlite3.connect('database.db')
cur=conn.cursor()

cur.execute (''' CREATE TABLE Produk(kode INTEGER NOT NULL,
										nama VARCHAR(25),
										harga FLOAT,
										PRIMARY KEY(kode)
			)''')


cur.execute("INSERT INTO Produk VALUES (1, 'Pensil', 6000)")
cur.execute("INSERT INTO Produk VALUES (2, 'Spidol', 12000)")
cur.execute("INSERT INTO Produk VALUES (3, 'Penggaris', 5000)")


print "made a database have done well"
conn.commit()
cur.close()
conn.close()
exit()