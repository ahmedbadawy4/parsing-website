##### -*- coding: utf-8 -*-
from flask import Flask, jsonify
from scraping import scrape
import requests
#source = requests.get("https://www.myfitness.lv/en/club/domina/class-schedule/").text
#soup = BeautifulSoup(source, 'lxml')
#tbody = soup.find('tbody')
#all = soup.find('tbody').select_one('td')
#all = soup.find('tbody').find_all('tr')
#print(all)
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify(Products=scrape())
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
#app = Flask(__name__, template_folder='.')