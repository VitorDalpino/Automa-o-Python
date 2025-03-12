from openpyxl import Workbook

print("Iniciando nosso robô...")
print("Lendo dados do arquivo de texto...")

# Abrindo o arquivo de texto corretamente
with open(r"C:\Users\vitor\OneDrive\Documentos\MeusProjetos\projetos_py\automacao_udemy\excel\txt-excel\gastos.txt", encoding="utf-8") as file_txt:
    arquivo = file_txt.read()

# Separando os dados em linhas e colunas
lista_dados = [linha.split(",") for linha in arquivo.splitlines()]

# Criando arquivo Excel
print("Criando arquivo Excel...")
wb = Workbook()
ws = wb.active

# Adicionando os dados ao arquivo Excel
for row in lista_dados:
    ws.append(row)

# Salvando o arquivo Excel
wb.save("gastos.xlsx")
print("Arquivo Excel criado com sucesso!")
