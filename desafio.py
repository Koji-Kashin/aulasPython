#Calculador de Médias de Alunos...

# print("Bem-vindo ao Calculador Master de médias de alunos...\n" \
# nota1 = float(input("Digite a primeira nota do aluno: \n"
# nota2 = float(input("Digite a segunda nota do aluno: ")))))

#Boas vindas ao sistema e coleta de dados...
print("Bem-vindo ao Calculador de Notas...")
nome = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

#definindo quantidade de provas para posterior teste
#qtdProvas = float(input("Digite a quantidade de provas feitas durante o semestre:"))




#Exibo as notas
print("A primeira nota foi:", nota1, "e a segunda nota foi:", nota2)

media = float((nota1 + nota2) / 2)

print("A média do aluno", nome,  "foi: ", media)