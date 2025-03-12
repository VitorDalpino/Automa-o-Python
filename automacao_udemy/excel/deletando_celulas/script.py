from openpyxl import load_workbook

nome_arquivo = r"G:\Meu Drive\MeusProjetos\projetos_py\automacao_udemy\excel\deletando_celulas\book.xlsx"
wb = load_workbook(filename=nome_arquivo)

ws = wb['Data']
ws.delete_rows(1)
ws.delete_cols(1)

wb.save(filename=nome_arquivo)