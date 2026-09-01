#Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela.

num = int(input())
multiplus = []
multiplicador = 1
for i in range (10):
   prox = num * multiplicador
   multiplicador = multiplicador + 1 
   multiplus.append(prox) 


print (multiplus)
