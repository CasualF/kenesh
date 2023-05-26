import csv
import requests
from bs4 import BeautifulSoup as bs

def write_csv(data):
    with open('kenesh.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([data['title'],data['date'],data['image'],data['description']])
def get_html(url):
    response = requests.get(url)
    return response.text
for i in range(20):
    url = f'http://kenesh.kg/ru/news/all/list?page={i+1}'
    access = get_html(url)
    page = bs(access,'lxml')
    news = page.find_all('div','news__item news__item__3')
    for i in news:
        title = i.h3.text
        date = i.find('div','news__item__date').text
        try:
            img = 'kenesh.kg'+i.find('img','news__item__image__img').get('src')
        except:
            img = None
        link = 'http://kenesh.kg'+i.a.get('href')
        d_page = bs(get_html(link),'lxml')
        des = d_page.find('div','ck-editor').find_all('p')
        des2 = " ".join([i.text for i in des])
        ls = {'title':title,'date': date,'image':img,'description':des2}
        write_csv(ls)
