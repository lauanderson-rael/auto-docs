from fillpdf import fillpdfs
# localizando campos
camposPDF1 = list(fillpdfs.get_form_fields('edit1.pdf').keys())
camposPDF2 = list(fillpdfs.get_form_fields('edit2.pdf').keys())
camposPDF3 = list(fillpdfs.get_form_fields('edit3.pdf').keys())

#dados necessarios
sexo_fem = False
nome = " Joao Silva Batista Silva"
data_nasc = '10/05/1997'
nome_mae = "Maria Silva Batista Assuncao"
nome_pai = "Jose Silva Batista Assuncao"
cpf = "058.874.112-45"
rg = '8373566232003-0'
data_emissao_rg = '23/09/2022'
pis = "7763893478738"
cei = '677736764/87'
rua = " Rua Presidente Dutra"
n = '344'
bairro = " Centro"
rgp = cpf.replace(".", "").replace("-", "")

#edit1.pdf
data_dict1 ={
    camposPDF1[0]: nome,
    camposPDF1[1]: data_nasc,
    camposPDF1[2]:nome_mae,
    camposPDF1[3]:cpf,
    camposPDF1[4]:rg,
    camposPDF1[5]:pis,
    camposPDF1[6]:cei,
    camposPDF1[7]:rua,
    camposPDF1[8]:n,
    camposPDF1[9]:bairro,
    camposPDF1[22]:rgp,
}

# edit2.pdf
data_dict2 = {
    camposPDF2[0]: nome,
    camposPDF2[6]: cpf,
    camposPDF2[4]: rg,
    camposPDF2[5]: f"{rua}, {n}",
    camposPDF2[7]: bairro
}

#edit3.pdf
data_dict3 = {
    camposPDF3[2]: nome,
    camposPDF3[3]: cpf,
    camposPDF3[4]: rg,
    camposPDF3[5]: data_emissao_rg,
    camposPDF3[6]: data_nasc,
    camposPDF3[7]: nome_pai,
    camposPDF3[8]: nome_mae,
    camposPDF3[9]: pis,
    camposPDF3[11]: f'{rua}, {n}',
    camposPDF3[12]:bairro,
    camposPDF3[18]:rgp,
    camposPDF3[20]:'RIO PARNAÍBA',
    camposPDF3[24]: 'x' if sexo_fem else '',
    camposPDF3[25]: 'x' if sexo_fem == False else '',
    camposPDF3[32]: nome,
    camposPDF3[33]:cpf,
}

fillpdfs.write_fillable_pdf('edit1.pdf',f'./arquivos_gerados/{rgp}_requerimento.pdf',data_dict1)
fillpdfs.write_fillable_pdf('edit2.pdf',f'./arquivos_gerados/{rgp}_anexoIII.pdf',data_dict2)
fillpdfs.write_fillable_pdf('edit3.pdf',f'./arquivos_gerados/{rgp}_FLPP.pdf',data_dict3)
