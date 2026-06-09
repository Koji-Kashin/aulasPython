#Importa a biblioteca de tempo
import time

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print ("Ituaú, feito para você!")

#Busca o horário atual do usuário
horario = time.localtime()
#Busca os segundos desde de 1970 (CRIAÇÃO DO UNIX)
horario = time.time()
#Converte o horário em segundos para a data atual do usuário
convertido = time.ctime(horario)

print(horario)
print(convertido)