from flask import Flask, request, render_template, redirect
from models import Produk
import os
import sqlite3



Database=os.getcwd() + '/database.db'

app=Flask(__name__)

@app.route('/')
def index():
	conn=sqlite3.connect(Database)
	cur=conn.cursor()
	container=[]
	for kode, nama, harga in cur.execute('SELECT * FROM Produk'):
		model=Produk(kode, nama, harga)
		container.append(model)
	conn.commit()
	cur.close()
	conn.close()
	return render_template('index.html', container=container, model=model)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
	if request.method=='POST':
		kode=int(request.form['kode'])
		nama=request.form['nama']
		harga=float(request.form['harga'])
		model=Produk(kode, nama, harga)
		model.tambah()
		return redirect('/')
	else :
		return render_template('tambah_form.html')

@app.route('/ubah/<int:id>', methods=['GET', 'POST'])
def ubah(id):
	model=Produk()
	model.load(id)
	if request.method=='POST':
		kode=int(request.form['kode'])
		nama=request.form['nama']
		harga=float(request.form['harga'])
		model.setKode(kode)
		model.setNama(nama)
		model.setHarga(harga)
		model.ubah()
		return redirect('/')
	else :
		return render_template('Ubah.html', model=model)


@app.route('/hapus/<int:id>')
def delete(id):
	model=Produk()
	model.load(id)
	model.hapus()
	return redirect ('/')



if __name__ == '__main__':
	app.run(debug=True)