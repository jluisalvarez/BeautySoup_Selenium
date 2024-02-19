
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)

for page in range(1, 3):
    
    
    url = 'https://www.ebay.com/b/Dell-Laptops-Netbooks/175672/bn_2780156?_pgn='+str(page)

    print("Página:", str(page), "url:", url )

    driver.get(url)

    elements = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "mainContent"))
    )


    soup = BeautifulSoup(driver.page_source, 'lxml')
    items = soup.find("ul", {"class": "b-list__items_nofooter"}).findAll("li", {"class": "s-item"})

    for i, item in enumerate(items):
        pc = item.find({"h3": "b-s-item__title"}).text
        price = item.find("span", {"class": "s-item__price"}).text
        try:
            pvp = float(price[1:])
            if pvp<100  and " SSD " in pc:
                print(i+1, pc, ' - Precio:', pvp )
        except:
            pass

           
