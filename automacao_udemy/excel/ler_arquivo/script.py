from openpyxl import load_workbook

wb = load_workbook(filename=r"C:\Users\vitor\OneDrive\Documentos\MeusProjetos\projetos_py\automacao_udemy\excel\ler_arquivo\nomes.xlsx")

planilha = wb['Planilha1']

# print(planilha['A2'].value)

for i in range(2,5):
    print("%s tem %s anos." % (planilha['A%s' % i].value,planilha['B%s' % i].value) )