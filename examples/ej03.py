
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)



url = 'https://realpython.github.io/fake-jobs/'

driver.get(url)

elements = WebDriverWait(driver, 5).until(

    EC.presence_of_element_located((By.ID, "ResultsContainer"))

)


soup=BeautifulSoup(driver.page_source, "html.parser")

job_elements = soup.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    print(title_element.text)
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print("\t"+link.text+": "+link_url)
