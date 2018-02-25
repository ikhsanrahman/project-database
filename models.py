import sqlite3
import os


Database=os.getcwd() + '/database.db'

class Produk(object):
	def __init__(self, kode=0, nama='', harga=0):
		self.kode=kode
		self.nama=nama
		self.harga=harga

	def setKode(self, kode):
		self.kode=kode

	def setNama(self, nama):
		self.nama=nama

	def setHarga(self, harga):
		self.harga=harga

	def tambah(self):
		conn=sqlite3.connect(Database)
		cur=conn.cursor()
		cur.execute("INSERT INTO Produk VALUES(?,?,?)", (self.kode, self.nama, self.harga))

		conn.commit()
		cur.close()
		conn.close()

	def ubah(self):
		conn=sqlite3.connect(Database)
		cur=conn.cursor()
		cur.execute('''UPDATE Produk SET nama=?, harga=? WHERE kode=?''', (self.nama, self.harga, self.kode))

		conn.commit()
		cur.close()
		conn.close()

	def hapus(self):
		conn=sqlite3.connect(Database)
		cur=conn.cursor()
		cur.execute('''DELETE FROM Produk WHERE kode=?''', (self.kode))

		conn.commit()
		cur.close()
		conn.close()

	def load(self, id):
		conn=sqlite3.connect(Database)
		cur=conn.cursor()
		for kode, nama, harga in cur.execute("SELECT * FROM Produk"):
			if kode==id:
				self.kode=kode
				self.nama=nama
				self.harga=harga

		conn.commit()
		cur.close()
		conn.close()


		