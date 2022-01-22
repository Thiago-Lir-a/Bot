from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


url = 'http://diario.ac.gov.br/'

# abrindo navegador e passando o endereço
driver = webdriver.Chrome()
driver.get(url)

# buscando elemento de download por click
download_capa = driver.find_element(By.CLASS_NAME, 'pdficon')
# download_capa.click()

# buscando o número do diário para uso posterior
numero_diario = driver.find_element(By.CLASS_NAME, 'txt-hj-pequeno')
numero_diario = numero_diario.text.split()
numero_diario = int(numero_diario[3]) - 1

# iniciando o loop para baixar os pdf's

while numero_diario > 13072:
    caixa_busca = driver.find_element(By.ID, "numero")
    caixa_busca.click()
    caixa_busca.clear()
    caixa_busca.send_keys(numero_diario)
    caixa_busca.send_keys(Keys.ENTER)
    download = driver.find_elements(
        By.CSS_SELECTOR, '[title="Fazer download"]')
    cont = len(download) - 1
    while cont > -1:
        download[cont].click()
        cont = cont - 1
    numero_diario = numero_diario - 1

# encontrando a caixa de busca por número, passando o numero e a tecla enter
