from lib2to3.pgen2.driver import Driver
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

# buscando o número do diário para uso posterior
numero_diario = driver.find_element(By.CLASS_NAME, 'txt-hj-pequeno')
numero_diario = numero_diario.text.split()
numero_diario = numero_diario[3]
print(numero_diario)

# encontrando a caixa de busca por número, passando o numero e a tecla enter
caixa_busca = driver.find_element(By.ID, "numero")
caixa_busca.click()
caixa_busca.send_keys(numero_diario)
caixa_busca.send_keys(Keys.ENTER)
sleep(10)

# buscando o arquivo para download

download = driver.find_element(By.PARTIAL_LINK_TEXT, "http://diario.ac.gov")
download.click()

driver.close()
