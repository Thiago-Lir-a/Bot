from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import options
url = 'https://proceedings.science/cbee7/papers'

driver = webdriver.Chrome()
driver.get(url)


contatos = driver.find_elements(By.CSS_SELECTOR, '[class="panel-body"]')
print(contatos[0])
