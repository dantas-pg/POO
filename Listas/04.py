#Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.


lista_original = []
for i in range (10):
    num = int(input('Digite um número'))
    lista_original.append(num)

duplicados = []

for item in lista_original:
    if lista_original.count(item) > 1 and item not in duplicados:
        duplicados.append(item)

print(duplicados)
