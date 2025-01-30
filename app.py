from fillpdf import fillpdfs

camposPDF1 = list(fillpdfs.get_form_fields('edit1.pdf').keys())
campos = list(fillpdfs.get_form_fields('edit2.pdf').keys())
print("nomes dos campos: ", campos)
print("nomes dos campos: ", camposPDF1)

nome = " Lauanderson Rael 2"
data_nasc = '10/05/2099'
nome_mae = "Maria Silva"
cpf = "758.874.112-45"
rg = '8373566232003-0'
pis = "7763893478738"
cei = '677736764/87'
rua = " Rua X"
n = '344'
bairro = " Anil"
rgp = cpf.replace(".", "").replace("-", "")

#edit 1
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

# edit 2
data_dict = {
    campos[0]: nome,
    campos[6]: cpf,
    campos[4]: rg,
    campos[5]: f"{rua}, {n}",
    campos[7]: bairro
}

fillpdfs.write_fillable_pdf('edit1.pdf','new_edit1.pdf',data_dict1)
fillpdfs.write_fillable_pdf('edit2.pdf','new_edit2.pdf',data_dict)
