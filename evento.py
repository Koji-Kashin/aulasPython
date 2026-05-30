"""
#Sistema de elegibilidade
para Evento Universitário

"""

# Iniciando o sistema
print("Carregando sistema...")

valorIngresso = 620.00
# Desconto caso frequência > 90% (20% desconto)
desconto = 20

# Mensagem de boas-vindas
print(
    "Bem-vindo ao sistema de Elegiblidade para a festança e curtição universitária\n"
    "Precisamos das seguintes informações para prosseguir com o seu ingresso e desconto..."
)

# Coleta de dados para comparações...
nome = input(
    "Digite o seu nome: ")
matricula = input(
    "Você está matriculado em algum curso? (responda com Sim ou Não apenas....)"
)

idade = int(input("Agora digite a sua idade em números: "))

freq = int(input("Digite o seu percentual de frequência (Ex: 95%): "))

# Variável para pendência finânceira
divida = input("Você possui pendências finânceiras??")


# Verificação de elegebilidade...

if (idade < 18):
    print("Vá crescer primeiro!!!")
    