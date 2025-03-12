from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd;
print('Iniciando nosso robô...')

#Lendo do excel
file_path = 'dominio.xlsx'
df = pd.read_excel(file_path)
dominios = df.iloc[:,0]
# print(dominios);

# workbook = xlrd.open_workbook('dominio.xlsx')
# sheet = workbook.sheet_by_index(0)
# print(sheet.cell_value(0,0))

# driver = webdriver.Chrome() # Entrar no Google

# driver.get('https://registro.br') # Entrar no site 

# dominios = ["roboscompython.com.br","udemy.com", "uol.com.br", "pythoncurso.com"];
# for dominio in dominios:
#     pesquisa = driver.find_element(By.ID, "is-avail-field") # Achar a barra de pesquisa
#     pesquisa.clear() # Limpar a barra de pesquisa
#     pesquisa.send_keys(dominio) # Escrever a string dentro da barra
#     pesquisa.send_keys(Keys.RETURN) # Apertar o ENTER
#     time.sleep(2)
#     resultados = driver.find_elements(By.TAG_NAME,'strong')
#     print('Dominio %s %s ' % (dominio,resultados[2].text))


# driver.close()