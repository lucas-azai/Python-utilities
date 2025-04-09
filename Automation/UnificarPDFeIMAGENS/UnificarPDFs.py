import PyPDF2
from PIL import Image
import os

def combinar_pdfs_imagens(lista_pdfs, lista_imagens, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()
    
    # Adiciona páginas de PDF
    for pdf in lista_pdfs:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    
    image_pdfs = []
    for image_path in lista_imagens:
        image = Image.open(image_path)
        # Converte a imagem para PDF
        pdf_path = f"{image_path}.pdf"
        image.convert("RGB").save(pdf_path)
        image_pdfs.append(pdf_path)
        # Adiciona o PDF gerado a partir da imagem
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        pdf_writer.add_page(pdf_reader.pages[0])
    
   
    with open(output_pdf, 'wb') as output:
        pdf_writer.write(output)
    
   
    for pdf in image_pdfs:
        os.remove(pdf)

    print("PDFs e imagens combinados com sucesso!")

# Especifica o diretório onde estão os arquivos
pasta = "C:\\Users\\lucas.azai\\Desktop\\SUA PASTA"  # Altere para o caminho da pasta com PDFs e JPEGs

G
lista_pdfs = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.pdf')]
lista_imagens = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.jpeg') or f.endswith('.jpg')]

output_pdf = 'relacao.pdf'


combinar_pdfs_imagens(lista_pdfs, lista_imagens, output_pdf)
