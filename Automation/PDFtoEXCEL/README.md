📄 Descrição Geral

✨Este script automatiza a extração de dados estruturados (como nome, endereço, CPF, telefone, etc.) a partir
de arquivos PDF com texto formatado em linhas contendo esses campos. Após a extração, os dados são
convertidos em um DataFrame do pandas e salvos em um arquivo Excel.

📚Bibliotecas Utilizadas

- pdfplumber: Para leitura e extração de texto de arquivos PDF.
- pandas: Para manipulação e exportação dos dados em formato tabular.
- re: Para eventuais expressões regulares (importada, mas não utilizada neste trecho de código).

🔧Funções

extract_data_from_pdf(pdf_path)

Descrição:
Extrai informações de pessoas (ou entidades) de um PDF com campos como "Nome", "Endereço", "Cidade",
"Telefone", etc.

Parâmetros:
- pdf_path (str): Caminho para o arquivo PDF que será processado.

Retorno:
- data (list of dict): Lista de dicionários, cada um representando os dados de uma pessoa ou entidade.
Lógica de Funcionamento:

	1. Abre o PDF e percorre página por página.
	2. Para cada página, extrai o texto e divide em linhas.
	3. Cada linha é verificada para identificar se contém algum dos campos esperados.
	4. Quando uma nova entrada é detectada com "Nome:", inicia um novo dicionário de dados.
	5. Os dados coletados são adicionados a uma lista.
	6. Ao final, a lista é retornada.

📁Exemplo de Uso

pdf_path = "C:\Users\lucas.azai\Downloads\PContraria.pdf"
data = extract_data_from_pdf(pdf_path)
df = pd.DataFrame(data)
df.to_excel("dados_extraidos.xlsx", index=False)
print("Extração concluída! Os dados foram salvos em 'dados_extraidos.xlsx'")


📝 Formato Esperado no PDF

O script espera que o texto no PDF contenha linhas iniciadas por:
- Nome:
- Endereço:
- Cidade:
- Telefone:
- CEL:
- Fax:
- E-mail:
- CPF:
- RG:
- CNPJ:
- INSCRIÇÃO ESTADUAL:

Cada campo deve estar em uma linha separada e bem identificado por esses rótulos.

💾Saída

- Arquivo gerado: dados_extraidos.xlsx
- Formato: Planilha Excel com colunas correspondentes aos campos extraídos.
Observações
- Certifique-se de que o PDF contenha texto selecionável (não é imagem escaneada).
- O script não realiza validação dos dados extraídos (como formato de CPF ou e-mail).
- Para PDFs com layout diferente ou campos adicionais, o script precisará ser adaptado.


✅ Instalação com um comando
Você pode instalar todas as dependências de uma vez com:

	pip install pdfplumber pandas openpyxl

ou faça o clone do repositorio e utilize o pip install -r requirements.txt pelo terminal