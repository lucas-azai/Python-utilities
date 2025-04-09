import pdfplumber
import pandas as pd
import re


def extract_data_from_pdf(pdf_path):
    data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                person_data = {}
                
                for line in lines:
                    
                    if line.startswith("Nome:"):
                        if person_data:  
                            data.append(person_data)
                        person_data = {"Nome": line.replace("Nome:", "").strip()}
                    elif line.startswith("Endereço:"):
                        person_data["Endereço"] = line.replace("Endereço:", "").strip()
                    elif line.startswith("Cidade:"):
                        person_data["Cidade"] = line.replace("Cidade:", "").strip()
                    elif "Telefone:" in line:
                        person_data["Telefone"] = line.split("Telefone:")[1].strip()
                    elif "CEL:" in line:
                        person_data["CEL"] = line.split("CEL:")[1].strip()
                    elif "Fax:" in line:
                        person_data["Fax"] = line.split("Fax:")[1].strip()
                    elif "E-mail:" in line:
                        person_data["E-mail"] = line.split("E-mail:")[1].strip()
                    elif "CPF:" in line:
                        person_data["CPF"] = line.split("CPF:")[1].strip()
                    elif "RG:" in line:
                        person_data["RG"] = line.split("RG:")[1].strip()
                    elif "CNPJ:" in line:
                        person_data["CNPJ"] = line.split("CNPJ:")[1].strip()
                    elif "INSCRIÇÃO ESTADUAL:" in line:
                        person_data["INSCRIÇÃO ESTADUAL"] = line.split("INSCRIÇÃO ESTADUAL:")[1].strip()
                
                if person_data:
                    data.append(person_data)
    
    return data

# Caminho do PDF
pdf_path = "C:\\Users\\lucas.azai\\Downloads\\NomedoPDF.pdf"  # Substituir pelo caminho correto

# Extrair os dados
data = extract_data_from_pdf(pdf_path)

# Converter para DataFrame
df = pd.DataFrame(data)

# Salvar para Excel
df.to_excel("dados_extraidos.xlsx", index=False)

print("Extração concluída! Os dados foram salvos em 'dados_extraidos.xlsx'")
