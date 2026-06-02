# Qual é o número mais maior de todos

print("Boa-noite, vamos descobrir o valor mais maior de todos")

# Colhendo os dados
num1 = int (input("Digite o primeiro número(EM NÚMEROS): "))
num2 = int (input("Digite o segundo número(EM NÚMEROS TAMBÉM)"))

# Verificações

#Primeira verificação
if(num1 > num2):
    print("--- O número ", num1, " é maior do que o número ", num2, " ---")
# Se a de cima der errado tenta essa
elif(num1 == num2):
    print("--- Os números ", num1, " e ", num2, " são iguais ---")
# Se todas as outras não forem, chega até aqui    
else:
    print("--- O número ", num2, " é maior do que o número ", num2, " ---")
       
    