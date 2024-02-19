import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

items = soup.find_all('div', {'class':'card'})

print(items[0])

print(items[0].find('h2').text)
print(items[0].find('h3').text)
print(items[0].find('time').text)
print(items[0].find('a', {'class':'card-footer-item'}).get_text())
print(items[0].find('a', {'class':'card-footer-item'})["href"])

