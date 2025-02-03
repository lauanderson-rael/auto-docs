import os
import tkinter as tk
from tkinter import filedialog, messagebox
from fillpdf import fillpdfs

def gerar_pdfs():
    if not verificar_campos():
        return  # nao continua

    nome = entry_nome.get()
    data_nasc = entry_data_nasc.get()
    nome_mae = entry_nome_mae.get()
    nome_pai = entry_nome_pai.get()
    cpf = entry_cpf.get()
    rg = entry_rg.get()
    data_emissao_rg = entry_data_emissao_rg.get()
    pis = entry_pis.get()
    cei = entry_cei.get()
    rua = entry_rua.get()
    n = entry_numero.get()
    bairro = entry_bairro.get()
    sexo_fem = var_sexo.get() == "F"
    rgp = cpf.replace(".", "").replace("-", "")

    try:
        camposPDF1 = list(fillpdfs.get_form_fields(pdf1_path).keys())
        camposPDF2 = list(fillpdfs.get_form_fields(pdf2_path).keys())
        camposPDF3 = list(fillpdfs.get_form_fields(pdf3_path).keys())

        data_dict1 = {
            camposPDF1[0]: nome,
            camposPDF1[1]: data_nasc,
            camposPDF1[2]: nome_mae,
            camposPDF1[3]: cpf,
            camposPDF1[4]: rg,
            camposPDF1[5]: pis,
            camposPDF1[6]: cei,
            camposPDF1[7]: rua,
            camposPDF1[8]: n,
            camposPDF1[9]: bairro,
            camposPDF1[22]: rgp,
        }

        data_dict2 = {
            camposPDF2[0]: nome,
            camposPDF2[6]: cpf,
            camposPDF2[4]: rg,
            camposPDF2[5]: f"{rua}, {n}",
            camposPDF2[7]: bairro,
        }

        data_dict3 = {
            camposPDF3[1]: nome,
            camposPDF3[2]: cpf,
            camposPDF3[3]: rg,
            camposPDF3[4]: data_emissao_rg,
            camposPDF3[5]: data_nasc,
            camposPDF3[6]: nome_pai,
            camposPDF3[7]: nome_mae,
            camposPDF3[8]: pis,
            camposPDF3[9]: f'{rua}, {n}',
            camposPDF3[10]: bairro,
            camposPDF3[13]: rgp,
            camposPDF3[15]: 'x' if sexo_fem else '',
            camposPDF3[16]: 'x' if not sexo_fem else '',
            camposPDF3[19]: nome,
            camposPDF3[20]: cpf,
        }

        output_dir = f"./arquivos_gerados/{cpf}"
        os.makedirs(output_dir, exist_ok=True)

        fillpdfs.write_fillable_pdf(pdf1_path, f'{output_dir}/requerimento.pdf', data_dict1)
        fillpdfs.write_fillable_pdf(pdf2_path, f'{output_dir}/anexoIII.pdf', data_dict2)
        fillpdfs.write_fillable_pdf(pdf3_path, f'{output_dir}/FLPP.pdf', data_dict3)

        messagebox.showinfo("Sucesso", "AnexoIII.pdf,  requerimento.pdf  e  FLPP.pdf \nGerados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


# verificacao de campos
def verificar_campos():
    for entry in entries:
        if entry.get().strip() == "":
            messagebox.showwarning("Campo vazio", "Por favor, preencha todos os campos.")
            return False
    return True


# interface grafica
root = tk.Tk()
root.title("Preenchimento de PDFs")

# título H1
tk.Label(root, text="Bot preenchedor de pdfs", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(root, text="Sera preenchido e GERADO os pdfs: AnexoIII, requerimento e FLPP", font=("Arial", 10, "bold"),fg="red").grid(row=1, column=0, columnspan=2, pady=0)

labels = ["Nome Completo", "Data de Nascimento", "Nome da Mãe", "Nome do Pai", "CPF (com ou sem  .  e  -)", "RG (somente números)", "Data Emissão RG", "PIS/NIS/NIT", "Nº Matricula CEI", "Rua", "Nº da casa", "Bairro"]
entries = []

# Preenchendo os campos com Labels e Entry
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i+2, column=0, padx=5, pady=5)
    entry = tk.Entry(root, width=70)
    entry.grid(row=i+2, column=1, padx=5, pady=5)
    entries.append(entry)

entry_nome, entry_data_nasc, entry_nome_mae, entry_nome_pai, entry_cpf, entry_rg, entry_data_emissao_rg, entry_pis, entry_cei, entry_rua, entry_numero, entry_bairro = entries

var_sexo = tk.StringVar(value="M")
tk.Label(root, text="Sexo").grid(row=len(labels)+2, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="Masculino", variable=var_sexo, value="M").grid(row=len(labels)+2, column=1, padx=5, pady=5)
tk.Radiobutton(root, text="Feminino", variable=var_sexo, value="F").grid(row=len(labels)+3, column=1, padx=5, pady=5)

btn_gerar = tk.Button(root, text="Gerar PDFs", command=gerar_pdfs)
btn_gerar.grid(row=len(labels)+4, column=0, columnspan=2, pady=10)

pdf1_path = "edit1.pdf"
pdf2_path = "edit2.pdf"
pdf3_path = "edit3.pdf"

root.mainloop()
