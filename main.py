import tkinter as tk
from tkinter import messagebox

# Funções para abrir as janelas correspondentes
def abrir_filiacao_residencia():
    from auto_word import index

def abrir_requerimento():
    from auto_pdf import app

def fechar_janela():
    print("saindo do sistema!..")
    root.destroy()

#  janela principal
root = tk.Tk()
root.title("Menu Principal")
root.geometry("300x200")
#root.configure(bg="azure2")


#opções do menu
btn_filiacao = tk.Button(root, text="Fazer Filiação e Residência", command=abrir_filiacao_residencia, width=20,bg='azure3',fg='#000')
btn_filiacao.pack(pady=20)

btn_requerimento = tk.Button(root, text="Fazer Requerimento", command=abrir_requerimento, width=20, bg='azure3',fg='#000')
btn_requerimento.pack(pady=20)

# novo
btn_fechar = tk.Button(root, text="Sair", command=fechar_janela, bg='red',fg='white',width=20)
btn_fechar.pack(pady=20)
# novo

root.mainloop()
