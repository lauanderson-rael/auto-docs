import os
from docx import Document
doc = Document("residencia.docx")


#local 1
texto_nome = 'GERIVALDO BARBOSA'
texto_cpf = 'Cadastro de Pessoas Físicas (CPF) sob o nº'
texto_rg = 'Carteira de Identidade (RG) nº'
texto_endereco = 'no endereço:'

#dados
cpf = '123.456.789-22'
nome = 'LAUANDERSON RAEL COSTA GOMES'
sexoF = True
nacionaldade = 'BRASILEIRA' if sexoF else 'BRASILEIRO'
estado_civil = 'UNÃO ESTÁVEL'
rua_e_numero = 'RUA SAO BRAZ, 45'
bairro = 'ANIL'

# Percorrer os parágrafos para encontrar a palavra desejada e adicionar texto
# for para in doc.paragraphs:
#     if texto_nome in para.text: 
        


# Salvar as alterações
nova_pasta = 'salvos'
os.makedirs(nova_pasta, exist_ok=True)
caminho_arquivo = os.path.join(nova_pasta, f"{cpf}_residencia.docx")
doc.save(caminho_arquivo)
