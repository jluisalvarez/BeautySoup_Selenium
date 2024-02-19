from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")

import time

import requests
from bs4 import BeautifulSoup

import pandas as pd

driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://bookauthority.org/")

time.sleep(2)

search = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/div/div/div/div[3]/div/span[1]')
search.click()

time.sleep(3)

input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/input')

input.send_keys("Computer Science")
time.sleep(2)
input.send_keys(Keys.ENTER)

time.sleep(6)
print(driver.current_url)
h1 = driver.find_element(By.CLASS_NAME, 'pageTitle')

print(h1.text)

div = driver.find_element(By.CLASS_NAME, 'books')

books = div.find_elements(By.CSS_SELECTOR, '.book')

titles = []
authors = set()

i=0
for book in books:
    i=i+1
    if i<=5:
        titulo = book.find_element(By.TAG_NAME, 'h2')
        #print("-", titulo.text)
        titles.append(titulo.text)
        anio = book.find_element(By.CSS_SELECTOR, 'span.date')
        print(anio.text[2:])
        rating = book.find_element(By.CSS_SELECTOR, 'span.our-rating')
        print(rating.text)
        autores = book.find_element(By.CSS_SELECTOR, 'h3.authors')
        nombres = autores.find_elements(By.TAG_NAME, 'a')
        j=1
        print('\t', end='')
        for n in nombres:
            authors.add(n.text)
            if j<len(nombres):
                print(n.text, end=', ')
            else:
                print(n.text)
            j=j+1

#print(authors)
driver.quit()

db = pd.DataFrame()
print(db)
