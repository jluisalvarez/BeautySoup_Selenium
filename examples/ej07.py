
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)

    
url = 'http://localhost:8080/ej/'


driver.get(url)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "formulario"))
)

search_input = driver.find_element("name", "nombre")
boton = driver.find_element("id", "boton")

#search_input.send_keys("Pepe", Keys.ENTER)

search_input.send_keys("Pepe")
boton.submit()

print(driver.page_source)
