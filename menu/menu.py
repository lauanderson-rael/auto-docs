import tkinter as tk
from tkinter import messagebox

# Funções para abrir as janelas correspondentes
def abrir_filiacao_residencia():
    import app

def abrir_requerimento():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Requerimento")
    nova_janela.geometry("300x200")
    label = tk.Label(nova_janela, text="Formulário de Requerimento")
    label.pack(pady=20)
    # Aqui você pode adicionar mais widgets para o formulário

# Configuração da janela principal
root = tk.Tk()
root.title("Menu Principal")
root.geometry("300x200")

# Botões para as opções do menu
btn_filiacao = tk.Button(root, text="Fazer Filiação e Residência", command=abrir_filiacao_residencia)
btn_filiacao.pack(pady=20)

btn_requerimento = tk.Button(root, text="Fazer Requerimento", command=abrir_requerimento)
btn_requerimento.pack(pady=20)

# Iniciar o loop principal da aplicação
root.mainloop()
