from flask import Flask, render_template, request, url_for, redirect
import requests
import json
from index import *

app = Flask(__name__)

@app.route('/')
def home():
    r = requests.get('https://api.quran.sutanlab.id/surah')
    data = r.json()
    home = data['data']
    return render_template('index.html', len = len(home), home = home)

@app.route('/surah')
def back():
    return redirect('/')

@app.route('/surah/<id>')
def surah(id):
    ayatke = id
    r = requests.get('https://api.quran.sutanlab.id/surah/'+ayatke)
    arrayku = r.json()
    if arrayku['code'] == 404 :
        return redirect('/')
    else:
        quran = {
            'asma': arrayku['data']['name']['short'],
            'arti': arrayku['data']['name']['translation']['id'],
            'nama': arrayku['data']['name']['transliteration']['id'],
        }
        ayat = arrayku['data']['verses']
        return render_template('surah.html', quran=quran, len = len(ayat), ayat = ayat)

@app.route('/pymonad', methods=['POST', 'GET'])
def pymonad():

    if request.method == "GET":
        return render_template('pymonad.html')

    if request.method == "POST":

        angka1 = request.form['pertama']
        angka2 = request.form['kedua']
        pilih = request.form['pilihan']
        if angka1 == '' or angka2 == '' or pilih == '':
            pesan = 'Input Tidak Boleh Kosong'
            return render_template('pymonad.html', pesan=pesan)

        # bagian select pilihan
        if pilih == 'tambah':
            data = pertambahan(int(angka1), int(angka2))
        elif pilih == 'kali':
            data = perkalian(int(angka1), int(angka2))
        elif pilih == 'kurang':
            data = pengurangan(int(angka1), int(angka2))
        else:
            data = pembagian(int(angka1), int(angka2))

        return render_template('pymonad.html', data=data)

@app.route('/pymonad-multi', methods=['POST', 'GET'])
def pymonad_multi():

    if request.method == "GET":
        return redirect('/pymonad')

    if request.method == "POST":

        pertama = request.form['angka_x']
        if pertama == '':
            pesan = 'Input Tidak Boleh Kosong'
            return render_template('pymonad-multi.html', pesan=pesan)

        data = new_func(int(pertama))
        return render_template('pymonad-multi.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)