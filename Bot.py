from hashlib import new
from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
tempo = 0

url = 'http://diario.ac.gov.br/'

# abrindo navegador e passando o endereço
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# buscando elemento de download por click
download_capa = driver.find_element(By.CLASS_NAME, 'pdficon')

# buscando o número do diário para uso posterior
numero_diario = driver.find_element(By.CLASS_NAME, 'txt-hj-pequeno')
numero_diario = numero_diario.text.split()
numero_diario = int(numero_diario[3]) - 1

# iniciando o loop para baixar os pdf's

while numero_diario > 13180:  # 13072:
    caixa_busca = driver.find_element(By.ID, "numero")
    caixa_busca.click()
    sleep(2)
    caixa_busca.clear()
    caixa_busca.send_keys(numero_diario)
    caixa_busca.send_keys(Keys.ENTER)
    download_arquivo = driver.find_elements(
        By.CSS_SELECTOR, '[title="Fazer download"]')
    cont = len(download_arquivo) - 1
    while cont > -1:
        sleep(2)
        download_arquivo[cont].click()
        cont = cont - 1
    numero_diario = numero_diario - 1
    driver.delete_all_cookies()
    sleep(2)


done = True
while done == True:
    local = os.chdir('/home/thiago/Downloads')
    arquivos = sorted(os.listdir(local))
    num_arquivos = len(arquivos) - 1
    cont = 0
    while num_arquivos > cont:
        teste = arquivos[cont]
        if teste.endswith('.crdownload'):
            print(teste)
        cont = cont + 1
        sleep(10)
        print('esperando 10 segundos...')
if not teste.endswith('.crdownload'):
    done = False
