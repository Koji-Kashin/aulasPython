# Faça o computador sorter um número inteiro
# Solicita ao usuário um número e compara para descobrir se ele acertou
# import da biblioteca
import random

# Cria a varíavel do sorteieo e guarda o valor sorteado
numSorteado = random.randint(1, 60)

print(
    "--- ADVINHE O NÚMERO E GANHE UM MEGA PREMIO --- \n"
    "--- FÁCIL, SIMPLES E MILIONÁRIO, REALIZE SEUS SONHOS --- \n"
)

tentativa = int(input("--- Para concorrer, digite um número inteiro: \n" "--- "))

if tentativa == numSorteado:
    print("--- Parabéns, você acertou!!! ---")
else:
    print("--- Deu ruim, mais sorte na próxima ---")
    print(f"O número sorteado era: {numSorteado}")
