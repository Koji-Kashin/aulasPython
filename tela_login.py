# Importação do CustomTkinter
import customtkinter as ctk
from PIL import Image

# Cores e fontes
cor_principal = "#FFFFFF"
cor_secundaria = "#FF0000"
cor_texto = "#000000"
cor_sucesso = "#00A100"
cor_erro = "#FF0000"
fonte_padrao = ("Segoe UI", 20, "bold")

# Criação e definição da tela
janela_inicial = ctk.CTk()
# Título do app
janela_inicial.title("Login do Mago")
# Define o tamanho da janela
janela_inicial.geometry("500x350")
# Define a cor de fundo da janela
janela_inicial.configure(fg_color=cor_principal)

# Criando os elementos da tela
# CTkLabel = cria textos na tela
titulo = ctk.CTkLabel(
    janela_inicial,
    text="LOGIN DO MAGO!!! 🦆",
    font=("Arial", 40, "bold"),
    text_color="#00ff00",
    # Anexa o título na tela
    # Paddy = cria espaços entre os elementos no eixo y
)
titulo.pack(pady="20")

# Texto Usuário
txt_usuario = ctk.CTkLabel(
    janela_inicial, text="👨‍💻 Usuário", font=fonte_padrao, text_color=cor_texto
)
txt_usuario.pack(pady="10")

# Input do usuário
cx_usuario = ctk.CTkEntry(
    janela_inicial, placeholder_text="Digite o seu usuário... ", justify="center"
)
cx_usuario.pack()

# Texto senha
txt_senha = ctk.CTkLabel(
    janela_inicial, text="🔐 Senha", font=fonte_padrao, text_color=cor_texto
)
txt_senha.pack(pady="10")

# Input senha
cx_senha = ctk.CTkEntry(
    janela_inicial, placeholder_text="Digite a sua senha...", justify="center", show="*"
)
cx_senha.pack(pady="10")


# Variáveis para usuário e senha pré-definidos
real_user = "Mago Patolino"
real_password = "Mago123@"


# Função para verificar o login (def = função)
def verificar_login():
    # Guarda as informações das caixinhas
    usuario = cx_usuario.get()
    senha = cx_senha.get()
    # Verificação das informações:
    if usuario == real_user and senha == real_password:
        txt_final.configure(text="LOGIN REALIZADO!!! ✔️", cor_texto=cor_sucesso)
    else:
        txt_final.configure(text="FALHA NA AUTENTICAÇÃO ❌", cor_texto=cor_erro)


# Botão de login
botao_login = ctk.CTkButton(
    janela_inicial,
    text="Login",
    fg_color=cor_secundaria,
    command=verificar_login,
    hover_color=cor_texto,
)
botao_login.pack(pady="10")

# Texto resposta
txt_final = ctk.CTkLabel(janela_inicial, text="", font=("Comic Sans MS", 20, "bold"))
txt_final.pack(pady="10")

# Sempre em último por que sim
janela_inicial.mainloop()
