
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")

# En primer plano
#driver = webdriver.Chrome()
# En Segundo plano
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://selenium.dev")

# Espera implicita para que los elementos de la página estén disponibles
driver.implicitly_wait(0.5)


opcion1 = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[1]/div/div[1]/h4")
opcion2 = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[2]/div/div[1]/h4")
opcion3 = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[3]/div/div[1]/h4")

print(opcion1.text)
print(opcion2.text)
print(opcion3.text)


driver.quit()