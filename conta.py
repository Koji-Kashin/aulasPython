# Mensagem pro usuário, coleta, armazenamento de dados e conversão para númer
print(
    "Olá, bem vindo ao maior sistema de contas do universo....\n"
    "Digite dois números diferentes"
)
# float converte string para números decimais
n1 = float(input("Digite o Primeiro número: "))
n2 = float(input("Digite o Segundo núméro: "))

# Exibo os números na tela
print("Seus números são: ", n1, "e", n2)


# Operações Matemáticas
soma = n1 + n2
sub = n1 - n2
div = n1 / n2
multi = n1 * n2

# Resultado das operações
print(
    "A somatória dos números é: ",
    soma,
    "\n" "A subtração dos números é:",
    sub,
    "\n" "A multiplicação dos números é:",
    multi,
)


# Exemplo de como profissionais costumam escrever esse print:
# print(f"A somatória é: {int(sum)}\nA subtração é: {int(sub)}\nA multiplicação é: {int(multi)}")
