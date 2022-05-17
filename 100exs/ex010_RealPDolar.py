from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Parte pra pegar cotação do dólar no momento
navegador = webdriver.Chrome()
navegador.get('https://www.google.com/')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolarstr = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
dolar = float(dolarstr)
sleep(5)
# Programa principal
real = float(input('Quanto você tem em reais? R$'))
dol = real/dolar
print(f'Com R${real:,.2f} você conseguiria agora U${dol:,.2f}')