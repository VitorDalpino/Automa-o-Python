import PyPDF2
from openpyxl import Workbook

# Abrir o arquivo PDF
pdf_file = open(r"G:\Meu Drive\MeusProjetos\projetos_py\automacao_udemy\excel\pdf-excel\tabela_despesas.pdf", "rb")

# Ler o PDF
read_pdf = PyPDF2.PdfReader(pdf_file)

# Obter o número de páginas
number_of_pages = len(read_pdf.pages)

# Pegar o conteúdo da primeira página
page = read_pdf.pages[0]
page_content = page.extract_text()

# Processar o texto
parsed = page_content.splitlines()
parsed = [x for x in parsed if x.strip()]  # Removendo linhas vazias

# Criar a lista de dados organizados
lista_dados = []
for i in range(0, len(parsed) - 2, 3):
    lista_dados.append([parsed[i], parsed[i+1], parsed[i+2]])

# Criar o arquivo Excel
print("Criando arquivo Excel...")
wb = Workbook()
ws = wb.active

# Adicionar os dados na planilha
for row in lista_dados:
    ws.append(row)

# Salvar o arquivo Excel
wb.save(filename="gastos.xlsx")

# Fechar o arquivo PDF
pdf_file.close()

print("Arquivo Excel criado com sucesso!")
