# BeautySoup y Selenium


### REFERENCES


https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://realpython.com/beautiful-soup-web-scraper-python/
https://aprendepython.es/pypi/scraping/beautifulsoup/
https://pythonalgos.com/2021/11/20/web-scraping-the-easy-way-python-selenium-beautiful-soup/

https://selenium-python.readthedocs.io/

https://www.oak-tree.tech/blog/python-web-scraping-selenium

https://www.youtube.com/playlist?list=PLas30d-GGNa3YgAUAzpf-dnZxeSH1f1-m


## Python

```
$ py -V
Python 3.10.9

$ py --list
Installed Pythons found by py Launcher for Windows
 -3.10-64 *
```

```
$ py -m venv entorno

$ entorno\Scripts\activate

(entorno) $

```


```
(entorno) $ pip install beautifulsoup4
```

```
(entorno) $ pip freeze
beautifulsoup4==4.12.2
soupsieve==2.5
```

```
(entorno) pip install requests
```

```
(entorno) $ pip freeze
beautifulsoup4==4.12.2
certifi==2023.11.17
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
soupsieve==2.5
urllib3==2.1.0
```

```
(entorno) pip install selenium

```

```
(entorno) $ pip freeze
attrs==23.2.0
beautifulsoup4==4.12.2
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
exceptiongroup==1.2.0
h11==0.14.0
idna==3.6
outcome==1.3.0.post0
pycparser==2.21
PySocks==1.7.1
requests==2.31.0
selenium==4.16.0
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.5
trio==0.23.2
trio-websocket==0.11.1
urllib3==2.1.0
wsproto==1.2.0
```


```
(entorno) $ pip install webdriver_manager
```

```
(entorno) $ pip freeze
attrs==23.2.0
beautifulsoup4==4.12.2
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
exceptiongroup==1.2.0
h11==0.14.0
idna==3.6
outcome==1.3.0.post0
packaging==23.2
pycparser==2.21
PySocks==1.7.1
python-dotenv==1.0.0
requests==2.31.0
selenium==4.16.0
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.5
trio==0.23.2
trio-websocket==0.11.1
urllib3==2.1.0
webdriver-manager==4.0.1
wsproto==1.2.0
```

```
(entorno) $ pip install lxml
```

## Ejemplo 1

```python
import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)
```

## Ejemplo 2

```python
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

# print(results.prettify())

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    print(title_element.text)
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print("\t"+link.text+": "+link_url)
```

## Ejemplo 3

```python
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

```

