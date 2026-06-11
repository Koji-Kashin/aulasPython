# Importação do CustomTkinter e do Pillow (para o GIF)
import customtkinter as ctk
from PIL import Image

# Cores e fontes (Suas variáveis originais)
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
janela_inicial.configure(fg_color=cor_principal)


# --- SESSÃO DO GIF (PLANO DE FUNDO) 🌌 ---

# 1. Caminho do GIF (lembre-se de manter o caminho correto do seu computador)
caminho_do_gif = r"C:\Users\14151\Downloads\mago.gif"
imagem_gif = Image.open(caminho_do_gif)

# 2. Extrair os "frames" (quadros) do GIF
frames = []
try:
    while True:
        frame_atual = imagem_gif.copy().convert("RGBA")
        # Tamanho exato da janela para preencher o fundo
        frame_ctk = ctk.CTkImage(light_image=frame_atual, size=(500, 350)) 
        frames.append(frame_ctk)
        imagem_gif.seek(len(frames))
except EOFError:
    pass

# 3. Criar o Label do GIF e colocar no fundo da tela
label_gif = ctk.CTkLabel(janela_inicial, text="", fg_color="transparent")
label_gif.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

# 4. Função para animar
def animar_gif(indice=0):
    label_gif.configure(image=frames[indice])
    proximo_indice = (indice + 1) % len(frames)
    janela_inicial.after(50, animar_gif, proximo_indice)

# 5. Dá o play na animação!
animar_gif()


# --- ELEMENTOS DA TELA (SOBRE O GIF) 🔮 ---

# Título principal
titulo = ctk.CTkLabel(
    janela_inicial,
    text="LOGIN DO MAGO!!! 🦆",
    font=("Arial", 40, "bold"),
    text_color="#00ff00",
    fg_color="transparent" # Fundo transparente para ver o GIF
)
titulo.place(relx=0.5, rely=0.15, anchor="center")

# Campo de Login
campo_login = ctk.CTkEntry(
    janela_inicial,
    placeholder_text="Digite seu e-mail místico 📜",
    width=250,
    height=40,
    font=("Arial", 14)
)
campo_login.place(relx=0.5, rely=0.40, anchor="center")

# Campo de Senha
campo_senha = ctk.CTkEntry(
    janela_inicial,
    placeholder_text="Digite sua senha secreta 🔑",
    width=250,
    height=40,
    font=("Arial", 14),
    show="*" # Transforma as letras digitadas em asteriscos
)
campo_senha.place(relx=0.5, rely=0.55, anchor="center")

# Botão de Entrar
botao_entrar = ctk.CTkButton(
    janela_inicial,
    text="Entrar no Reino 🏰",
    width=200,
    height=40,
    font=("Arial", 16, "bold"),
    fg_color=cor_sucesso,
    hover_color="#007a00" # Uma cor um pouco mais escura para o hover
)
botao_entrar.place(relx=0.5, rely=0.75, anchor="center")


# Sempre em último por que sim
janela_inicial.mainloop()