

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")

import time

driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.imdb.com/search/title/")

time.sleep(2)

aceptar = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/button[2]')
aceptar.click()

time.sleep(2)

dd = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')

dd.click()

time.sleep(2)

#p = driver.find_element(By.XPATH, "//button[@data-testid='test-chip-id-movie']") 

p = driver.find_element(By.XPATH, "//*[@id='accordion-item-titleTypeAccordion']/div/section/button[1]") 
p.click()

time.sleep(2)


r = driver.find_element(By.XPATH, "//*[@id='__next']/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]") 
r.click()

time.sleep(2)

results = driver.find_element(By.CSS_SELECTOR, "ul[role='presentation']")

l = results.find_elements(By.TAG_NAME, "li")

i=1
for option in l:
    i=i+1
    try:
        titulo = option.find_element(By.TAG_NAME, "h3")
        ranking = option.find_element(By.CSS_SELECTOR, "span[data-testid='ratingGroup--imdb-rating']")

        v = ranking.text[0:3]
        fv = float(v.replace(',', '.'))
        if fv > 7.5:
            print(titulo.text, v)

    except:
        pass

time.sleep(5)

driver.quit()

