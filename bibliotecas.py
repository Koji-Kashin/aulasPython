# Importa biblioteca de matemática
import math

# Cria variável e guarda o valor arredondado para cima
valorArredondado = math.ceil(77.77)
# Cria variável e guarda o valor arredondado para baixo
valorPraBaixo = math.floor(86.23)
# Cria a variável e guarda o resultado da raiz quadrada
raizQuad = math.sqrt(64)
# Cria a variável e guarda o resultado da potência
potencia = math.pow(6, 9)


# Mostra os valores
print(valorArredondado)
print(valorPraBaixo)
print(raizQuad)
print(potencia)


# Exercício
pot = int(input("Digite o primeiro para exponência-lo: "))
expoente = int(input("Digite agora o expoente: "))

print(f"Resultado da potência é: {math.pow(pot,expoente)}")
