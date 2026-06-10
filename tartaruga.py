# # Importando o módulo de turtle
# import turtle

# # Criando a tela de pintura
# tela = turtle.Screen()
# # Definindo o tamanho da tela
# tela.setup(width=800, height=600)
# # Nome da tela
# tela.title("Desenhando com a turtle")
# # Criando a turtle
# rafael = turtle.Turtle()


# # forward - anda pra frente
# rafael.forward(200)
# # backward - anda pra trás
# rafael.backward(200)
# # right - gira a seta para direita de acordo com o angulo
# rafael.right(90)
# # left - gira a seta para esquerda de acordo com o angulo
# rafael.left(180)
# rafael.forward(200)
# rafael.right(90)
# rafael.forward(200)
# rafael.right(90)
# rafael.forward(200)


# # Sai quando clicar
# tela.exitonclick()

# Importando o módulo turtle
import turtle

# Criando a tela de pintura
tela = turtle.Screen()

# Definindo o tamanho da tela
tela.setup(width=800, height=600)

# Nomeando a tela
tela.title("Desenhando com turtle")

# Criando a turtle
rafael = turtle.Turtle()

# Foward anda pra frente
rafael.forward(200)
# Backward anda para trás
rafael.backward(300)
# Right gira a seta para a direita de acordo com o seu ângulo
rafael.right(90)

# Apaga a tela
rafael.clear()

# Levanta a caneta para reposicionar sem riscar (se não fizer isso, risca até o local determinado)
rafael.penup()

rafael.goto(260, 250)

rafael.pendown()

# Fazer o quadrado dentro do for
for x in range(0, 4):
    rafael.forward(200)
    rafael.left(90)

rafael.clear()

# Desenho
rafael.speed('fastest')
for x in range(0, 6780):
    rafael.forward(x)
    rafael.right(x)
    rafael.left(x)
    rafael.backward(x)
    rafael.right(x)
    rafael.forward(x)
    
# volta para o centro da tela
rafael.home()

# Desenho 3 - crie um círculo
for x in range(0,900):
    rafael.circle(50)
    rafael.left(17)


#volta pro centro da tela e apaga os desenhos
rafael.home()
rafael.clear()



tela.exitonclick()
