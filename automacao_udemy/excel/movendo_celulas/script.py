from openpyxl import load_workbook

#Escolheno o arquivo
dest_filename =r'G:\Meu Drive\MeusProjetos\projetos_py\automacao_udemy\excel\movendo_celulas\book.xlsx'
wb = load_workbook(filename=dest_filename)
ws = wb['Data']

#Move a linha 2(De A até Z) uma para cima
ws.move_range("A2:Z2", rows=-1)

#Move f8 duas colunas para a direita
ws.move_range("F8:F8", cols=2)

#Move f10 duas colunas para a esquerda
ws.move_range("F10:F10", cols=-2)

#Duas para esquerda e uma para cima
ws.move_range("C13:E15", cols=-2, rows=-1)

wb.save(filename=dest_filename)