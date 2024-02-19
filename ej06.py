
import time

import requests
from bs4 import BeautifulSoup


URL = "https://bookauthority.org/books/best-computer-science-books"
print(URL)
page = requests.get(URL)
print(page.content)
time.sleep(6)
soup = BeautifulSoup(page.content, "lxml")
time.sleep(6)
items = soup.find('div', {'class':'books'})

print(items)


