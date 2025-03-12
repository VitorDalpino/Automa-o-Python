import pyautogui
import time
import subprocess
import os

# Configurações globais
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Abrir navegador diretamente
url = "https://www.gabrielcasemiro.com.br/atividade_pyautogui"
subprocess.run(["start", "chrome", url], shell=True)

# Aguarda a página carregar
time.sleep(7)  # Ajuste conforme necessário

# Verifica se o arquivo existe
csv_path = "membros.csv"
if not os.path.exists(csv_path):
    pyautogui.alert("Arquivo CSV não encontrado!", "Erro")
    exit()

# Processamento do arquivo CSV
with open(csv_path, encoding="utf-8") as f:
    next(f)  # Pula o cabeçalho
    
    for line in f:
        line = line.strip().split(";")
        
        # Verifica se os dados estão corretos
        if len(line) < 4:
            print("Linha inválida:", line)
            continue

        name, sex, email, phone = line
        print(f"Processando: {name}, {sex}, {email}, {phone}")

        def click_image(image, confidence=0.8, duration=1):
            """Localiza e clica na imagem, evitando erros."""
            try:
                x, y = pyautogui.locateCenterOnScreen(f"img\\{image}.png", confidence=confidence)
                pyautogui.click(x, y, duration=duration)
            except TypeError:
                print(f"Erro: {image} não encontrado.")

        # Preenchendo os campos
        click_image("nome")
        pyautogui.typewrite(name, interval=0.25)

        click_image("email")
        pyautogui.typewrite(email, interval=0.25)

        click_image("telefone")
        pyautogui.typewrite(phone, interval=0.25)

        click_image("sexo")
        if sex.lower() == "masculino":
            click_image("masculino")
        else:
            click_image("feminino")

        # Captura de tela para registro
        pyautogui.screenshot(f"cadastro_{name}.png")

        # Clica no botão de envio
        click_image("botao_enviar")
        time.sleep(3)  # Aguarda processamento

# Exibe alerta ao finalizar
pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")
