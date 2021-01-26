from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    r = requests.get('https://api.quran.sutanlab.id/surah')
    data = r.json()
    home = data['data']
    return render_template('index.html', len = len(home), home = home)

@app.route('/surah/<id>')
def surah(id):
    ayatke = id
    r = requests.get('https://api.quran.sutanlab.id/surah/'+ayatke)
    arrayku = r.json()
    quran = {
        'asma': arrayku['data']['name']['short'],
        'arti': arrayku['data']['name']['translation']['id'],
        'nama': arrayku['data']['name']['transliteration']['id'],
    }
    ayat = arrayku['data']['verses']
    return render_template('surah.html', quran=quran, len = len(ayat), ayat = ayat)

if __name__ == "__main__":
    app.run(debug=True)