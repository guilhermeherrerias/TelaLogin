# Importar bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox

# Criar janela principal
root = tk.Tk()
root.title("Tela de Login")

# Criar labels e entradas para usuário e senha
label_usuario = tk.Label(root, text="Usuário:")
label_usuario.grid(column=0, row=0, padx=5, pady=5)

entrada_usuario = tk.Entry(root, width=20)
entrada_usuario.grid(column=1, row=0, padx=5, pady=5)

label_senha = tk.Label(root, text="Senha:")
label_senha.grid(column=0, row=1, padx=5, pady=5)

entrada_senha = tk.Entry(root, width=20, show="*")
entrada_senha.grid(column=1, row=1, padx=5, pady=5)

# Função para verificar login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    # Verificar se o usuário e senha estão corretos
    if usuario == "admin" and senha == "123456":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos!")

# Criar botão de login
botao_login = tk.Button(root, text="Login", command=verificar_login)
botao_login.grid(column=1, row=2, padx=5, pady=5)

# Iniciar aplicação
root.mainloop()
