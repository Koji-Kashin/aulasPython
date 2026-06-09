#Inicio do sistema...

print("--- Bem-vindo ao Banco Koji --- \n"
      "--- é um prazer ter você aqui ---")

# Fluxo decide se continua ou sai do sistema
opcao = int(input("Digite a opção desejada: 1 (Crédito Imobiliário) 2(Sair): "))
# Determinar Valores, sálário, qtd de anos pagando, acréscimo de 15% do valor do imóvel, limitar comprometimento máximo de renda em 30%...

match opcao:
    case 1:
        valorImovel = float(input("Digite em Reias o valor da casa: R$ "))
    
    #Calcula Juros do financiamento...
        valor_financiamento = valorImovel * 1.15
    
    # Inserção do Salário do cidadão
        salario = float(input("Agora, digite em reais o salário do financiador: R$ "))
        
    # Inserção da quantidade de anos que o cidadão vai pagar ()...
        anosParcelamento = int(input("Digite quantos anos de parcelamento: "))
    
    # Definindo limite da parcela
        limiteParcela = 0.30
    
    # Conversão para meses...
        mesesParcelamento = anosParcelamento * 12
    
    # Cálculo da parcela mensal...
        parcela_Mensal = valor_financiamento / mesesParcelamento
    
    # Critério para aprovação é Parcela < 30% do Salário...
        limite_permitido = salario * limiteParcela
        
        if(parcela_Mensal <= limite_permitido):
            print(f"O valor do imóvel é de: R$ {valorImovel:.2f} \n O valor total do financiamento é: R$ {valor_financiamento:.2f} \nO valor das parcelas é: R$ {parcela_Mensal:.2f} \n  --- Financiamento!! ---")                                 
        else:
            print(" --- Financiamento NEGADO! --- ")            
    case 2:
        print("--- Finalizando o Sistema --- \n"
              "         Finalizado...")