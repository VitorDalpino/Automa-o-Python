from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

ws['A1'] = "Você vai ver uma imagem abaixo"
caminho_imagem = r"G:\Meu Drive\MeusProjetos\projetos_py\automacao_udemy\excel\imagens\logo_py.png"
img = Image(caminho_imagem)

ws.add_image(img,'A2')

caminho_saida = r"G:\Meu Drive\MeusProjetos\projetos_py\automacao_udemy\excel\imagens\logo.xlsx"
wb.save(filename=caminho_saida)