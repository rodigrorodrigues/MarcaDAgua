# Adicionar Marca d'Água em PDF

Este projeto é uma aplicação em Python que permite adicionar marcas d'água a arquivos PDF. Ele utiliza as bibliotecas `PyPDF2` para manipulação de PDFs e `reportlab` para criação de conteúdo PDF. A interface gráfica é construída utilizando `tkinter` e `ttkbootstrap`.

## Funcionalidades

- Seleção de arquivo PDF.
- Inserção de texto para a marca d'água.
- Definição do nome do arquivo de saída.
- Adição de marca d'água com texto personalizado.
- Abertura automática da pasta contendo o arquivo de saída após a conclusão.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `tkinter`
  - `ttkbootstrap`
  - `PyPDF2`
  - `reportlab`
  - `Pillow`

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/rodrigorodrigues/MarcaDAgua.git
   cd MarcaDAgua
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Execute o script principal:

   ```sh
   python main.py
   ```

2. Na interface gráfica:
   - Clique em "Selecionar" para escolher um arquivo PDF.
   - Insira o texto da marca d'água.
   - Defina o nome do arquivo de saída.
   - Clique em "Adicionar Marca d'Água" para gerar o PDF com a marca d'água.

## Estrutura do Projeto

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch com a sua feature: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m 'Adiciona minha feature'`.
4. Faça um push para a branch: `git push origin minha-feature`.
5. Abra um Pull Request.

## Autor

Rodrigo Rodrigues

[https://www.linkedin.com/in/rodrigodevrodrigues/](https://www.linkedin.com/in/rodrigodevrodrigues/)
