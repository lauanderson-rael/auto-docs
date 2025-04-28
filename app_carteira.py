from docx import Document
import os
import tkinter as tk
from tkinter import messagebox

def fechar_janela():
    print("fechar")
    root.destroy()


# Função para gerar a carteira
def gerar_carteira():
    nome_pai = entradas["Nome do Pai"].get()
    nome_mae = entradas["Nome da Mãe"].get()
    nome_rua = entradas["Nome da Rua e Nº"].get()
    nome_bairro = entradas["Nome do Bairro"].get()
    naturalidade = entradas["Naturalidade"].get()
    data_nasc = entradas["Data de Nascimento"].get()
    estado_civil = entradas["Estado Civil"].get()
    num_rg = entradas["Número do RG"].get()
    # Garantir que o RG tenha 14 caracteres
    num_rg = num_rg.ljust(15)
    num_cpf = entradas["Número do CPF"].get()
    data_emissao = entradas["Data de Emissão"].get()
    numero_sind = entradas["Número de Inscrição"].get()
    nome_local = entradas["Local/Cidade"].get()
    nome_socio = entradas["Nome Completo"].get()

    # Caminho para o arquivo Word
    caminho_arquivo = './assets/sociocart2.docx'
    # Verifique se o arquivo de entrada existe
    if not os.path.exists(caminho_arquivo):
        messagebox.showerror("Erro", "O arquivo de entrada 'sociocart2.docx' não foi encontrado!")
        return

    # Carregar o documento
    doc = Document(caminho_arquivo)

    # Definindo as informações para substituição
    substituicoes = {
        "NOME_PAI": nome_pai,
        "NOME_MAE": nome_mae,
        "NOME_RUA": nome_rua,
        "NOME_BAIRRO": nome_bairro,
        "NATURALIDADE": naturalidade,
        "DATA_NASC": data_nasc,
        "EST_CIVIL": estado_civil,
        "12345678900000": num_rg,
        "123.456.789": num_cpf,
        "DATA_EMISS": data_emissao,
        "N_SIND": numero_sind,
        "NOME_LOCAL": nome_local,
        "NOME_SOCIO": nome_socio,
    }

    # Substituir no conteúdo dos parágrafos
    for para in doc.paragraphs:
        for run in para.runs:  # Manter a formatação do texto
            for texto_antigo, texto_novo in substituicoes.items():
                if texto_antigo in run.text:
                    run.text = run.text.replace(texto_antigo, texto_novo)

    # Criar nova pasta se não existir e salvar o arquivo
    nova_pasta = os.path.join("carteiras_socio_geradas")
    os.makedirs(nova_pasta, exist_ok=True)
    novo_arquivo = os.path.join(nova_pasta, f"{entradas["Nome Completo"].get()}.docx")
    doc.save(novo_arquivo)
    messagebox.showinfo("Sucesso", "A carteira foi criada com sucesso!")

# interface grafica
root = tk.Tk()
root.title("Gerador de Carteira de Sócio")
root.config(padx=70, pady=5)

# Header
tk.Label(root, text="Gerador de Carteira de Sócio", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 5))
tk.Label(root, text="Será gerada a carteira com os dados preenchidos", font=("Arial", 10, "bold"), fg="red").grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Lista de campos (label, variável para entrada)
campos = [
    "Nome do Pai",
    "Nome da Mãe",
    "Nome da Rua e Nº",
    "Nome do Bairro",
    "Naturalidade",
    "Data de Nascimento",
    "Estado Civil",
    "Número do RG",
    "Número do CPF",
    "Data de Emissão",
    "Número de Inscrição",
    "Local/Cidade",
    "Nome Completo"
]

# Dicionário para armazenar os widgets de entrada
entradas = {}

# Criando os labels e entradas com for
for i, campo in enumerate(campos):
    tk.Label(root, text=f"{campo}:").grid(row=i+2, column=0, padx=10, pady=5)
    entrada = tk.Entry(root, width=50)
    entrada.grid(row=i+2, column=1, padx=10, pady=5)
    entradas[campo] = entrada

btn_gerar = tk.Button(root, text="Gerar Carteira", bg="azure3", command=gerar_carteira)
btn_gerar.grid(row=len(campos)+2, column=1, padx=10, pady=20, sticky='w')

btn_fechar = tk.Button(root, text="Sair", command=fechar_janela, bg='red', fg='white', width=10)
btn_fechar.grid(row=len(campos)+2, column=1, padx=10, pady=20, sticky='e')


root.mainloop()
