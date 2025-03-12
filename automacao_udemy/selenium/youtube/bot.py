from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RoboYouTube():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        self.webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def busca(self, busca):
        url = f"https://www.youtube.com/results?search_query={busca}"
        self.webdriver.get(url)

        # Aguarda a exibição dos resultados (miniaturas dos vídeos)
        try:
            WebDriverWait(self.webdriver, 10).until(
                EC.presence_of_element_located((By.ID, "video-title"))
            )
            print("Resultados carregados!")
        except:
            print("Tempo limite atingido. Nenhum resultado encontrado.")
            return
        
        # Corrigindo a busca pelos títulos dos vídeos
        titulos = self.webdriver.find_elements(By.XPATH, "//a[@id='video-title']")
        for i, titulo in enumerate(titulos[:5]):  # Mostra os 5 primeiros resultados
            print(f"Vídeo {i+1}: {titulo.text}")

# Executando o robô
bot = RoboYouTube()
bot.busca("teste")

input("Pressione Enter para sair...")
bot.webdriver.quit()
