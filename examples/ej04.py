
from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
   response = requests.get(url)
   return response.text


def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_="card-content")
    return items



def get_item_data(item):
    try:  
          title = item.find("h2", class_="title").text
    except:
          title = ''
    try:  
          fecha = item.find("time").text
    except:
          fecha = ''

    data = {'title': title, 'fecha': fecha}
    return data



def write_csv(i, data):
    with open('notebooks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'], data['fecha']))
        print(i+1, data['title'], data['fecha'], 'parsed')



def main():
   print("Iniciando...")
   url = 'https://realpython.github.io/fake-jobs/'
   pagina = get_html(url)
   #print(pagina)
   all_items = get_all_items(pagina)
   #print(all_items)
   for i, item in enumerate(all_items):
       data = get_item_data(item)
       #print(data)
       write_csv(i, data)


if __name__ == '__main__':
   main()