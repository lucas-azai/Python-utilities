# 📄 Combinar PDFs e Imagens JPEG em um único PDF


✅ Dependências de instalação

PyPDF2	Leitura e manipulação de arquivos PDF	pip install PyPDF2
Pillow	Abrir e converter imagens JPEG em PDF	pip install Pillow


Este script Python combina múltiplos arquivos PDF e imagens JPEG em um único arquivo PDF consolidado.

---

## 🔧 Funcionalidade

- Junta todas as páginas de arquivos PDF encontrados em um diretório.
- Converte imagens JPEG/JPG em páginas PDF e as inclui no final.
- Remove arquivos temporários gerados durante o processo.
- Gera um único arquivo chamado `relacao.pdf`.

---

## 📂 Estrutura Esperada

Todos os arquivos (PDFs e imagens JPEG) devem estar em uma única pasta.

📁 SUA PASTA ├── arquivo1.pdf ├── arquivo2.pdf ├── imagem1.jpeg ├── imagem2.jpg

yaml
Copiar
Editar

---

## 🚀 Como usar

1. Altere a variável `pasta` no código para o caminho desejado:
    ```python
    pasta = "C:\\Users\\seu_usuario\\Desktop\\SUA PASTA"
    ```
2. Execute o script com Python.

3. O PDF combinado será salvo como `relacao.pdf` no mesmo diretório onde o script foi executado.

---

## 📦 Dependências

pip install -r requirements.txt