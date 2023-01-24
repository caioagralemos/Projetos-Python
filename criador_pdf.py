from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 8)

nome_arquivo = input("Coloque o seu arquivo no diretório desse programa e passe o nome do arquivo com a .extensão: ")

try:
    f = open(f"{nome_arquivo}", "r")
except:
    print("Algo deu errado.")
    exit()
else:
    text = f.read()

barran = text.count('\n')
ponto = text.count('.')

if barran >= 1:
    paragraph = text.split("\n")
    ct = 1
    for p in paragraph:
        pdf.cell(200,10,txt=paragraph[ct-1],ln=ct,align="L")
        ct+=1
else:
    dot = text.split(".")
    ct = 1
    for d in dot:
        pdf.cell(200,10,txt=dot[ct-1],ln=ct,align="L")
        ct+=1

nome_pdf = input("Nome do seu novo arquivo PDF sem a terminação: ")
pdf.output(f"{nome_pdf}.pdf")


