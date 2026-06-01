# Sistema de Elegibilidade para Evento Universitário

# Entrada de dados do estudante
nome = input("Digite o nome do estudante: ")
idade = int(input("Digite a idade: "))
frequencia = float(input("Digite o percentual de frequência: "))
pendencia = input("Possui pendência financeira? (sim/não): ").strip().lower()
matriculado = input("Está matriculado? (sim/não): ").strip().lower()
valor_base = float(input("Digite o valor base do ingresso: R$ "))

# Conversão das respostas para valores lógicos
tem_pendencia = pendencia == "sim"
esta_matriculado = matriculado == "sim"

# Verificação dos critérios de elegibilidade
# Para estar apto, todas as condições precisam ser verdadeiras
apto = idade >= 18 and esta_matriculado and frequencia >= 75 and not tem_pendencia

# Cálculo inicial do valor final
valor_final = valor_base

# Aplicação do desconto de 20%, caso a frequência seja superior a 90%
if frequencia > 90:
    desconto = valor_base * 0.20
    valor_final = valor_base - desconto
else:
    desconto = 0

# Saída de dados
print("\n--- Resultado ---")
print(f"Nome do estudante: {nome}")

if apto:
    print("Situação: Apto")
    print(f"Valor final do ingresso: R$ {valor_final:.2f}")

    if desconto > 0:
        print("Desconto aplicado: 20%")
    else:
        print("Desconto aplicado: Não houve desconto")
else:
    print("Situação: Não apto")
    print("Valor final do ingresso: Não aplicável")
