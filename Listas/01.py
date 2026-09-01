#Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros negativos e a soma dos numeros positivos desse vetor.
import random
lista = []
for i in range (10):
    num = random.randint(-100, 100)
    lista.append(num)

positivos = []
negativos = 0
for j in lista:
    if j > 0:
        positivos.append(j)
    else:
        negativos += 1 

print(negativos)
print(lista)
print(sum(positivos))
        
