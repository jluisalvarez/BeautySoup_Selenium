from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()

driver.get("https://www.google.com")

titulo = driver.title
print(titulo)

# Encontrar elemento por ID
aceptar = driver.find_element(By.ID, "L2AGLb")
aceptar.click()

#assert titulo=='Google'

# Retardo de 0.5 segundos
driver.implicitly_wait(0.5)

# Encontrar elemento por nombre
texto = driver.find_element(By.NAME, "q")
boton = driver.find_element(By.NAME, "btnK")

texto.send_keys("Selenium")
boton.click()

buscado = driver.find_element(By.NAME, "q")
# Obtener el valor de un atributo (value) de un elemento
valor = buscado.get_attribute("value")
print(valor)


driver.close()