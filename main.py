import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

# Funções para abrir as janelas correspondentes
def abrir_declaracoes():
    print("Opcao Filiacao selecionada - 'Abrindo Filiacao e Residência'")
    root.destroy()
    os.system("python app_dec.py")

def abrir_requerimento():
    print("Opcao Requerimento selecionada - 'Abrindo Requerimento e +'")
    root.destroy()
    os.system("python app_req.py")

def abrir_carteira_socio():
    print("Opcao Carteira de Socio selecionada - 'Abrindo Carteira de Socio'")
    root.destroy()
    os.system("python app_carteira.py")

def fechar_janela():
    print("Opcao Sair selecionada - Fechando Menu Principal")
    root.destroy()

def abrir_link(event):
    webbrowser.open("https://github.com/lauanderson-rael")

# interface - menu principal
root = tk.Tk()
root.title("Bot auxiliar - Menu Principal")
root.geometry("500x365")

# titulo
tk.Label(root, text="O que deseja fazer?", font=("Arial", 16, "bold")).pack(pady=20)

# botao declaracoes
btn_declaracoes = tk.Button(root, font=4, text="Declarações do Pescador", command=abrir_declaracoes, width=24, bg='azure3',fg='#000')
btn_declaracoes.pack(pady=10)

# botao requerimento
btn_requerimento = tk.Button(root, font=(4), text="Requerimento e +", command=abrir_requerimento, width=24, bg='azure3',fg='#000')
btn_requerimento.pack(pady=10)

# botao carteira de socio
btn_carteira_socio = tk.Button(root, font=(4), text="Carteira de Socio", command=abrir_carteira_socio, width=24, bg='azure3',fg='#000')
btn_carteira_socio.pack(pady=10)


btn_fechar = tk.Button(root,font=(1), text="Sair", command=fechar_janela,bg='red',fg='white',width=24 )
btn_fechar.pack(pady=10)

footer = tk.Label(root, text="Desenvolvido por @lauanderson-rael", fg="blue", cursor="hand2")
footer.pack(pady=10)
footer.bind("<Button-1>", abrir_link)  # Vincular o clique ao link
root.mainloop()
