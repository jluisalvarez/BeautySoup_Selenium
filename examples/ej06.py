
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

    
    
url = 'https://www.tcgplayer.com/'


driver.get(url)

elements = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located((By.ID, "autocomplete-input"))
)

search_input = driver.find_element("name", "acInput")

search_input.send_keys("Pokemon", Keys.ENTER)

print(driver.page_source)





           
