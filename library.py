#Importa a biblioteca para valores aleatório
import random

#randint = retorna um número inteiro aleatório
print(random.randint(1,60))
#uniforme = retorna um número decimal aleatório
print(f'{random.uniform(10,25):.2f}')

#Lista top de lanches
lanches = ["X-Egg Beacon", "Big Mac", "Coca-cola", "Coxinha", "Batata-frita"]

#Escolhe um lanche aleatório
print(random.choice(lanches))