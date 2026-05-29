#Inicio do sistema
print("Emprestador de dinheiros automáticos do Juninho...")

#Variável de valor e mensagem 
valorEmprest = float(input("Digite quantos Reais você quer emprestado:"))
parcela = int(input("Digite em quantas parcelas você quer pagar:"))
print("Você pagará em", parcela, "parcelas...\n"
      "**Acréscimo de 20% no valor final**")

#Declarando o valor do Juros
juros = 0.20

#Cálculo
valorDivida = valorEmprest * (1 + juros)

#Valor das parcelas
valorParcela = (valorDivida) / (parcela)

print("O valor de cada parcela é: " ,valorParcela, "\n"
      "O valor final a ser pago é: ", valorDivida)