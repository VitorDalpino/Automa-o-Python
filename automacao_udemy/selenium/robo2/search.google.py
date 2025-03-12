from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

pesquisa = input("Digite a pesquisa: ")


driver = webdriver.Chrome()
driver.get("https://www.google.com")

campo = driver.find_element(By.XPATH, "//textarea[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)
input("Pressione Enter para sair...")
driver.quit()