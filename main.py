import tkinter as tk
from tkinter import messagebox
import webbrowser 

# Funções para abrir as janelas correspondentes
def abrir_filiacao_residencia():
    print("Opcao Filiacao selecionada - 'Abrindo Filiacao e Residência'")
    root.destroy()
    import app_dec

def abrir_requerimento():
    print("Opcao Requerimento selecionada - 'Abrindo Requerimento e +'")
    root.destroy()
    import app_req

def fechar_janela():
    print("Opcao Sair selecionada - Fechando Menu Principal")
    root.destroy()

def abrir_link(event):
    webbrowser.open("https://github.com/lauanderson-rael")

# interface - menu principal
root = tk.Tk()
root.title("Bot auxiliar - Menu Principal")
root.geometry("500x350")

# titulo
tk.Label(root, text="O que deseja fazer?", font=("Arial", 16, "bold")).pack(pady=20)

#opções
btn_filiacao = tk.Button(root, font=4, text="Filiação e Residência", command=abrir_filiacao_residencia, width=20, bg='azure3',fg='#000')
btn_filiacao.pack(pady=20)

btn_requerimento = tk.Button(root, font=(4), text="Requerimento e +", command=abrir_requerimento, width=20, bg='azure3',fg='#000')
btn_requerimento.pack(pady=20)

btn_fechar = tk.Button(root,font=(1), text="Sair", command=fechar_janela,bg='red',fg='white',width=20 )
btn_fechar.pack(pady=20)

footer = tk.Label(root, text="Desenvolvido por @lauanderson-rael", fg="blue", cursor="hand2")
footer.pack(pady=20)
footer.bind("<Button-1>", abrir_link)  # Vincular o clique ao link
root.mainloop()
