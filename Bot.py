from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


url = 'http://diario.ac.gov.br/'

# abrindo navegador e passando o endereço
driver = webdriver.Chrome()
driver.get(url)

# buscando elemento de download por click
download_capa = driver.find_element(By.CLASS_NAME, 'pdficon')
download_capa.click()

# buscando elemento de
numero_diario = driver.find_element(By.CLASS_NAME, 'txt-hj-pequeno')
print(numero_diario)

sleep(50)
driver.close()
