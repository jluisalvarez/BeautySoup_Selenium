# Selenium en Python

## References

https://selenium-python.readthedocs.io/

https://www.oak-tree.tech/blog/python-web-scraping-selenium

https://www.youtube.com/playlist?list=PLas30d-GGNa3YgAUAzpf-dnZxeSH1f1-m

## Instalación

Crear entorno

```
$ py -m venv entorno

$ entorno\Scripts\activate

(entorno) $

```
Instalar selenium

```
(entorno) pip install selenium

```


## Ejemplo: Primer Script

En el núcleo de Selenium es el WebDriver que permite manejar un navegador de forma nativa, como lo haría un usuario.

```python

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()

```

## Aspectos básicos

Esta guía se desarrolla con Chrome, para usar otros navegadores consultar: https://www.selenium.dev/documentation/webdriver/browsers/

### Iniciar y finalizar el WebDriver

```python

driver = webdriver.Chrome()

...

driver.quit()

```

### Navegar a una página

```python
...
url = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(url)
...
```

### Definir estrategia de espera

Espera implicita

```python
...
driver.implicitly_wait(0.5)
...
```

Espera explicita

```python

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
...
driver.get(url)

# Espera hasta que se detecte la presencia del elemento con id = ResultsContainer
elements = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ResultsContainer"))
)

```

Para otras opciones consultar: https://www.selenium.dev/documentation/webdriver/waits/

### Buscar elementos y realizando acciones

```python
...
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()
...
```

### Obtener información de la página o de un elemento

```python
...
title = driver.title

text= driver.find_element(by=By.ID, value="my-text")
text = message.text
...
```

## Buscando elementos

El WebDriver nos facilita diferentes métodos para buscar:

find_element(By by)  - Busca el primer elemento
find_elements(By by) - Busca todos los elementos

El parámetro By se obtiene desde:

```
from selenium.webdriver.common.by import By
```

y puede tomar los siguientes valores:

```
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
```

### ID

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
</html>

```
```python
# Elemento con id = loginForm
login_form = driver.find_element(By.ID, 'loginForm')
```

### Name

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
</html>
```

```python
# Elemento con name = username
username = driver.find_element(By.NAME, 'username')
# Elemento con name = password
password = driver.find_element(By.NAME, 'password')
```

```python
# Primer elemento con name = continue, esto es Login no el Clear
continue = driver.find_element(By.NAME, 'continue')
```

### XPATH

La búsqueda por XPATH puede ser consultada mediante el inspector de objetos, con click derecho, Copiar y XPATH

```
elto = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[1]/div/div[1]/h4")

```
```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
</html>
```

```python
# Ruta absoluta al formulario
login_form = driver.find_element(By.XPATH, "/html/body/form[1]")

# Primer formulario en el HTML
login_form = driver.find_element(By.XPATH, "//form[1]")
 
# Formulario con atributo id = loginForm
login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")
```

```python
# Elemento input cuyo atributo name = username del primer formulario
username = driver.find_element(By.XPATH, "//form[input/@name='username']")
# Primer input del formulario con id = loginForm
username = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]")
# Primer input cuyo atributo name = username
username = driver.find_element(By.XPATH, "//input[@name='username']")
```

```python
# Dos formas de obtener el elemento Clear
clear_button = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")
```

### Links

```html
<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
</html>
```
```python
# Dos formas de obtener el link cuyo text es Continue o incluye Conti
continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
```

### Tagname

```html
<html>
 <body>
  <h1>Welcome</h1>
  <p>Site content goes here.</p>
</body>
</html>
```
```python
# Primer elemento con etiqueta h1
heading1 = driver.find_element(By.TAG_NAME, 'h1')
```

### Class name

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
</html>
```

```python
# Primer elemento con class = content (el párrafo)
content = driver.find_element(By.CLASS_NAME, 'content')
```

### CSS Selector
```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
</html>
```

```python
# Primer elemento con selector CSS etiqueta párrafo class content
content = driver.find_element(By.CSS_SELECTOR, 'p.content')
```

## Interactuar con elementos

```html
<input type="text" name="passwd" id="passwd-id" />
```

```python
# Cuatro formas de acceder al elemento
element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")
```
Asignar valor a un elemento input

```python
element.send_keys("some text")
element.send_keys(" and some", Keys.ENTER)
```

```html
<input type="submit" name="btnK" value="Enviar" />
```
```python 
boton = driver.find_element(By.NAME, "btnK")
boton.click()
```


