#                                           Parsing
# parsing - process of automatically collecting data 
# libraries
# 1. requests - sends request to a website and gets smth
# 2. BeautifulSoup -helps to get information from html. helps to adress certain tags and get data from them
# 3. lxml - is used as a parser for bs (analyzes data)
# python3 -m venv venv - create virtual environement
# source venv/bin/activate - activate virtual env (or . venv/bin/activate)


import requests
from bs4 import BeautifulSoup as bs
import csv

url = 'https://enter.kg/computers/noutbuki_bishkek'

def write_csv(data):
    with open('data.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([data['title'],data['price'],data['image']])

def get_html(url):
    response = requests.get(url)
    return response.text
def get_data(html):
    soup = bs(html,'lxml')
    rows = soup.find_all('div', 'row')
    dict_ = []
    for i in rows:
        title = i.find('span', 'prouct_name').text
        price = i.find('span', 'price').text
        img = 'https://enter.kg'+i.img.get('src')
        dict_={'title':title, 'price':price,'image':img}
        write_csv(dict_)
count = 1
while True:
    print(f'count - {count}')
    get_data(get_html(url))
    count += 1
