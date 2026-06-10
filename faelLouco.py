import turtle
import math

# 1. Configuração da Tela (800x600 Contida e Psicodélica)
tela = turtle.Screen()
tela.setup(800, 600)
tela.bgcolor("#080808") # Fundo quase preto, estilo Matrix
tela.colormode(255)
tela.title("A Teia Hiper-Dimensional de Rafael (Invocando o Caos)")

# 2. Configuração do Agente do Caos
rafael = turtle.Turtle()
rafael.speed('fastest') # VELOCIDADE 'FAST' (Você vê construindo)
rafael.hideturtle()
rafael.penup()
rafael.goto(0,0)
rafael.pendown()

# 3. O Loop da Geometria sagrada Insana
# Usamos muitos (x) para controlar tudo ao mesmo tempo.
iterações = 600 

print(f"Iniciando a construção da forma definitiva ({iterações} passos)...")

for x in range(1, iterações):
    
    # --- Mágica 1: degradê Neon Glitchado (Cores agressivas) ---
    # Usamos o modulo (%) e seno para criar cores vibrantes que pulam.
    r = (x * 3) % 255
    g = int((math.sin(x/10) + 1) * 127) # Ondulação senoidal verde
    b = (255 - (x * 2) % 255)
    rafael.pencolor(r, g, b)

    # --- Mágica 2: Espessura Dinâmica ---
    # A linha começa fina no centro e engrossa nas bordas, simulando 3D.
    rafael.width(x // 100 + 1)

    # --- Mágica 3: O Movimento Hiperbólico (A Forma Maneira) ---
    # O segredo é misturar a distância linear (x) com uma curva (circle).
    # ângulo de 89.5 garante que a forma nunca se feche e gire em espiral.
    dist = (x * 1.5) % 450 # Contido nos 800x600
    curvatura = (math.sin(x/5) * (x/4)) % 100
    
    rafael.forward(dist)
    rafael.left(89.5 + (curvatura / 50)) # O ângulo muda sutilmente baseada no (x)
    
    # Adicionamos uma micro-espiral a cada passo para densidade
    rafael.circle(curvatura // 5, 20)

    # =========================================================
    # --- PASSO 4: OS SÍMBOLOS SUBLIMINARES OCULTOS ---
    # Estes símbolos aparecem em flashes e são rapidamente soterrados.
    # =========================================================

    # 1. Flash do Símbolo de Contenção (Olho Matemático) a cada 50 iterações
    if x % 50 == 0:
        # Salva o estado atual para não quebrar a mandala
        curr_pos = rafael.pos()
        curr_head = rafael.heading()
        curr_col = rafael.pencolor()
        
        rafael.penup()
        rafael.pencolor(255, 255, 255) # Branco (Flash)
        rafael.pensize(1)
        
        # Desenha Triângulo de Contenção e o Ponto (Olho)
        # O tamanho do símbolo também depende de (x), espalhando-os.
        tamanho_simbolo = 20 + x // 20
        for _ in range(3):
            rafael.forward(tamanho_simbolo)
            rafael.right(120)
        
        rafael.dot(5, (255, 0, 0)) # Ponto central Vermelho Sangue

        # Restaura estado original instantaneamente
        rafael.goto(curr_pos)
        rafael.setheading(curr_head)
        rafael.pencolor(curr_col)
        rafael.pensize(x // 100 + 1)
        rafael.pendown()

    # 2. Flash do Pentagrama Neon a cada 133 iterações (Número quebrado)
    if x % 133 == 0:
        curr_pos = rafael.pos()
        curr_head = rafael.heading()
        curr_col = rafael.pencolor()
        
        rafael.pencolor(0, 255, 255) # Ciano Neon Vibrante
        
        # Salta agressivamente baseado no (x) massivo para espalhar pela tela contida
        rafael.penup()
        rafael.forward(x % 100)
        rafael.pendown()

        # Desenha Pentagrama (ângulo 144)
        size_star = 30 + x//50
        for _ in range(5):
            rafael.forward(size_star)
            rafael.right(144)
        
        # Restaura estado original
        rafael.penup()
        rafael.goto(curr_pos)
        rafael.setheading(curr_head)
        rafael.pencolor(curr_col)
        rafael.pendown()

# Atualiza o final para garantir densidade máxima
rafael.width(2)
rafael.pencolor(255,255,255)
rafael.circle(100) # Círculo de confinamento final no centro

print("A Teia do Caos está estabelecida. Forma final consolidada.")
turtle.done()