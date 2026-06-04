# Inicio do Sistema...
print(" --- Boa noite, bem vindo ao calculador de terrenos ---")
print("Carregando...")

larguraTerreno = float(input("Digite a largura do seu terreno: "))
comprimentoTerreno = float(input("Agora, digite o comprimento do seu terreno: "))

areaTerreno = (larguraTerreno) * (comprimentoTerreno)

print("O seu terreno tem ", areaTerreno, "m²")

if (areaTerreno <100):
    print("--- O seu terreno é do tipo popular ---")
elif(areaTerreno >= 100 and areaTerreno <= 500):
    print("--- O seu terreno é do tipo Master ---")
else:
    print("--- O seu terreno é o tipo VIP ---")