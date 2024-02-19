
from selenium import webdriver

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

# Obtener el título
titulo = driver.title
print(titulo)

driver.quit()